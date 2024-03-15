try:
  import os
  import random
except:
  print("Error import module's")

rnum = random.randint(1, 100)
boolean = 1

while boolean < 10:
  boolq = boolean+1
  boolean = boolq + 1 
  print(f"Result: {rnum}")  
  