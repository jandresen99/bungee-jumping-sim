
h = 1.0
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

def get_new_data():
    u = []
    v = []
    w = []
    total_cases = []
    k = 0.0
    u0 = n
    v0 = 120.0
    w0 = 0.0
    u.append(u0)
    v.append(v0)
    w.append(w0)
    un = u1(u0, v0)
    vn = v1(u0, v0)
    wn = w1(u0, v0, w0)
    u.append(un)
    v.append(vn)
    w.append(wn)
    total_cases.append(vn + wn)
    while k < 62:
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
        total_cases.append(vn+wn)

    return u, v, w,total_cases

def read_data():
    file1 = open('casos.txt', 'r')
    Lines = file1.readlines()
    data = []

    for line in Lines:
        data.append(int(line.strip()))
    return data

def get_gamma_values():
    value = 0.03
    values = []
    while value <= 0.14:
        value += 0.01
        values.append(value)
    return values

def get_sigma_values():
    value = 1
    values = []
    while value <= 20:
        value += 0.10
        values.append(value)
    return values

def main():
    errors = []
    global y
    global beta
    ys = get_gamma_values()
    sigmas = get_sigma_values()

    vs = []
    ws = []
    total_casesDict = {}

    print("Calculando...")

    for sigma in sigmas:
        for gamma in ys:
            beta = sigma*gamma
            y = gamma
            try:
                u, v, w, total_cases = get_new_data()
                vs.append(v)
                ws.append(w)
                total_casesDict["beta:" + str(beta) + " y:"+ str(y)] = total_cases
            except:
                print("Error")

    real_total_cases = read_data()
    total_errorsDict = {}

    for key in total_casesDict:
        error = 0
        for i in range(len(real_total_cases)):
            error += (abs(total_casesDict[key][i] - real_total_cases[i]))
        errors.append(error)
        total_errorsDict[key] = error

    min_error = min(errors)

    print("Comparando...")

    for key in total_errorsDict:
        if total_errorsDict[key] == min_error:
            print("Valores:", key)
            return

main()