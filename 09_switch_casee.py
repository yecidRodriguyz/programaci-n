#switch case
import math as ma
nlad=int(input("Seleccione el numero de lados: "))
lad=int(input("Ingrese la medida de los lados: "))
#Error checking
per=lad*nlad
vert=((2*ma.pi)/nlad)/2
ap=(lad/2)/ma.tan(vert)
if nlad<3:
    area=ma.pi*(lad**2)
    print ("Error, lados indefinidos: ",area)
if nlad>7:
    area=ma.pi*(lad**2)
    print ("Error, lados indefinidos: ",area)
if nlad==3:
   area=(per*ap)/2
   print ("Triangulo: ",area)
else:
    if nlad==4:
      area=lad*lad
      print("Cuadrado: ",area)
    else:
        if nlad==5:
            area=(per*ap)/2
            print("Pentagono: ",area)
        else:
            if nlad==6:
                area=(per*ap)/2
                print("Hexagono: ",area)
            else:
                if nlad==7:
                    area=(per*ap)/2
                    print ("Heptagono: ",area)