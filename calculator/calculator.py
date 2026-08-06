ADDITION = 1
SUBTRACTION = 2
MULTIPLICATION = 3
DIVISION = 4
MODULUS = 5

def start():
  print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus")


def operation():
  while True:
    op = int(input("Select Operation:"))
    if op < 1 or op > 5:
      print("Wrong Operation")
    else:
      break
  
  return op


def get_vals():
  x = float(input("Enter Number:"))
  y = float(input("Enter Number:"))
  return x, y

def calculator(op,x,y):
  if op == 1:
    add = x+y
    return add
    
  elif op == 2:
    sub = x-y
    return sub
    
  elif op == 3:
    mult = x*y
    return mult
    
  elif op == 4:
    div = x/y
    return div
    
  elif op == 5:
    mod = x%y
    return mod

def main():
  start()
  op = operation()
  x,y = get_vals()
  ans = calculator(op,x,y)
  print("Answer:",ans)
 
 
main()
 
 


