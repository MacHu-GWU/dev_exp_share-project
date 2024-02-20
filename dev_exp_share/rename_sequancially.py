# -*- coding: utf-8 -*-

"""
在这个项目中, 所有的文档都是扁平结构. 为了保持所有的文档有序, 所有的文档都会从 1, 2, ... 一直到 9999
(最多支持 9999 篇文档) 编号. 为了便于在两篇文档的顺序中间插入新文档, 所有的编号都是 100 的整数倍,
例如 100, 200, ... 一直到 999900. 这个脚本可以给所有的文档进行重新编号.
"""

from .paths import dir_doc_source

step = 100


def normalize_title(title: str) -> str:
    words = [word.strip() for word in title.split() if word.strip()]
    return "-".join(words)


def main():
    p_dir_list = dir_doc_source.sort_by_abspath(
        dir_doc_source.select_dir(
            recursive=False,
            filters=lambda p: p.basename != "_static",
        )
    )
    i = 0
    for p_dir in p_dir_list:
        parts = p_dir.basename.split("-", 1)
        if parts[0].isdigit():
            title = parts[1]
        else:
            title = p_dir.basename
        i += 1
        seq = i * step
        title = normalize_title(title)
        new_basename = f"{seq:06d}-{title}"
        p_dir.moveto(new_basename=new_basename)
