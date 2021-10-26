from timeit import default_timer as timer

A1 = 25678071166819355351
B1 = 13611196686033047009
A2 = 621127170412659657225870005149089549077
B2 = 315056110669131796109059079047081051609
A3 = 45292121605016577498108705242535303583912829952949883371582182972621837244782259
B3 = 16080345684623974690115441179815095911555808759264399497696889450720618482304401


def extended_euclidean_algorithm(a, b):
    if a < b:
        a, b = b, a
    Xchar = 'x'
    xi_1 = 1
    x_i = 0
    Ychar = 'y'
    yi_1 = 0
    y_i = 1
    Rchar = 'r'
    ri_1 = a
    r_i = b
    Ichar = 'i'
    Qchar = 'q'
    i = 0
    tmp_r, tmp_x, tmp_y = 1, 1, 1
    print("\n\tРасширенный алгоритм Евклида")

    print("% 3c" % Ichar, "% 25c" % Rchar, "% 25c" % Xchar, "% 25c" % Ychar, "% 25c" % Qchar)
    print("% 3d" % i, "% 25d" % ri_1, "% 25d" % x_i, "% 25d" % y_i)

    while not tmp_r == 0:
        i = i + 1
        q = int(ri_1 / r_i)
        tmp_r = ri_1 % r_i
        print("% 3d" % i, "% 25d" % ri_1, "% 25d" % x_i, "% 25d" % y_i, "% 25d" % q)
        if tmp_r == 0:
            break
        tmp_x = xi_1 - q * x_i
        tmp_y = yi_1 - q * y_i
        xi_1 = x_i
        x_i = tmp_x
        yi_1 = y_i
        y_i = tmp_y
        ri_1 = r_i
        r_i = tmp_r
    print("НОД = ", r_i)
    print("Первый коэффициент: ", x_i)
    print("Второй коэффициент: ", y_i)
    return


start = timer()
extended_euclidean_algorithm(A1, B1)
print("Время: {:g} secs".format(timer() - start))


def extended_binary_euclidean_algorithm(a, b):
    Ichar = 'i'
    Uchar = 'u'
    Vchar = 'v'
    Achar = 'A'
    Bchar = 'B'
    Cchar = 'C'
    Dchar = 'D'
    g = 1
    u = a
    v = b
    A = 1
    B = 0
    C = 0
    D = 1
    i = 0
    while a % 2 == 0 & b % 2 == 0:
        a = a // 2
        b = b // 2
        g = g * 2
    print("\n\tРасширенный бинарный алгоритм Евклида")
    print("% 3c" % Ichar, "% 42c" % Uchar, "% 42c" % Vchar, "%42c" % Achar, "% 42c" % Bchar, "% 42c" % Cchar,
          "% 42c" % Dchar)
    while u != 0:
        print("% 3d" % i, "% 42d" % u, "% 42d" % v, "% 42d" % A, "% 42d" % B, "% 42d" % C, "% 42d" % D)
        i += 1
        while u % 2 == 0:
            u = u // 2
            if A % 2 == 0 and B % 2 == 0:
                A = A // 2
                B = B // 2
            else:
                A = (A + b) // 2
                B = (B - a) // 2
        while v % 2 == 0:
            v = v // 2
            if C % 2 == 0 and D % 2 == 0:
                C = C // 2
                D = D // 2
            else:
                C = (C + b) // 2
                D = (D - a) // 2
        if u >= v:
            u = u - v
            A = A - C
            B = B - D
        else:
            v = v - u
            C = C - A
            D = D - B
    d = g * v
    x = C
    y = D
    print("НОД = ", int(d))
    print("Первый коэффициент = ", int(x))
    print("Второй коэффициент = ", int(y))
    return


start = timer()
extended_binary_euclidean_algorithm(A2, B2)
print("Время: {:g} secs".format(timer() - start))


def extended_euclidean_algorithm_with_us(a, b):
    if a < b:
        a, b = b, a
    Xchar = 'x'
    xi_1 = 1
    x_i = 0
    Ychar = 'y'
    yi_1 = 0
    y_i = 1
    Rchar = 'r'
    ri_1 = a
    r_i = b
    Ichar = 'i'
    Qchar = 'q'
    i = 0
    tmp_r, tmp_x, tmp_y = 1, 1, 1
    print("\n\tРасширенный бинарный алгоритм Евклида с усечёнными остатками")
    print("% 3c" % Ichar, "% 85c" % Rchar, "% 42c" % Xchar, "% 42c" % Ychar, "% 10c" % Qchar)
    print("% 3d" % i, "% 85d" % ri_1, "% 42d" % x_i, "% 42d" % y_i)
    while 0 != tmp_r:
        i += 1
        q = int(ri_1 / r_i)
        tmp_r = ri_1 % r_i
        print("% 3d" % i, "% 85d" % ri_1, "% 42d" % x_i, "% 42d" % y_i, "% 10d" % q)
        if tmp_r == 0:
            break
        tmp_x = xi_1 - q * x_i
        tmp_y = yi_1 - q * y_i
        xi_1 = x_i
        yi_1 = y_i
        x_i = tmp_x
        y_i = tmp_y
        if tmp_r >= (r_i / 2):
            tmp_r = r_i - tmp_r
            x_i = xi_1 - x_i
            y_i = yi_1 - y_i
        ri_1 = r_i
        r_i = tmp_r
    print("НОД = ", r_i)
    print("Первый коэффициент: ", x_i)
    print("Второй коэффициент: ", y_i)
    return


start = timer()
extended_euclidean_algorithm_with_us(A3, B3)
print("Время: {:g} secs".format(timer() - start))
