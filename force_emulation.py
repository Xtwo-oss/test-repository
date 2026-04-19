from time import sleep as slp
while True:
    v = 0
    g = float(input("enter g:")) #0 for standart
    if g == 0:
        g = 9.8
    p = float(input("enter p:")) #0 for standart
    if p == 0:
        p = 1.225
    cd = 1.0
    h = float(input("enter height:")) #like 1.23 (123 cm)
    w = float(input("enter width:")) #like 1.23 (123 cm)
    a = int(input("is this a body?(0/1):"))
    if a == 1:
        S = h*w*0.8
    elif a == 0:
        S = h*w
    m = float(input("enter mass:")) #like 123 (123 kg)
    t = 0.01
    k = (p*cd*S)/(2*m)
    for tm in range(int(input("enter time:"))*100):
        a = g-k*v**2
        if a < 0:
            a = 0
        v += a * t
        print(f"velocity: {v:0<18}mps, time: {(tm+1)/100:0<5}")
        slp(0.01)
    print("[program end]")