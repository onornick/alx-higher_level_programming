#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv

    argc = len(argv)
    if argc == 1:
        add = 0
    add = 0
    index = 1
    while index < argc:
        add += int(argv[index])
        index += 1
    print(add)
