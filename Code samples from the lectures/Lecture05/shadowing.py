# Global state
x = 1

def f(z):
    return x * z

print f(10)
x = 2
print f(10)
# print z



# Shadowing
x = 1

def f(x):
    return x * 2

print f(10)
print f(20)