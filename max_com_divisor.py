
#ingereso de frecuencias y coeficientes de x(t)

frecs = [25,50, 100, 150,200]  #frecuencias de menor a mayor
coeficientes = [2,3, -4, 0.7,7] #coeficientes según frecuencias correspondientes


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

print("f = %d Hz"%(frecuencia)+"\n")


#Ahora vamos a determinar el tipo de armónica
armonicas = [k/frecuencia for k in frecs]
for i in range(len(frecs)):
    print ('%5d, %d' %(frecs[i], armonicas[i]))

print("")

#obtener los resultados en una tabla incluyendo el periodo

print('Amplitud  frecuencia Hz  periodo seg  armónica')
amplitudes = [abs(k) for k in coeficientes]
periodos = [1./k for k in frecs]
for i in range(len(frecs)):
    print('%5.1f %12d %14.3f %7d' %(amplitudes[i], frecs[i], periodos[i], armonicas[i]))
print("")