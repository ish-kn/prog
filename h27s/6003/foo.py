import sys
p = sys.stdout.write


def main():
    f = open('program.txt', 'r')

    for row in f:
        p(row)

    f.close()

if __name__ == '__main__':
    main()
