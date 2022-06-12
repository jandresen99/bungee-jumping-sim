import numpy as np

def get_hs():
    h = [0.4, 0.2, 0.1]
    return h

def y(t):
    yt = (2*np.exp(-t))+(t**2)-2
    return np.float32(yt)

def yp(y, t):
    yp = (-y) + (t**2) + (2*t) -2
    return np.float32(yp)

def euler(uo, n, h):
    u = uo + (h*yp(uo,n*h))
    return np.float32(u)

def main():
    h = get_hs()
    for i in range(len(h)):
        u = 0
        n = 0
        while n < 11:
            u = euler(u, n, h[i])
            print("h: "+str(h[i]), "n: "+ str(n+1),"t(n): "+str(n*h[i]),"u" + str(n+1) + ": " + str(u))
            n += 1

main()