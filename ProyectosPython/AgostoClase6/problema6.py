#Ejercicio 6
#Escribir un programa que pida al usuario su peso (en kg) y estatura (en
#metros), calcule el índice de masa corporal y lo almacene en una
#variable, y muestre por pantalla la frase Tu índice de masa corporal es
#<imc> donde <imc> es el índice de masa corporal calculado redondeado
#con dos decimales.

peso = float(input("Ingrese peso \n"))
estatura = float(input("Ingrese estatura \n"))


imc = peso / (estatura ** 2)


print(f"Su imc es {round(imc, 2)}")
