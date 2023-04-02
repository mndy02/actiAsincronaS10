#Inicio del programa
print("¡BIENVENIDO AL PROGRAMA!\n")

#Definir variables
totalCompras = 0
numCompras = int(input("Ingrese la cantidad de compras: ")) 
contadorCom = 0

#Bucle While para el ingreso de compras
while contadorCom < numCompras:
    #Pedir al usuario que ingrese el monto de la compra
    montoCompra = float(input("Ingrese el monto de la compra N° " + str(contadorCom + 1) + ": $"))
    #Agregar el monto al total
    totalCompras += montoCompra
    #Aumentar 1 al contador
    contadorCom += 1
    
print("\nEL TOTAL A PAGAR ES DE: $", totalCompras)

#Aplicación de descuentos al total de compras
if totalCompras > 500 and totalCompras <= 1000:
        descuento = totalCompras * 0.05        
elif totalCompras > 1000:
        descuento = totalCompras * 0.1         
else:
        descuento = 0

totalDesc = totalCompras - descuento 
        
#Mostrar el total a pagar
if descuento > 0:
    print("\nAplica para un descuento del " + str(descuento/totalCompras*100) + "% , $" +  str(descuento.__round__(2)))
print("\nEL TOTAL A PAGAR CON DESCUENTO ES DE: $", totalDesc.__round__(2))

print("\nFIN DEL PROGRAMA")