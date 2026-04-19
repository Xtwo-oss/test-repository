from time import sleep as slp
while True:
    v = 0
    g = float(input("Enter the acceleration due to gravity (0 for the default value):"))
    if g == 0:
        g = 9.8
    p = float(input("Enter air/atmosphere density (0 for default value):"))
    if p == 0:
        p = 1.225
    cd = 1.0
    h = float(input("Enter the height (or length) of the object (the higher the height, the slower the object):")) #like 1.23 (123 cm)
    w = float(input("Enter the width of the object (the higher the width, the slower the object):")) #like 1.23 (123 cm)
    a = float(input("Enter the object's streamlining (the lower the object's roundness, the rounder it is):"))
    S = h*w*a
    m = float(input("Enter the weight of the object (the higher the weight, the faster the object):")) #like 123 (123 kg)
    t = 0.01
    k = (p*cd*S)/(2*m)
    for tm in range(int(input("enter time:"))*100):
        a = g-k*v**2
        if a < 0:
            a = 0
        v += a * t
        if (tm+1)//100 == (tm+1)/100:
            print(f"velocity: {v:0<20}mps, time: {(tm+1)/100:0<5}")
    print("[program end]")