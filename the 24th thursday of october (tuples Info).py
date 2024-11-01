#mcblah blah blah
#Tuples give the option to list what is inside the brackets to then be written, it can be listed out,
#have Parts replaced, look through it to then print in something, and Add then together
# it lets you store mutliple items in one variable

thistuple = ("War", "Peststilene","Famine","Death","Pollution","Taxes","Corruption")
if 'Taxes' in thistuple:
    print("Taxes are the Worst of them All")

x = ("Reist", "Rise", "Reorder")
y = list(x)
y[1] = "and"
x = tuple(y)
print(x) 

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

Tuplemax = ("War", "Famine", "Pestenstilance")
y = ("Death",)
Tuplemax += y
print(Tuplemax)

#thistuple = ("Disorder", "Corupption", "Taxes")
#y = list(thistuple)
#y.remove("Taxes")
#thistuple = tuple(y)

#print(thistuple)

#fruits = ("apple", "banana", "cherry")
#(green, yellow, red) = fruits
#print(green)
#print(yellow)
#print(red)



#Horsemen = ("Famine", "Pestilence", "War", "Death", "Taxes", "41")
#(Tarn, Helex, *Vos ) = Horsemen 
#print(Tarn)
#print(Helex)
#print(Vos)

#thistuple = ("apple", "banana", "cherry")
#for x in thistuple:
#  print(x)

#thistuple = ("Cider", "Vodka", "Gin")
#for i in range(len(thistuple)):
#  print(thistuple[i]) 


#thistuple = ("Rum", "Scotch", "Whiskey")
#i = 0
#while i < len(thistuple):
#  print(thistuple[i])
#  i = i + 1 

#tuple1 = ("a", "b" , "c")
#tuple2 = (1, 2, 3)

#tuple3 = tuple1 + tuple2
#print(tuple3) 


#fruits = ("Parkvile", "Anzac", "Arden")
#mytuple = fruits * 2

#print(mytuple) 


Triad = ("Tokyo", "Osaka", "Hiroshima", "Nagasaki", "Kyoto")
if 'Nagasaki' in Triad:
    print("Peace Park")
(Famine, Death, *war, Pollution) = Triad
Trinity = list(Triad)
Trinity[3] = "Sendai"  
Triad = tuple(Trinity)
print(Triad)
print(Famine)
print(Death)
print(war)
print(Pollution)

