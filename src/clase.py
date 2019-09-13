print ('hola mundo')
a,b,c='Hola','mundo',2019
print(a)
print(b)
print(c)

t_registro=('juan','Perez',2000)
nombre,apellido,anio=t_registro
print(nombre)
print(apellido)
print(anio)

#a=7
#b=6
#if a>b:
#    print(a,"es mayor que",b)
#elif a!=b:
#    print("Son distintos")
#else:
#    print(b,"es mayor que ", a)

#a=0 
#while a<10:
#    print("numero ->",a)
#    a+=1

# =============
#while True:
#    nombre = input("indique su nombre")
#    if nombre:
#        break

#mi_lista=['juan','Antonio','Pedro','Hermino']
#for nombre in mi_lista:
#    print(nombre)

#mi_tupla=('rosa','verde','celeste','amarillo')
#for color in mi_tupla:
#    print (color)

#for anio in range(2001,2021):
#    print ("informes del año",str(anio))

#c=0
#while c<=5:
#    c+=1
#    print("c vale",c)
#else:
#   print("se ha completado toda la iteracion y c vale",c)

#indice =0
#numeros=[1,2,3,4,5,6,7,8,9,10]
#for numero in numeros:
#    numeros[indice] *=10
#    indice+=1
#    print(numeros)

#cadena ="hola mundo"
#for caracter in cadena:
#    print(cadena)


#====

#print("Bienvenido al menu interactivo")
#while(True):

#def soyunafuncion():
#    print("hola mundo")

#soyunafuncion()

#def funcion(arg):
#    print("hola",arg)

#funcion(rodri)

def suma(a,b):
    return a+b

#s=suma(30,10)
#print("suma=",s)

#s=suma(b=30,a=10)
#print(s)

def suma(a=None,b=None):
    if a==None or b==None:
        print("Error, algun numero esta vacio")
        return
    return a+b
s=suma()
print(s)

#=====
def indeterminados_posicion(*args):
    for arg in args:
        print(arg)

indeterminados_posicion(1,"ABC",[0,1,2,3,4,5])

def funcion_nombre(**kwargs):
    for kwarg in kwargs:
        print(kwarg,"=>",kwargs[kwarg])

funcion_nombre(n=5,c="ABC",l=[1,2,3,4,5])

