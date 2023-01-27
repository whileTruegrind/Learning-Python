# Variable Scope = Where a variable is visible and accessible
# Scope Resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

import math

d = 0

def fn1():
    a = 1
    print(a)             # Local to fn1
def fn2():
    b = 2
    print(b)             # Local to fn2
    def fn3():
        c = 2
        print(c)         # Enclosed
        print(d)         # Global
        print(math.e)    # Built-in
    fn3()

fn1()
fn2()