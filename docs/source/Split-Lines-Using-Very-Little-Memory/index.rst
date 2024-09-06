Split Lines Using Very Little Memory
==============================================================================
在大数据处理领域, 将大数据分而治之是非常常用的技巧. 例如将一个 CSV 或者 NDJSON 按行拆分成小文件然后分而治之.

下面这个例子给出了 Python 中的最优实现 (``main2``).

.. dropdown:: example.py

    .. literalinclude:: ./example.py
       :language: python
       :emphasize-lines: 1-1
       :linenos:

