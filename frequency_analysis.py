#!/Users/Ryota/.pyenv/shims/python
# coding=UTF-8
"""
This program will offer you percentages of characters in sentence.
So you use it,you can solve substitution cipher easy.
"""

import re
import sys
import os
import string as st
import matplotlib.pyplot as plt


def freq_analysis(text, char_set=st.ascii_lowercase, pattern=r"[\d | \s | \' | \" | : | ; | -]"):
    """
    frequency analysis module

    Parameters
    ----------
    text : str
        target text
    char_set : str
        Inspect Characters
    pattern : str
        ignore pattern
    Returns
    -------
    data : dict{str: tuple(int, float)}
        {Character: (Count, Percentage)}
    """

    assert len(text) > 0, "text is empty"
    char_len = len(char_set)
    low_text = re.sub(pattern, "", text.lower())
    data = dict()
    for i, s in enumerate(char_set):
        freq = low_text.count(s)
        data[s] = (freq, freq / len(text) * 100)

    ignore_count = len(text) - len(low_text)
    data[".."] = (ignore_count, ignore_count / len(text) * 100)
    return data


def print_table(data, char_set, text_len):
    """
    print table, format → markdown

    Parameters
    ----------
    data : dict
        data
    char_set : str
        check character
    text_len : int
        target text length
    Returns
    -------
    none
    """

    count = 0
    text_format = "| {0:<3} | {1:>10} |   {2:>20.15f} |"
    print("-" * 45)
    print("| chr |      count |         percentage (%) |")
    print("| --- | " + "-"*10 + " | " + "-" * 22 + " |")
    for s in char_set:
        print(text_format.format(s, data[s][0], data[s][1]))
        count += data[s][0]
    print(text_format.format("Σ", count, count/text_len*100))
    print(text_format.format("..", data[".."][0], data[".."][1]))
    print("-" * 45)


def plot_graph(data, char_set, file_name):
    """
    Graph Plot Module for frequency analysis

    Parameters
    ----------
    data : dict{str:tuple(int, float)}
        plot data
    char_set : str
        char_set
    file_name : str
        file_name
    Returns
    -------
    none
    """

    freq = list()
    for s in char_set:
        freq.append(data[s][0])
    plt.bar([i for i in range(len(char_set))], freq)
    plt.xticks([i for i in range(len(char_set))], list(char_set))
    plt.xlabel("Char set")
    plt.ylabel("Count")
    plt.grid(color="gray")
    plt.title("Frequency Analysis for \"" + file_name + "\"")
    file_name = os.path.splitext(file_name)[0]
    plt.savefig(file_name + "_freq.png")
    plt.show()


def main(file_name):
    """
    main module

    Parameters
    ----------
    file_name : str
        target file name
    Returns
    -------
    none
    """

    try:
        f = open(file_name, "r", encoding="UTF-8")
        text = f.read()
        f.close()
    except:
        print(sys.exc_info())
        exit()

    alpha = st.ascii_lowercase
    symbol = "," + "." + "(" + ")" + "{" + "}" + "?" + "!"
    char_set = alpha + symbol

    data = freq_analysis(text, char_set)
    print_table(data, char_set, len(text))
    plot_graph(data, char_set, file_name)


if __name__ == "__main__":
    args = sys.argv
    assert len(args) == 2, "Usage " + args[0] + " file_name"
    main(args[1])
