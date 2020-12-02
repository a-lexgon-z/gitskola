# definierat en funktion som returnerar medelvärdet av två tal
#def medelvärde(tal1,tal2):
    # medel är en lokal variabel - syns endast i scopet av funktionen
    #medel = (tal1+tal2)/2
    #return medel

#vikt_medel = medelvärde(60,62)
#print(f"Min medelvikt är {vikt_medel}kg")

import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return x**2

# anropa funktionen med paramtern 5
print(f(5))
x = np.random(-10,10)
y = f(x)
print(x)
plt.plot(x,y)
plot.xlabel("x")
plot.ylabel("y")
plt.title("f(x) = x**2")
plt.show()