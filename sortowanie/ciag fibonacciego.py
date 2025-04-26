def f_rekurecyjny(n):
    return f_rekurecyjny(n-1) + f_rekurecyjny(n-2)
def f_rekuracyjny(n):
    if n<2:
        return n
   fn_1 = 1
   fn_2 = 0
for _ in range (2, n+1):
    fn = fn_1 + fn_2
    fn_2 = fn_1
    fn_1 = fn
return fn
fn_2, fn_1 = fn_1, fn_2 + fn_1
return fn_1

if __name__ == '__main__':
print (f_iteracyjny(40)
