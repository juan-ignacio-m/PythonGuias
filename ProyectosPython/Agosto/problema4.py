#PROBLEMA 4
#Problemas condicionales con If anidados
######################################################################
#Desarrollar una app para chile, preguntarle al usuario su edad y cuanto gana, informa si tributa o no, tributaria si es mayor de 18 o gana mas de 1000 EU


edad = int(input("Ingrese su edad \n"))
if  (edad > 121 or edad < 1 ) :
    print("Error de edad")
else : 
    salario = float(input("Ingrese cuanto gana \n"))
    if  (salario > 1000000 or salario < 1)  :
        print("Error de salario")
    else:
        if edad >= 16 or salario >=1000 :
            print("ud tributa")
        else :
            print("ud no tributa")
