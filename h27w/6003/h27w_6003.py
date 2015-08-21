# -*- coding: utf-8 -*-
# ID: 6003


def f(n):  # (1)
    if n < 1:
        return 1
    else:
        return (161 * f(n - 1) + 2457) % 2**24


def cnt_i():  # (2)
    cnt = 0
    for i in xrange(100):
        if f(i) % 2 == 0:
            cnt += 1
    return cnt


def cnt_i_odd():  # (3)
    cnt = 0
    for i in xrange(100):
        if f(i) % 2 == 0 and i % 2 == 1:
            cnt += 1
    return cnt


def f_dp(n):  # (4)
    f = 1
    for i in xrange(n):
        f = (161 * f + 2457) % 2**24
    return f


def g(n):  # (5)
    g = 1
    for i in xrange(n):
        g = (1103515245 * g + 12345) % 2**26
    return g


def G(n, g):
    if (n < 1):
        return 1
    return (1103515245 * g + 12345) % 2**26


def calc_gk(n):  # (6)
    gn = 1
    for i in xrange(n):
        gn = G(n, gn)

    gnk = gn
    k = 1
    while 1:
        gnk = G(n + k, gnk)
        if gnk == gn:  # g(n + k) == g(n)
            return k
        k += 1


def h(gn):
    return gn % 2**10


def calc_hk(n):  # (7)
    gn = 1
    for i in xrange(n):
        gn = G(n, gn)

    hn = h(gn)
    gnk = gn
    k = 1
    while 1:
        gnk = G(n + k, gnk)
        hnk = h(gnk)
        if hnk == hn:  # h(n + k) == h(n)
            return k
        k += 1


def main():
    print 'f(100) =', f(100)

    print 'Number of i =', cnt_i()

    print 'Number of i(odd) =', cnt_i_odd()

    print 'f(1000000) =', f_dp(1000000)

    print 'g(2) =', g(2)
    print 'g(3) =', g(3)

    print 'gk =', calc_gk(2**13)

    print 'hk =', calc_hk(2**5)

if __name__ == '__main__':
    main()
