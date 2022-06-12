
beta = 0.3
h = 0.1
y = 0.15
n = 60000.0


def u(un, vn, xk, yk):
    u = un - ((h / 2) * (beta / n) * ((vn * un) + (xk * yk)))
    return u


def v(un, vn, xk, yk):
    v = vn + ((h / 2) * (((beta / n) * ((vn * un) + (xk * yk))) - (y * (vn + yk))))
    return v


def w(vn, wn, yk):
    w = wn + ((h / 2) * y * (vn + yk))
    return w


def XK1(u0, v0, xk, yk):
    xk1 = u0 - ((h / 2) * (beta / n) * ((u0 * v0) + (xk * yk)))
    return xk1


def YK1(u0, v0, xk, yk):
    yk1 = v0 - ((h / 2) * (((beta / n) * ((u0 * v0) + (xk * yk))) - (y * (v0 + yk))))
    return yk1

def errorU(un1, un, vn, vn1):
    e = ((un1-un)/h)-((beta / n) * ((vn * un) + (un1 * vn1)))
    return e

def errorV(vn1, vn, un, un1):
    e = ((vn1-vn)/h)-((((beta / n) * ((vn * un) + (un1 * vn1))) - (y * (vn + vn1))))
    return e

def errorW(wn1, wn, vn, vn1):
    e = ((wn1-wn)/h)-(y * (vn + vn1))
    return e

def gauss_seidel(u0, v0):
    ex = 1
    ey = 1
    xk = 0
    yk = 0
    xk1 = u0
    yk1 = v0
    while ex > 0.001 and ey > 0.001:
        xk1 = XK1(u0, v0, xk1, yk1)
        yk1 = YK1(u0, v0, xk1, yk1)

        ex = abs(xk1 - xk)
        ey = abs(yk1 - yk)

        xk = xk1
        yk = yk1
    return xk1, yk1

def main():
    k = 0.0
    u0 = n
    v0 = 120.0
    w0 = 0.0
    ul = []
    vl = []
    wl = []
    xk, yk = gauss_seidel(u0, v0)
    un = u(u0, v0, xk, yk)
    vn = v(u0, v0, xk, yk)
    wn = w(v0, w0, yk)
    ul.append(un)
    vl.append(vn)
    wl.append(wn)
    while k < 102:
        k+=1
        xk, yk = gauss_seidel(un, vn)
        un1 = u(un, vn, xk, yk)
        vn1 = v(un, vn, xk, yk)
        wn1 = w(vn, wn, yk)
        un = un1
        vn = vn1
        wn = wn1
        ul.append(un)
        vl.append(vn)
        wl.append(wn)

    k = 0.0
    u0 = ul[100]
    v0 = vl[100]
    w0 = wl[100]
    ul = []
    vl = []
    wl = []
    xk, yk = gauss_seidel(u0, v0)
    un = u(u0, v0, xk, yk)
    vn = v(u0, v0, xk, yk)
    wn = w(v0, w0, yk)
    ul.append(un)
    vl.append(vn)
    wl.append(wn)
    while k < 400/h:
        k += 1
        xk, yk = gauss_seidel(un, vn)
        un1 = u(un, vn, xk, yk)
        vn1 = v(un, vn, xk, yk)
        wn1 = w(vn, wn, yk)
        un = un1
        vn = vn1
        wn = wn1
        ul.append(un)
        vl.append(vn)
        wl.append(wn)

    print(errorU(ul[-1], ul[-2], vl[-2], vl[-1]))
    print(errorV(vl[-1], vl[-2], ul[-2], ul[-1]))
    print(errorW(wl[-1], wl[-2], vl[-2], vl[-1]))

main()