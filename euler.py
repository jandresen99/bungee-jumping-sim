import os
import pandas as pd

NP = 103958
g = 9.81
L0 = 43.437
m = 65.832
k1 = 43.958


#L0 = (((0.1/10000) * (NP - 100000)) + 0.25) * 150
#m = (40/10000) * (NP - 100000) + 50
#k1 = (10/10000) * (NP - 100000) + 40


def write_to_excel(rows):
    new_sheet = {}
    for i in range(len(rows[0])):
        column_name = rows[0][i]
        data = []
        for row in rows:
            data.append(row[i])

        new_sheet[column_name] = data

    new_df = pd.DataFrame(new_sheet)
    new_df = new_df.iloc[1:, :]

    filename = 'datos.xlsx'
    desktop = os.path.join(os.path.expanduser("~"), "Downloads")
    filePath = os.path.join(desktop, filename)
    writer = pd.ExcelWriter(filePath, engine='xlsxwriter')

    new_df.to_excel(writer)

    writer.save()


def u_n1(un, vn, h):
    un1 = un + (h * vn)
    return un1


def v_n1(un, vn, h):
    if un >= L0:
        vn1 = vn + (h * (g - ((k1 * (un - L0))/m)))
    else:
        vn1 = vn + (h * g)

    return vn1


def w_n1(un):
    if un >= L0:
        wn1 = (g - ((k1 * (un - L0))/m))
    else:
        wn1 = g

    return wn1


def main():
    rows = [["N", "h", "un", "vn", "wn"]]
    un = 0
    vn = 0
    wn = 0

    h = 0.1
    i = 1000
    n = 0

    y_lim = 0
    a_lim = 0

    rows.append([n, h, un, vn, wn])
    print("n:", n, "| un:", un, "| vn:", vn, "| wn:", wn)

    while n < i:
        n += 1

        un1 = u_n1(un, vn, h)
        vn1 = v_n1(un1, vn, h)
        wn1 = w_n1(un)

        un = un1
        vn = vn1
        wn = wn1

        if un > y_lim:
            y_lim = un
            a_lim = wn

        rows.append([n, h, un, vn, wn])

        print("n:", n, "| un:", un, "| vn:", vn, "| wn:", wn)

    print("Y lim:", y_lim, "| A lim:", a_lim)

    write_to_excel(rows)


main()