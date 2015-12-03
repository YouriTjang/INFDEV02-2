# Global state
x = 1

def f(z):
    return x * z

print (f(10))
x = 2
print(f(10))
# print( z)



# Shadowing
x = 1

def f(x): #the local variable x wil be used here. Not the global
    return x * 2

print(f(10))
print(f(20))