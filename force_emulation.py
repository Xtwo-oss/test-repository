from time import sleep as slp
while True:
    v = 0
    g = float(input("enter g:"))
    p = float(input("enter p:"))
    cd = 1.0
    h = float(input("enter your height:"))
    w = float(input("enter your width:"))
    S = h*w*0.8
    m = float(input("enter your mass:"))
    t = 0.01
    k = (p*cd*S)/(2*m)
    for tm in range(int(input("enter time:"))*100):
        a = g-k*v**2
        if a < 0:
            a = 0
        v += a * t
        print(f"velocity: {v:0<20}, time: {(tm+1)/100:0<5}")
        slp(0.01)
    print("[program end]")