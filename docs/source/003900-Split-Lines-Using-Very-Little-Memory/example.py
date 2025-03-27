# -*- coding: utf-8 -*-

"""
"""

import io
import uuid
import gzip
import time
from pathlib import Path

import polars as pl
from more_itertools import batched  # itertools.batched is only available in Python3.12
from memory_profiler import profile

dir_tmp = Path(__file__).absolute().parent.joinpath("tmp")
dir_tmp.mkdir(exist_ok=True)
path_source = dir_tmp.joinpath("source.json.gz")


def make_source():
    """
    一共 1M 行, 每个 uuid 重复 100 次 (一条记录大约 3KB). 压缩前 3200MB, 压缩后 34.8MB.
    最终的输出是 100 个 32MB 的小文件.
    """
    n_rows = 1_000_000
    data = [{"id": i, "text": uuid.uuid4().hex * 100} for i in range(1, 1 + n_rows)]
    df = pl.DataFrame(data)
    buffer = io.BytesIO()
    df.write_ndjson(buffer)
    path_source.write_bytes(gzip.compress(buffer.getvalue()))


@profile
def main1():
    """
    elapsed = 3.99

    Line #    Mem usage    Increment  Occurrences   Line Contents
    =============================================================
    34     63.3 MiB     63.3 MiB           1   @profile
    35                                         def main1():
    46   4531.5 MiB   4468.2 MiB           1       lines = gzip.decompress(path_source.read_bytes()).decode("utf-8").splitlines()
    47   4562.5 MiB -11951.4 MiB         101       for ith, lst in enumerate(batched(lines, 10000), start=1):
    48   4562.5 MiB  -8820.7 MiB         100           p = dir_tmp.joinpath(f"{str(ith).zfill(4)}.json")
    49   4593.3 MiB  -8759.2 MiB         100           p.write_text("\n".join(lst))
    """
    lines = gzip.decompress(path_source.read_bytes()).decode("utf-8").splitlines()
    for ith, lst in enumerate(batched(lines, 10000), start=1):
        p = dir_tmp.joinpath(f"{str(ith).zfill(4)}.json")
        p.write_text("\n".join(lst))


@profile
def main2():
    """
    elapsed = 2.2

    Line #    Mem usage    Increment  Occurrences   Line Contents
    =============================================================
    52     62.7 MiB     62.7 MiB           1   @profile
    53                                         def main2():
    64   3543.1 MiB   3480.4 MiB           1       buffer = io.BytesIO(gzip.decompress(path_source.read_bytes()))
    65   6985.7 MiB     80.7 MiB         101       for ith, lst in enumerate(batched(buffer.readlines(), 10000), start=1):
    66   6985.7 MiB      0.0 MiB         100           p = dir_tmp.joinpath(f"{str(ith).zfill(4)}.json")
    67   6985.7 MiB      1.9 MiB         100           p.write_bytes(b"".join(lst))
    """
    buffer = io.BytesIO(gzip.decompress(path_source.read_bytes()))
    for ith, lst in enumerate(batched(buffer.readlines(), 10000), start=1):
        p = dir_tmp.joinpath(f"{str(ith).zfill(4)}.json")
        p.write_bytes(b"".join(lst))


if __name__ == "__main__":
    st = time.process_time()
    # make_source()
    main1()
    # main2()
    et = time.process_time()
    elapse = et - st
    print(f"{elapse = }")
