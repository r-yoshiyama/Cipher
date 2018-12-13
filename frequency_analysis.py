#!/Users/Ryota/.pyenv/shims/python
# coding=UTF-8
"""
This program will offer you percentages of characters in sentence.
So you use it,you can solve substitution cipher easy.
"""

import re
import string as st
import matplotlib.pyplot as plt

def freq_analysis(text, char_set=st.ascii_lowercase, pattern=r"[\d | \s | \' | \" | : | ; | -]"):
    """
    frequency analysis function
    text <- target text
    char_set <- Search character
    pattern <- Patterns of excluded characters
    """

    char_len = len(char_set)
    low_text = re.sub(pattern, "", text.lower())
    text_length = len(low_text)
    freq = [0 for i in range(char_len)]
    data = [[0 for i in range(3)] for j in range(char_len)]
    test = []
    for i, s in enumerate(char_set):
        freq[i] = low_text.count(s)
        data[i][0] = s
        data[i][1] = freq[i]
        data[i][2] = freq[i] / text_length * 100
        test.append(s)

    return data, freq

def main():
    """ Main function """

    file_name = input("File Name >>> ")
    f = open(file_name, "r", encoding="UTF-8")
    text = f.read()
    f.close()

    alpha = st.ascii_lowercase
    symbol = "," + "." + "(" + ")" + "{" + "}" + "?" + "!"
    char_set = alpha + symbol

    data, freq = freq_analysis(text, char_set)

    print("\nLength of the text : " + str(len(text)))
    for i in range(len(freq)):
        print("{0} : {1:>10}     {2:>20}%".format(data[i][0], data[i][1], data[i][2]))
    print("Σ : {0:>10}     {1:>20}%".format(sum(freq), sum(freq)/len(text) * 100))
    print("Most frequently appearance character >>> " + data[freq.index(max(freq))][0])

    plt.bar([i for i in range(len(char_set))], freq)
    plt.xticks([i for i in range(len(char_set))], list(char_set))
    plt.xlabel("Char set")
    plt.ylabel("Count")
    plt.grid(color="gray")
    plt.title("Frequency Analysis for \"" + file_name + "\"")
    plt.savefig(file_name + "_freq-ana.png")
    plt.show()

if __name__ == "__main__":
    main()
