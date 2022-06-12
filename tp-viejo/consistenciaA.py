
beta = 0.3
h = 0.1
y = 0.15
n = 60000.0

def f(i, s):
    fx = ((-beta)/n)*i*s
    return fx

def g(i, s):
    gx = ((beta/n)*i*s) - (y*i)
    return gx

def k(i):
    kx = (y*i)
    return kx

def u1_2(un, vn):
    u = un + ((h/2)*f(vn, un))
    return u

def v1_2(un, vn):
    v = vn + ((h/2)*g(vn, un))
    return v

def w1_2(wn, vn):
    w = wn + ((h/2)*k(vn))
    return w

def u1(un, vn):
    u = un + (h * f(v1_2(un, vn), u1_2(un, vn)))
    return u

def v1(un, vn):
    v = vn + (h*g(v1_2(un, vn), u1_2(un, vn)))
    return v

def w1(un, vn, wn):
    w = wn + (h*k(v1_2(un, vn)))
    return w

def errorU(un1, un, vn):
    e = ((un1-un)/h)-((-beta/n)*vn*un)
    return e

def errorV(vn1, vn, un):
    e = ((vn1-vn)/h)-(((beta/n)*vn*un)-(y*vn))
    return e

def errorW(wn1, wn, vn):
    e = ((wn1-wn)/h)-(y*vn)
    return e

def main():
    k = 0.0
    u0 = n
    v0 = 120.0
    w0 = 0.0
    u = []
    v = []
    w = []
    un = u1(u0, v0)
    vn = v1(u0, v0)
    wn = w1(u0, v0, w0)
    u.append(un)
    v.append(vn)
    w.append(wn)
    while k < 102:
        k+=1
        un1 = u1(un, vn)
        vn1 = v1(un, vn)
        wn1 = w1(un, vn, wn)
        un = un1
        vn = vn1
        wn = wn1
        u.append(un)
        v.append(vn)
        w.append(wn)

    k = 0.0
    u0 = u[100]
    v0 = v[100]
    w0 = w[100]
    u = []
    v = []
    w = []
    un = u1(u0, v0)
    vn = v1(u0, v0)
    wn = w1(u0, v0, w0)
    u.append(un)
    v.append(vn)
    w.append(wn)
    while k < 400/h:
        k += 1
        un1 = u1(un, vn)
        vn1 = v1(un, vn)
        wn1 = w1(un, vn, wn)
        un = un1
        vn = vn1
        wn = wn1
        u.append(un)
        v.append(vn)
        w.append(wn)

    print(errorU(u[-1], u[-2], v[-2]))
    print(errorV(v[-1], v[-2], u[-2]))
    print(errorW(w[-1], w[-2], v[-2]))

main()