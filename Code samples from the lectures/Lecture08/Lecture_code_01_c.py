def combine(op,x,y):
  return op(x,y)

def plus(x,y): return x + y
def times(x,y): return x * y
def minus(x,y): return x - y
  
print(combine(plus, "10", "20"))
print(combine(times, 10, 20))
print(combine(minus, 10, 20))



#http://www.pythontutor.com/visualize.html#code=def+combine(op,x,y%29%3A%0A++return+op(x,y%29%0A%0Adef+plus(x,y%29%3A+return+x+%2B+y%0A%0Aprint(combine(plus,+%2210%22,+%2220%22%29%29%0A&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&textReferences=false&py=3&rawInputLstJSON=%5B%5D&curInstr=0