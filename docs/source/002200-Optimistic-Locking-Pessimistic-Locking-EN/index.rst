Optimistic Locking vs Pessimistic Locking EN
==============================================================================


What is a Distributed Lock?
------------------------------------------------------------------------------
A distributed lock is a mechanism for controlling synchronized access to shared resources in a distributed system. It ensures that only one process or thread can access the shared resource at a time, preventing data inconsistency issues caused by multiple processes modifying data simultaneously. Distributed locks are implemented by storing the lock state in a location accessible to all processes, such as a distributed cache or database.

A typical application scenario for distributed locks is an online ticketing system. Suppose there are many users simultaneously purchasing tickets for the same show online, and the number of tickets is limited. To prevent overselling caused by multiple users buying the same ticket concurrently, the ticketing system needs to use a distributed lock. When a user attempts to purchase a ticket, the system tries to acquire the distributed lock for that ticket. If the lock is successfully obtained, the user can exclusively access the ticket for the subsequent purchase operation. Meanwhile, other users cannot purchase this ticket because they cannot acquire the lock until it is released. This way, the distributed lock ensures that only one user can purchase a specific ticket at a time, avoiding overselling issues.


What are Optimistic Locking and Pessimistic Locking?
------------------------------------------------------------------------------
There are two common implementations of distributed locks: optimistic locking and pessimistic locking. The difference between the two lies in how locks are acquired. Optimistic locking attempts the operation first and then checks if other processes have modified the resource after the operation is completed, while pessimistic locking acquires the lock first and then performs the operation.


Implementation of Optimistic Locking
------------------------------------------------------------------------------
When implementing optimistic locking using a database system, a dedicated field for optimistic locking is required. Usually, this field is an auto-incrementing version number. For example, when a user is ready to purchase a ticket, they first read the ticket data from the database and obtain the version number. Then, when confirming the purchase, the database is updated, and the version number is incremented by 1. When updating the database, it checks if this field matches the previous version number. If they don't match, it means someone has modified the data before you, and you need to re-read the data and try to purchase again. Therefore, optimistic locking does not involve adding row locks in the database (implemented by ``SELECT ... FOR UPDATE`` in relational databases), **so optimistic locking is actually not a lock**. Everyone is optimistic and believes that the probability of conflicts is low, so they proceed with the operation first and then check for conflicts, retrying if necessary. This is the origin of the term "optimistic locking."

When implementing optimistic locking using a database system, the database system must support these two features:

1. **All write operations on the same data must be executed sequentially on the server-side**. The next write operation cannot be executed until the previous one is completed. This isolation mechanism is called Isolation Level. This condition cannot be guaranteed in some non-relational and distributed databases.
2. **The database update operation must support conditional update**. In SQL, this is implemented through ``UPDATE ... WHERE version = ...``. Not all databases support this operation; for example, Redis does not.

**Advantages of optimistic locking**:

- Simple, requiring only one read and one write operation, with no need for frequent locking (because there is no locking action), reducing the overhead of locking.
- Suitable for scenarios with low concurrency conflicts, offering better performance.
- Non-blocking, does not cause thread waiting.

**Disadvantages of optimistic locking**:

- In highly concurrent and competitive scenarios, a large number of workers spend most of their time constantly re-reading data and retrying. Statistically speaking, assuming there are K workers competing for the same resource, and the business processing time is A, in the case of no conflicts, it can be done within A * K time. However, in the case of conflicts, in extreme situations, the first attempt consumes A * K time, but only one worker succeeds. The second attempt consumes A * (K - 1), then A * (K - 2), ... and finally, it consumes A * K * K / 2 time.


Implementation of Pessimistic Locking
------------------------------------------------------------------------------
When implementing pessimistic locking using a database system, two dedicated fields are required: one for the lock itself and another for the lock acquisition time. The lock is represented as a string; "NA" indicates that it is not locked, and a randomly generated UUID indicates that it is locked. The lock acquisition time is used to prevent the resource from being locked by a worker and then the worker program crashing, causing the lock to be unable to be released. An expiration time can be set for the lock, such as 1 minute (assuming the business operation time will not exceed 1 minute). When the lock acquisition time exceeds 1 minute, even if there is a lock, it is treated as if there is no lock.

The business process using pessimistic locking is as follows:

1. Whenever a worker needs to obtain a resource, it first obtains the resource and checks whether the lock is "NA" or has expired (we'll simply call it locked or not locked later). If it is locked, the entire process is directly stopped.
2. If it is found to be unlocked, a randomly generated UUID is used, and this data is updated. This operation is implemented in SQL through ``UPDATE ... WHERE lock = 'NA'``. Therefore, pessimistic locking also requires the database update operation to support conditional judgment. If the update operation fails, it means that between the worker checking the lock and acquiring the lock, someone else has locked it.
3. This locking operation can be further optimized to ``UPDATE ... WHERE lock = 'NA' OR lock = 'your_UUID'``. The meaning of this operation is that if the lock on the database side is the same as the lock on the worker side, it means that this lock was acquired by me. Although it is already locked, I can still continue to execute the business logic or update the lock time. This is suitable for an application scenario where a worker wants to update the lock again before releasing it.
4. When the worker completes the business logic, it releases the lock. This operation is implemented through ``UPDATE ... WHERE lock = 'your_UUID'``. Logically, this update operation cannot fail because if the lock is different, it should have stopped at the second step.

In summary, pessimistic locking is a logical lock, not a physical lock like a database row lock. If everyone does not follow the rules and ignores this lock, then the lock has no meaning at all. Therefore, the implementation of pessimistic locking depends on the business logic and cannot completely rely on the database system.

**Advantages of pessimistic locking**:

- Ensures strong data consistency and prevents dirty reads.

**Disadvantages of pessimistic locking**:

- Poor concurrency performance and the existence of lock competition problems.
- Prone to deadlocks.
- High cost of locking and performance overhead.


Implementing Optimistic Locking and Pessimistic Locking with Relational Databases
------------------------------------------------------------------------------
Most relational databases can ensure that update operations on the same row are executed sequentially and support the ``UPDATE ... WHERE ...`` operation. Therefore, relational databases can implement both optimistic locking and pessimistic locking.


Implementing Optimistic Locking and Pessimistic Locking with Amazon DynamoDB
------------------------------------------------------------------------------
DynamoDB can ensure that update operations on the same row are executed sequentially, and the Update operation supports Condition Expression (similar to ``UPDATE ... WHERE ...``). Therefore, DynamoDB can implement both optimistic locking and pessimistic locking.

Reference:

- `Isolation levels for DynamoDB transactions <https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/transaction-apis.html#transaction-isolation>`_


Implementing Optimistic Locking and Pessimistic Locking with MongoDB
------------------------------------------------------------------------------
MongoDB can ensure that update operations on the same row are executed sequentially and supports the Query for Update operation (similar to ``UPDATE ... WHERE ...``). Therefore, MongoDB can implement both optimistic locking and pessimistic locking.

References:

- `Atomicity and Transactions <https://docs.mongodb.com/manual/core/write-operations-atomicity/>`_
- `Concurrency Control <https://docs.mongodb.com/manual/faq/concurrency/>`_
- `Read Isolation, Consistency, and Recency <https://docs.mongodb.com/manual/core/read-isolation-consistency-recency/>`_
