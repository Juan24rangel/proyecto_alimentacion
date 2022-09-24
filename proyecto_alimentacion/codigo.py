# lista de aliemtos 

print("----------------------")
print("--- alimentacion------")
print("----------------------")


#input 

#opcion

print("seleccione la opcion que desea ver:")
print("1. desayuno")
print("2. almuerzo")
print("3. comida")

opcion=int(input("digite que recetas desea ver:"))

#Desayunos
print("1. omelet con queso y hierbas")
print("2. Panquecas de platano")
print("3. batido de papaya y piña")

c=int(input("escoge la receta:"))

#processing
if(opcion==1):
    if (c==1):
        print("\n1.-Omelet con queso y hierbas- \nIngredientes: \n3 huevos batidos, 1 cucharada de hierbas de olor, 1 cucharada de mantequilla sin sal, 50 gramos de queso .\nModo de preparar: se mezcla todos los ingredientes excepto la mantequilla y el queso.calienta la mantequilla en un sartén y cuando esté caliente agrega la mezcla.Espera hasta que se forme el omelet, entonces coloca el queso encima y dobla por la mitad, se cocina por un minuto hasta que se derrita el quesoDisfruta.")
    elif(c==2):
        print("\n2.-Panquecas de plátano- \nIngredientes: \nTres plátanos hechos puré,100 gramos de mantequilla, 1 cucharada de miel.\nPreparación: forma las panquecas con el puré de plátano.Una vez formadas, fríelas en la mantequilla una por una, por alrededor de dos minutos.acompaña con miel y disfruta.")
    elif(c==3):
        c=print("\n3.--Batido de papaya y piña-- \nIngredientes : \n1 taza, (225 gramos) de piña en trozos,media taza (120 gramos) de papaya en trozos, media taza (125 ml) de cubos de hielo,60 ml de miel.\nPreparación: Vierte todos los ingredientes en la licuadora y licúa hasta que se mezclen.Sirve inmediatamente.")

