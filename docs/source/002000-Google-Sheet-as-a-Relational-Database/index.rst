Google Sheet as a Relational Database
==============================================================================


Overview
------------------------------------------------------------------------------
在传统关系数据库中, 你可以用范式对 one-to-many, many-to-many 进行建模, 然后用 JOIN 对这些关系进行搜索并 filter.

本文探讨了使用 Google Sheet 当做一个关系数据库并通过函数和 UI 来实现对复杂的关系进行搜索和 filter 的可能性. 虽然 Google Sheet 的 Query language 的 JOIN 语法非常难写, 并且性能及其糟糕, 但是通过一些技巧, 我们还是可以实现一些复杂的查询.

- `Sample Google Sheet <https://docs.google.com/spreadsheets/d/1nCBJHCjUkHwY-w-iTRvqySJmkrTggF3W91y4XMAFMt0/edit#gid=1872810320>`_


Reference
------------------------------------------------------------------------------
- `深入分析 Z-Order￼<http://www.aceconsider.com/?p=64>`_
