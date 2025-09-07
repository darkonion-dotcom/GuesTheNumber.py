#Este es el codigo de un programa que adivina el numero que el usuario piensa
import random
print("Piensa un numero del 1 al 10 y no me lo digas")
respuesta=input("Ya lo tienes? (y/n): ").lower()
if respuesta=='y':
    operacion=random.choice(["Ahora súmale","Ahora réstale"])
    numero=random.randint(1,20)
    print(f"{operacion} {numero} a tu número.")
    input("¿Listo? (Enter)")
    if operacion=="Ahora súmale":
        NumAdivinar=numero
s
        
    operacion=random.choice(["Ahora súmale","Ahora réstale"])
    numero=random.randint(1,20)
    print(f"{operacion} {numero} a tu número.")
    input("¿Listo? (Enter)")
    if operacion=="Ahora súmale":
        NumAdivinar+=numero
    else:
        NumAdivinar-=numero
    operacion=random.choice(["Ahora súmale","Ahora réstale"])
    numero=random.randint(1,20)
    print(f"{operacion} {numero} a tu número.")
    input("¿Listo? (Enter)")
    if operacion=="Ahora súmale":
        NumAdivinar+=numero
    else:
        NumAdivinar-=numero
        
    print("Ahora restale el numero que pensaste al principio")
    input("¿Listo? (Enter)")
    print(f"Tu número es {NumAdivinar}")
r=input("Correcto? (y/n): ")
if r=="y":
 print("¡Genial! ¡soy un genio!")
else:
 print("Beep Boop error 404...vaya mi creador debio programarme mal")
         
    