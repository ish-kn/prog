# -*- coding: utf-8 -*-
# ID: 6003

import sys
p = sys.stdout.write


def cntSemi():  # (1)
    f = open('program.txt', 'r')

    cnt = 0
    for row in f:
        cnt += row.count(':')
    f.close()

    return cnt


def printMain():  # (2)
    f = open('program.txt', 'r')

    i = 1
    for row in f:
        if 'main' in row:
            print i, ':', row
        i += 1
    f.close()


def clone3():  # (3)
    f = open('program.txt', 'r')

    clones = set()
    prev = ''
    for row in f:
        if row == prev:
            clones.add(row)
        prev = row
    f.close()

    for clone in clones:
        p(clone)


def clone4():  # (4)
    f = open('program.txt', 'r')
    rows = []
    for row in f:
        rows.append(row)
    f.close()

    clones = []
    for i in xrange(len(rows)):
        for j in xrange(i + 1, len(rows)):
            if rows[i] == rows[j] and not rows[i] in clones:
                clones.append(rows[i])

    for clone in clones:
        p(clone)
    print '\nTotal number of rows =', len(clones)


def isSimilar(row1, row2):
    if row1 == row2:
        return False
    row1 = row1[:len(row1) - 1]
    row2 = row2[:len(row2) - 1]
    if len(row1) > len(row2):
        row2 = row2 + ' ' * (len(row1) - len(row2))
    elif len(row1) < len(row2):
        row1 = row1 + ' ' * (len(row2) - len(row1))

    cnt = 0
    for i in xrange(len(row1)):
        if row1[i] != row2[i]:
            cnt += 1
    return cnt < 5


def clone5():  # (5)
    f = open('program.txt', 'r')
    rows = []
    for row in f:
        rows.append(row)
    f.close()

    clones = []
    for i in xrange(len(rows)):
        if len(rows[i]) < 20:
            continue
        for j in xrange(i + 1, len(rows)):
            if isSimilar(rows[i], rows[j]):
                clones.append((rows[i], rows[j]))

    for clone in clones:
        p(clone[0])
        p(clone[1])
        p('\n')
    print 'Total number of sets =', len(clones)


def editDistance(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    s1 = ' ' + s1
    s2 = ' ' + s2
    dp = [[0 for j in xrange(l2 + 1)] for i in xrange(l1 + 1)]
    for i in xrange(l1 + 1):
        dp[i][0] = i
    for i in xrange(l2 + 1):
        dp[0][i] = i

    for i in xrange(1, l1 + 1):
        for j in xrange(1, l2 + 1):
            cost = 0
            if s1[i] != s2[j]:
                cost = 1
            dp[i][j] = min(
                dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)

    return dp[l1][l2]


def clone6():  # (6)
    f = open('program.txt', 'r')
    rows = []
    for row in f:
        rows.append(row)
    f.close()

    clones = []
    for i in xrange(len(rows)):
        if len(rows[i]) < 20:
            continue
        for j in xrange(i + 1, len(rows)):
            if rows[i] != rows[j] and editDistance(rows[i], rows[j]) < 4:
                clones.append((rows[i], rows[j]))

    for clone in clones:
        p(clone[0])
        p(clone[1])
    print '\nTotal number of sets =', len(clones)


def clone7():  # (7)
    f = open('program.txt', 'r')
    rows = ()
    for row in f:
        rows += (row,)
    f.close()

    clones = set()
    i = 0
    while i < len(rows) - 3:
        cnt = 0
        for j in xrange(i + 1, len(rows)):
            if rows[i] == rows[j]:
                cnt += 1
            else:
                if cnt >= 3:
                    clones.add(rows[i:i + cnt + 1])
                i = j
                break

    for clone in clones:
        for row in clone:
            p(row)
        p('\n')


def main():
    print '(1) Number of semis =', cntSemi()

    print '(2)'
    printMain()

    print '(3)'
    clone3()

    print '(4)'
    clone4()

    print '(5)'
    clone5()

    print '(6)'
    clone6()

    print '(7)'
    clone7()

if __name__ == '__main__':
    main()
