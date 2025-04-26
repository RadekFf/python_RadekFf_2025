def f_rekurencja_ogonowa (n, fn=0, fn_1=1):
    if n == 0:
        return fn_2
    elif n == 1:
        return fn_1
    else:
        return f_rekurencja_ogonowa(n, n-1, fn_1, fn_2 + fn_1)

if __name__ == '__main__':
    print(f_rekurencja_ogonowa(50))
