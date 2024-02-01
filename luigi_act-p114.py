#QUESTION 1

def f(h) : 
  return - h**3 + 6.3*h**2 -25.93

import matplotlib.pyplot as plt

liste_x = []
liste_y = []

x = 0
while x < 4.2 : 
  liste_x.append(x)
  liste_y.append(f(x))
  x = x + 0.05
print(liste_x[-1])
plt.plot(liste_x,liste_y)
plt.grid()
plt.show()

x = 0
while x < 4.2 : 
  liste_x.append(x)
  liste_y.append(f(x))
  x = x + 0.05

#QUESTION 2 
import bisect 
id = bisect.bisect_left([f(0.01*i) for i in range(0,int(4.2/.01)+1)],0)
print(f"L'indice de la première valeur positive du tableau est {id} donc h0 vaut à peu près {0.01*id}")

#QUESTION 3
def bisection(f, a, b, eps): 
  nb_iterations = 0
  while True:
    nb_iterations += 1
    print(f'a:{a}, b:{b}, nb iterations:{nb_iterations}')
    mid = (a+b)/2
    if abs(f(mid))<eps:
      return mid
    elif f(mid)*f(b)>0: # mid et b de meme signe
      b = mid
    else: # mid et a de meme signe
      a = mid
#QUESTION 5 
def rac(x): # assert(x>0)
  def smaller_sq(k):
    return k*k - x
  return bisection(smaller_sq,0,max(1,x),0.0001)


#QUESTION 8
x = int(input("Entrez un nombre entier positif pour le code de la question 8 : "))

def w(y):
  """ fonction mystere """
  if y>x:
    return True
  elif y<x:
    return False
  else:
    return 4
def g(z):
  """ transforme le resultat de w d'une facon exploitable tel quel par bisection """
  y = w(z)
  if y==True:
    return 1
  elif y==False:
    return -1
  else:
    return 0
round(bisection(g,0,10**8,.25)) #2021

#QUESTION 9
from math import floor
def recherche_dicho(t, val):
  """ Ramene la recherche dichotomique a un probleme de bisection """
  a = 0
  b = len(t)-1
  def f(x):
    return t[floor(x)] - val
  i = round(bisection(f,a,b,2))
  for j in range(max(0,i-1),min(len(t),i+2)):
    if t[j] == val:
      return j
  return -1
recherche_dicho([2,4,5,7,9],3)