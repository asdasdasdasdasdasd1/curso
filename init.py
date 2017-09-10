from models.clientes import Cliente

cliente = Cliente('asd','asd',edad='18')
cliente.edad = '12'
#print(cliente.edad)
#print(cliente.nombres)

#Metodo global int
a = '1'
b = int(a)
c = 21
d = str(c)
e = range(0,9)
f = list(e)
g = [3,1,45,1,6,7]
h = sorted(g)
j = list(map(str,h))
i = sum(g)
m = round(i)
print (j)
print (m)

#tupla se declara con parentesis por convención
a = 5
b = 4
c = None
d = 4
if b == d:
    print("Son iguales")
if c is None:
    print("Es nulo")
else:
    print("bla guc")


a = range(0,10)
for i in a:
    print (i)
