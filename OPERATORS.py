#operators

#Arithmetic operators
x = 10
y = 3
z = x+y
print(z)
print(type(z))
print()

x = 10
y = 3
z = x-y
print(z)
print(type(z))
print()

x = 10
y = 3
z = x*y
print(z)
print(type(z))
print()

x = 10
y = 3
z = x/y
print(z)
print(type(z))
print()

x = 10
y = 3
z = x//y
print(z)
print(type(z))
print()

x = 10
y = 3
z = x%y
print(z)
print(type(z))
print()

x = 10
y = 3
z = x**y
print(z)
print(type(z))
print()


#Assignment Operators
x = 10
x = x+1
print(x)
print()

x = 10
x += 1
print(x)
print()

x = 10
x = x-1
print(x)
print()

x = 10
x -= 1
print(x)
print()

x = 10
x = x*2
print(x)
print()

x = 10
x *= 2
print(x)
print()

x = 10
x = x/2
print(x)
print()

x = 10
x /= 2
print(x)
print()

x = 10
x = x//2
print(x)
print()

x = 10
x //= 2
print(x)
print()

x = 10
x = x%1
print(x)
print()

x = 10
x %= 1
print(x)
print()

#Comparision Operators
x = 10
y = 20
print(x==y)
print(x!=y)
print(x<y)
print(x<=y)
print(x>y)
print(x>=y)
print()

#Logical Operators

x = 10
y = 20
z = 30
print( (x>y) and (y>z) )
print(not( (x>y) and (y>z) ))
print()
print( (x>y) or (y<z) )
print(not( (x>y) or (y<z) ))
print()

#Membership Operators
s = 'python'
print('S' in s)
print('P' in s)
print('P' not in s)
print()

#Identity Operators
x = 10
y = 10
print(id(x), id(y))
print()
print(x is y)
print(x is not y)
print()

#Bitwise Operators
x = 10
y = 20
print(x & y)
print(x | y)
print(x << 2)
print(x >> 2)

#Walrus operator
print(x:=10)