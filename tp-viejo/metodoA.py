
beta = 0.3
h = 1.0
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

def main():
    k = 0.0
    u0 = n
    v0 = 120.0
    w0 = 0.0
    un = u1(u0, v0)
    vn = v1(u0, v0)
    wn = w1(u0, v0, w0)
    print("n:",k+1, "/ u" + str(k+1) + ":", un, "/ v" + str(k+1) + ":",vn, "/ w" + str(k+1) + ":",wn)
    while k < 120:
        k+=1
        un1 = u1(un, vn)
        vn1 = v1(un, vn)
        wn1 = w1(un, vn, wn)
        un = un1
        vn = vn1
        wn = wn1
        print("n:", k + 1, "/ u" + str(k + 1) + ":", un, "/ v" + str(k + 1) + ":", vn, "/ w" + str(k + 1) + ":", wn)
main()