Sync data from normalized RDBMS model to denormalized NoSQL model
==============================================================================
在业内, 将关系数据库中的数据在保持 Schema 一致的前提下同步到分析型数据仓库的方案已经非常成熟了. 但在实际应用中, 经常会有 Target 数据库的 Schema 和 Source 数据库的 Schema 不一致的情况, 特别是存在 Denormalization 的情况. 举例来说, 在 MongoDB 中, 我们一般使用 Denormalized data model 来存数据, 将相关的数据提前放在一起以避免 JOIN. 但在 RDBMS 中一般是用 normalized data model, 遵循二范式来进行数据建模. 具体的例子如下:

我们用一个论坛应用举例. 一个 Post (帖子) 可以有很多 Tag (标签), 它们是多对多的关系. 在 RDBMS 中, 我们会有三个表: Post, Tag 和 PostTag. 其中 PostTag 是连接表, 它有两个字段: post_id 和 tag_id. 在 MongoDB 中, 我们会将 Post 和 Tag 的信息放在一起, 一个 Post 的数据结构如下:

.. code-block:: python

    {
        "_id": "post-1",
        "title": "Hello, world!",
        "content": "This is my first post!",
        "tags": [
            {"id": "tag-1", "name": "this is tag 1"},
            {"id": "tag-2", "name": "this is tag 2"},
        ]
    }

一般的数据库同步策略都是用的 Capture of Data Change (CDC) Stream. 但是在这个需求下, 跟 PostTag 相关的数据会长这个样子:

.. code-block:: python

    # 假设原先 post-1 的 tag 是 1 和 2, 后来修改为 2 和 3
    # 这在数据库中一般是两个 SQL 语句,
    # 第一个是在 PostTag 中删除 post-1, tag-1,
    # 第二个是在 PostTag 中插入 post-1, tag-3,
    # 那么在 CDC Stream 中你会看到
    # first
    {
        "operation": "delete",
        "data": {
            "post_id": "post-1",
            "tag_id": "tag-1",
        }
    }
    # second
    {
        "operation": "insert",
        "data": {
            "post_id": "post-1",
            "tag_id": "tag-3",
        }
    }

那么在这个 stream consumer 我们应该怎么处理呢? 有两种方法:

1. 在数据同步实时性要求很高的情况下, 我们需要一条条的处理. 对于第一条, 我们从 ``{"tags": [...]}`` 中删除对应的 Tag, 对于第二条我们添加对应的 Tag. 这样对下游的同步数据库的吞吐量要求比较高, 至少不能比原来的数据库慢. 不过对于分布式数据库例如 MongoDB 或者 DynamoDB 来说, 这点肯定是满足的.
2. 在数据同步实时性要求不高的情况下, 我们可以把 Stream 中的数据根据 primary key aggregate 起来, 一般 stream 中的数据只要是属于同一个 primary key 的话, 多条记录的时间是跟实际 RDBMS 中的数据变更发生的时间是严格一致的. 这样 aggregate 之后我们就可以跳过很多中间的数据状态, 直接计算出最终的状态, 然后用一个 Update 就可以搞定了. 减少了 Target 数据库的压力.

当然以上的讨论只是一个非常简单和理想的情况. 实际情况中的数据关系会比这复杂的多, 你可能需要处理很多的 edge case, 例如数据的冲突, 数据的丢失等等. 但是这个方案是一个很好的起点, 你可以根据自己的需求来进行扩展.
