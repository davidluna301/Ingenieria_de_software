area1 = 0
area2 = 0
areatotal = 0

a = float (input ("Digite la dimension A del terreno: "))
b = float (input ("Digite la dimension B del terreno: "))
c = float (input ("Digite la dimension C del terreno: "))

area1 = b*c
area2 = (b*(a-c))/2
areatotal = area1 + area2

print ("El area del terreno es ", areatotal)