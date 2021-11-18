#import time 
import matplotlib.pyplot as plt
name = input("Nombre del archivo con los valores del ping: ")
Vect = []
tiempo = []
i=1
with open("C:/Users/nicol/OneDrive/Escritorio/" + name + ".txt") as ping:
    for line in ping:
        """ print(line)
        print(type(line)) """
        #time.sleep(1)
        
        if line.startswith("Respuesta desde"): #i > 2 and not line.startswith("Tiempo de espera agotado para esta solicitud.") and line != " ":
            tiempo.append(i)
            si = line.find("tiempo")
            so = line.find("m",si+7)
            """ print(si,so)
            print(line[si+7:so])
            print(type(line[si+7:so])) """
            Vect.append(int(line[si+7:so]))
            i = i+1
    print(tiempo)
    print(Vect)

prom = sum(Vect)/len(Vect)
max = max(Vect)
min = min(Vect)
print("promedio: ",prom,"ms \n", "Máximo: ",max,"ms \n", "Mínimo: ",min,"ms")
plt.plot(tiempo,Vect)
plt.show()