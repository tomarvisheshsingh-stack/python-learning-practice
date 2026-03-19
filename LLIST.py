
#list
l = [10, 20, 'python', 10.25]
print(l)
print(type(l))
print()

#Tuple
s = (10, 25, 'python', 55555.2) 
print(s)
print(type(s))
print()

#Dictionary
d = {'name' : 'Vishesh',
	'age' : 21,
	'quali' : 'nothing'}
print(d)
print(type(d))

print()

d = {'name' : [10, 25, 35],
	'age' : (111, 52, 'python'),
	'quali' : {'x' : 10, 'b': 25}
}
print(d)
print()

#Set
s = {10, 20, 'python', 10, 'java', 'python'}
print(s)
print(type(s))
print()

#Frozenset
s = [10, 20, 'python', 'java', 20, 'python']
print(s)
fs = frozenset(s)
print(fs)
print(type(fs))
print()

#Boolean
x = True
print(x)
print(type(x))
print()

#None
x = None
print(x)
print(type(x))