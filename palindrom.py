def palindrom(x):
    """funkcja sprawdza czy słowo x jest palindromem"""
    return x == x[::-1]
    
x = "kajak" #w tym miejscu nalezy podac sprawdzane slowo

if palindrom(x) == True:
    print("slowo" + " jest palindromem")
elif palindrom(x) == False:
    print("slowo"  + " nie jest palindromem")
