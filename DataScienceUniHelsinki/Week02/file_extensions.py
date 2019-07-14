#!/usr/bin/env python3

def file_extensions(filename):
    file_exts = []
    retval = []
    file_map_dict = {}
    with open(filename, 'r') as f:
        for f_name in f.readlines():
            if '.' in f_name:
                ext = f_name.rstrip('\n').split('.')[-1]
                if ext not in file_exts:
                    file_exts.append(ext)
                    file_map_dict[ext] = [f_name.rstrip('\n')]
                else:
                    file_map_dict[ext].append(f_name.rstrip('\n'))
            else:
                retval.append([f_name.rstrip('\n')])

    retval.append(file_map_dict)
    return retval


def main():
    fe = file_extensions("/home/nguydin/PycharmProjects/data-science-python-uni-helsinki/DataScienceUniHelsinki/Week02/filenames.txt")
    print(f"{len(fe[0])} files with no extension")
    for k, v in fe[1].items():
        print(f"{k}\t{len(v)}")


if __name__ == "__main__":
    main()
