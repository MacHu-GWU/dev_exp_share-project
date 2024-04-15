# -*- coding: utf-8 -*-

"""
这是一个将中文文本转化为英文格式的脚本.

1. 把中文标点符号转换为英文标点符号.
2. 把中文和英文之间加上空格.
3. 在一些 "([<,." 等标点符号的前后视情况加上空格.

How to use:

翻到本脚本最下面, 将你的文本内容写在 main 函数的 text 变量中, 然后运行脚本即可. 它会自动
将输出的文本拷贝到剪贴板, 你只需 Ctrl + V 复制既可.

Requirements::

    pyperclip>=1.8.2,<2.0.0
"""

import string

mapper = {
    "‘": "'",
    "（": "(",
    "）": ")",
    "，": ",",
    "。": ".",
    "－": "-",
    "–": "-",
    "？": "?",
    "：": ":",
    "；": ";",
    "！": "!",
    "、": ",",
    "…": "...",
    "“": '"',
    "”": '"',
    "《": "<",
    "》": ">",
    "【": "[",
    "】": "]",
    "～": "~",
}

pre_space_chars = {"(", "[", "<"}
post_space_chars = {")", "]", ">", ",", ".", ":", ";", "?", "!"}
pre_and_post_space_chars = {"/", "|", "&", "+"}
non_cn_chars = set(string.ascii_letters + string.digits + string.punctuation)
ascii_chars = set(string.ascii_letters + string.digits)
stop_chars = {",", ".", ":", ";", "?", "!"}


def main(text: str) -> str:
    chars = [mapper.get(char, char) for char in list(text)]
    print("--- after mapper ---\n{}".format("".join(chars)))  # for debug only
    new_chars = list()
    for i, char in enumerate(chars):
        if char in pre_space_chars:
            try:
                if chars[i - 1] != " ":
                    new_chars.append(" ")
                    new_chars.append(char)
                else:
                    new_chars.append(char)
            except IndexError:
                new_chars.append(" ")
                new_chars.append(char)

        elif char in post_space_chars:
            try:
                c = chars[i + 1]
                if c != " " and c not in stop_chars:
                    new_chars.append(char)
                    new_chars.append(" ")
                else:
                    new_chars.append(char)
            except IndexError:
                new_chars.append(char)
                new_chars.append(" ")

        elif char in pre_and_post_space_chars:
            try:
                if chars[i - 1] != " ":
                    new_chars.append(" ")
            except IndexError:
                pass
            new_chars.append(char)
            try:
                c = chars[i + 1]
                if c != " " and c not in stop_chars:
                    new_chars.append(" ")
            except IndexError:
                pass

        else:
            # 如果是 a-zA-Z0-9
            if char in ascii_chars:
                #
                try:
                    if chars[i - 1] not in non_cn_chars:
                        new_chars.append(" ")
                except IndexError:
                    pass
                new_chars.append(char)
                try:
                    if chars[i + 1] not in non_cn_chars:
                        new_chars.append(" ")
                except IndexError:
                    pass
            else:
                new_chars.append(char)
    text = "".join(new_chars)
    print(f"--- after format ---\n{text}")  # for debug only
    new_text = " ".join([word for word in text.split(" ") if word.strip()])
    print("--- output ---")  # for debug only
    print(new_text)
    return new_text


# enter your text here
text = """
W-2表格，又叫做年度工资总结表，W-2表格是雇主需要在每个报税年结束之后发给每个雇员和美国国家税务局Internal Revenue Service(IRS)的报税文件。W-2表格报告了员工的年薪和工资中扣缴的各类税款（联邦税、州税、地方税等）。W-2是非常非常非常重要的报税文件，里面的信息是填写报税表的关键！
""".strip()
new_text = main(text)

try:
    import pyperclip

    pyperclip.copy(new_text)
    print("output copied to clipboard! You can paste it now.")
except ImportError:
    pass

