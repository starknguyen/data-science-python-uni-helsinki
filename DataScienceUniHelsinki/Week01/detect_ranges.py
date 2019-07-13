def detect_ranges(L):
    sorted_list = sorted(L)
    incr = False
    r = []
    low = high = sorted_list[0]
    for i in range(1, len(sorted_list)):
        try:
            if sorted_list[i - 1] + 1 == sorted_list[i]:
                if incr is False:
                    low = sorted_list[i - 1]
                high = sorted_list[i]
                incr = True
                if i == len(sorted_list) - 1:
                    r.append((low, high + 1))
                # print("incr = true, i={}, low = {}, high = {}".format(i,low,high))
            else:
                if incr is True:
                    r.append((low, high + 1))
                else:
                    r.append(sorted_list[i - 1])

                if i == len(sorted_list) - 1:
                    r.append(sorted_list[i])
                    return r

                low = sorted_list[i]
                high = sorted_list[i + 1]
                incr = False
                # print("incr = false, i={}, low = {}, high = {}, r={}".format(i,low,high,r))

        except Exception as e:
            print(e)
    return r


def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)


if __name__ == "__main__":
    main()
