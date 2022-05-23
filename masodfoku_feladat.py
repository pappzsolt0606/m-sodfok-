''' 1. Másodfokú egyenlet megoldása.
1. Készíts egy függvényt masodfoku(a, b, c) néven.
A függvény bemenő paraméterei az " a*x**2 + b*x + c = 0 "  egyenlet alaján a, b, c
A függvény None értékkel térjen vissza, ha az egyenletnek nincs megoldása a valós számok körében.
A függvény egy számmal térjen vissza, ha a két megoldás egybeesik.
A függvény egy tuple-be "csomagolva" adja vissza x1 és x2 értékét a valós számok körében.
''' 

def masodfoku(a, b, c):
    d = b**2 - 4 * a * c 
    if d < 0:
        return None
    if d == 0:
        x = (-b + d**(0.5)) /(2*a)
        return x
    elif d > 0:
        x1 = (-b + d**(0.5)) /(2*a)
        x2 = (-b - d**(0.5)) /(2*a)
        return x1 , x2
    
    



print(masodfoku(2, -12, 10))
