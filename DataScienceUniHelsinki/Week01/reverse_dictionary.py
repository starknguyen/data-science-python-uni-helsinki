#!/usr/bin/env python3
def reverse_dictionary(d):
    retval = {}
    for k, v in d.items():
        for val in v:
            if val in retval:
                retval[val].append(k)
            else:
                retval.update({val: [k]})
    return retval


def main():
    d = {"move": ["liikuttaa"], "hide": ["piilottaa", "salata"], "six": ["kuusi"], "fir": ["kuusi"]}
    print(reverse_dictionary(d))


if __name__ == "__main__":
    main()
