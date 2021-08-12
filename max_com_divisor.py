
#ingereso de frecuencias y coeficientes de x(t)

frecs = [50, 100, 150]  #frecuencias de menor a mayor
coeficientes = [3, -4, 0.7] #coeficientes según frecuencias correspondientes


def encontrar_mcd(x,y):
    """Esta función sirve para encontrar el máximo común divisor """
    while(y):
        x,y = y, x%y
    return x
num1 = frecs[0]
num2 = frecs[1]
mcd = encontrar_mcd(num1, num2)

for i in range(2, len(frecs)):
    mcd = encontrar_mcd(mcd, frecs[i])
frecuencia = mcd

print("f = %d Hz"%(frecuencia))

#Ahora vamos a determinar el tipo de armónica
armonicas = [k/frecuencia for k in frecs]
for i in range(len(frecs)):
    print ('%5d, %d' %(frecs[i], armonicas[i]))