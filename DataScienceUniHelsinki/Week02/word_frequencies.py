#!/usr/bin/env python3
import re

def word_frequencies(filename):
    """
    This method can be done faster by counting each time reading a line
    But here, for the sake of regex practice...
    :param filename:
    :return:
    """
    with open(filename, 'r') as f:
        content = f.read()
        lines = content.split('\n')

    words = []
    retval_dict = {}
    for line in lines:
        ls = line.split()
        for w in ls:
            words.append(w.strip("""!"#$%&'()*,-./:;?@[]_"""))

    # Take care of the duplication
    words = list(dict.fromkeys(words))
    for word in words:
        # Note: "Rabbit" word should be different than "Rabbit's"
        # pattern = r"(?=\b%s\b)" % re.escape(word)
        # pattern = r"(?<!\S)%s(?!\S)" % re.escape(word)
        pattern = r"(?=\b%s[^'])" % re.escape(word)
        count = len(re.findall(pattern, content))
        # result = "{}\t{}".format(word, count)
        # print(result)
        retval_dict.update({word: count})

    # print(len(retval))
    return retval_dict


def main():
    print(word_frequencies("alice.txt"))


if __name__ == "__main__":
    main()
