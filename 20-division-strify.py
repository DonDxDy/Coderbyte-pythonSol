import math
def DivisionStringified(num1,num2): 
  return "{:,}".format(int(math.ceil(float(num1)/num2)))
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print DivisionStringified(raw_input())  





