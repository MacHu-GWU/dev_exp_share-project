# -*- coding: utf-8 -*-

"""
"""

import io
import uuid
import gzip
from pathlib import Path

import polars as pl
from more_itertools import batched  # itertools.batched is only available in Python3.12
from memory_profiler import profile

dir_tmp = Path(__file__).absolute().parent.joinpath("tmp")
dir_tmp.mkdir(exist_ok=True)
path_source = dir_tmp.joinpath("source.json.gz")


def make_source():
    """
    一共 1M 行, 每个 uuid 重复 10 次. 压缩前 300MB, 压缩后 26.4MB. 最终的输出是 100 个 3MB 的小文件.
    """
    n_rows = 1_000_000
    data = [{"id": i, "text": uuid.uuid4().hex * 10} for i in range(1, 1 + n_rows)]
    df = pl.DataFrame(data)
    buffer = io.BytesIO()
    df.write_ndjson(buffer)
    path_source.write_bytes(gzip.compress(buffer.getvalue()))


@profile
def main1():
    """
    Line #    Mem usage    Increment  Occurrences   Line Contents
    =============================================================
    31     64.3 MiB     64.3 MiB           1   @profile
    32                                         def main1():
    33   1491.3 MiB   1427.0 MiB           1       lines = gzip.decompress(path_source.read_bytes()).decode("utf-8").splitlines()
    34   1499.3 MiB      7.2 MiB         101       for ith, lst in enumerate(batched(lines, 10000), start=1):
    35   1499.3 MiB      0.0 MiB         100           p = dir_tmp.joinpath(f"{str(ith).zfill(4)}.json")
    36   1499.3 MiB      0.8 MiB         100           p.write_text("\n".join(lst))
    """
    lines = gzip.decompress(path_source.read_bytes()).decode("utf-8").splitlines()
    for ith, lst in enumerate(batched(lines, 10000), start=1):
        p = dir_tmp.joinpath(f"{str(ith).zfill(4)}.json")
        p.write_text("\n".join(lst))


@profile
def main2():
    """
    Line #    Mem usage    Increment  Occurrences   Line Contents
    =============================================================
    49     63.3 MiB     63.3 MiB           1   @profile
    50                                         def main2():
    51    770.5 MiB    707.1 MiB           1       buffer = io.BytesIO(gzip.decompress(path_source.read_bytes()))
    52   1155.3 MiB     14.8 MiB         101       for ith, lst in enumerate(batched(buffer.readlines(), 10000), start=1):
    53   1155.3 MiB      0.0 MiB         100           p = dir_tmp.joinpath(f"{str(ith).zfill(4)}.json")
    54   1155.3 MiB      4.0 MiB         100           p.write_bytes(b"".join(lst))
    """
    buffer = io.BytesIO(gzip.decompress(path_source.read_bytes()))
    for ith, lst in enumerate(batched(buffer.readlines(), 10000), start=1):
        p = dir_tmp.joinpath(f"{str(ith).zfill(4)}.json")
        p.write_bytes(b"".join(lst))


if __name__ == "__main__":
    """ """
    make_source()
    # main1()
    # main2()
