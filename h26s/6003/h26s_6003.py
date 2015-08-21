# -*- coding: utf-8 -*-
# ID: 6003

from math import *

EPS = 1e-10


def equals(a, b):
    return fabs(a - b) < EPS


class Point:

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, a):
        return Point(a * self.x, a * self.y)

    def __div__(self, a):
        return Point(self.x / a, self.y / a)

    def norm(self):
        return self.x**2 + self.y**2

    def abs(self):
        return sqrt(self.norm())

    def __lt__(self, p):
        return self.x < p.x if self.x != p.x else self.y < p.y

    def __eq__(self, p):
        return equals(self.x, p.x) and equals(self.y, p.y)
Vector = Point


def dot(a, b):  # 内積
    return a.x * b.x + a.y * b.y


def cross(a, b):  # 外積の大きさ
    return a.x * b.y - a.y * b.x


def contains(g, p):  # 点の内包
    # IN 2 ON 1 OUT 0
    n = len(g)
    x = False
    for i in xrange(n):
        a = g[i] - p
        b = g[(i + 1) % n] - p
        if abs(cross(a, b)) < EPS and dot(a, b) < EPS:
            return 1
        if a.y > b.y:
            a, b = b, a
        if a.y < EPS < b.y and cross(a, b) > EPS:
            x = not x
    return 2 if x else 0


def AR_0(d):  # (1)
    cnt = 0
    x = 0
    while x <= 10:
        y = 0
        while y <= 10:
            if 0 <= x <= 10 and 0 <= y <= 10:
                cnt += 1
            y += d
        x += d
    return cnt


def AR_1(d):
    cnt = 0
    x = 0
    while x <= 10:
        y = 0
        while y <= 10:
            if (x - 5)**2 + (y - 5)**2 <= 25:
                cnt += 1
            y += d
        x += d
    return cnt


def AR_1R_0(d):  # (2)
    return AR_1(d) / (AR_0(d) * 4.0)


def SK_2():  # (3)
    sq3 = sqrt(3)
    s0 = sq3 / 4 * 100  # S(K_0)
    s1 = s0 + sq3 / 4 * (10 / 3.0)**2 * 3  # S(K_1)
    s2 = s1 + sq3 / 4 * (10 / 9.0)**2 * 12  # S(K_2)
    return s2


def SK_n(n):  # (4)
    sq3 = sqrt(3)
    s = sq3 / 4 * 100
    e = 3
    for i in xrange(1, n + 1):
        s += sq3 / 4 * (10.0 / 3 ** i)**2 * e
        e *= 4
    return s

snow = []


def app(p):
    if equals(p.x, 0):
        p.x = 0.0
    if equals(p.y, 0):
        p.y = 0.0
    snow.append(p)


def koch(n, a, b):  # コッホ雪片の頂点列生成
    if n == 0:
        return
    th = pi * -60 / 180
    s = (a * 2 + b * 1) / 3
    t = (a * 1 + b * 2) / 3
    u = Point(0, 0)
    u.x = (t.x - s.x) * cos(th) - (t.y - s.y) * sin(th) + s.x
    u.y = (t.x - s.x) * sin(th) + (t.y - s.y) * cos(th) + s.y

    koch(n - 1, a, s)
    app(s)
    koch(n - 1, s, u)
    app(u)
    koch(n - 1, u, t)
    app(t)
    koch(n - 1, t, b)


def AK_2(d, n):  # (5), (6)
    del snow[:]
    a = Point(0, 0)
    b = Point(10, 0)
    c = Point(5, 5 * sqrt(3))
    snow.append(a)
    koch(n, a, b)
    snow.append(b)
    koch(n, b, c)
    snow.append(c)
    koch(n, c, a)

    cnt = 0
    x = 0
    while x <= 10:
        y = 0
        while y <= 10:
            p = Point(x, y)
            if contains(snow, p) > 0:
                cnt += 1
            y += d
        x += d

    x = 0
    while x <= 10:
        y = -d
        while y > -3:
            p = Point(x, y)
            if contains(snow, p) > 0:
                cnt += 1
            y -= d
        x += d

    return cnt


def main():
    print '(1) A(d, R_0) (d = 1, 2, ..., 10) =', [AR_0(d) for d in xrange(1, 11)]

    print '(2) A(d, R_1)/A(d, R_0) * 1/4 (d = 1, 2, ..., 10) =',  [AR_1R_0(d) for d in xrange(1, 11)]

    print '(3) S(K_2) =', SK_2()

    print '(4) S(K_n) (n = 0, 1, 2, 3) =', [SK_n(n) for n in xrange(4)]

    print '(5) A(d, K_2) (d = 0.5, 1, 1.5) =', [AK_2(0.5, 2), AK_2(1, 2), AK_2(1.5, 2)]

    print '(6) A(d, K_n) (d = 0.5, 1, 1.5, n = 0) =', [AK_2(0.5, 0), AK_2(1, 0), AK_2(1.5, 0)]
    print '(6) A(d, K_n) (d = 0.5, 1, 1.5, n = 1) =', [AK_2(0.5, 1), AK_2(1, 1), AK_2(1.5, 1)]


if __name__ == '__main__':
    main()
