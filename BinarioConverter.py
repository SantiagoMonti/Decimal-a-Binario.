def binario(d):
    b=""
    for i in range (0,8):
        d=d/2
        if d==int(d):
            b+="0"
        else:
            b+="1"
            d-=0.5
    b=b[len(b)::-1]
    return b
print(">>> |CONVERTIDOR DECIMAL - BINARIO | <<<")
d=0
while d!=257:
    print("Ingrese -SALIR- para cerrar.")
    d=int(input("Ingrese un número decimal... "))
    if d!=257:
        print(f"{d} en binario es: {binario(d)}")
        print(" ")