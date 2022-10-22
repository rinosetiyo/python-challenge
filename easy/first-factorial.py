def FirstFactorial(num):
  calc = 1
  for i in range(1,num + 1):
    calc *= i
  return calc
  # code goes here
  return num

# keep this function call here 
print(FirstFactorial(int(input())))
