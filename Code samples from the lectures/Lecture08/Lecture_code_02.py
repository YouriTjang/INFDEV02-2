def combine(op,x,y):
  return op(x,y)

combine((lambda x, y: x + y), "10", "20")

# http://www.pythontutor.com/visualize.html#code=def+combine(op,x,y%29%3A%0A+return+op(x,y%29%0A%0Acombine((lambda+x,y+%3A+x+%2B+y%29,+%2210%22,+%2220%22%29%0A%0A&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&textReferences=false&py=3&rawInputLstJSON=%5B%5D&curInstr=0