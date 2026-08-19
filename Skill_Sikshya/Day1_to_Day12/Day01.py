#  CONCEPT OF LOOPS IN PYTHON




fruits = ["apple","banana","ornge"]
for fruit in fruits:
  if fruit == "apple":
      print(fruit)
      
      
      
      
      i = 0
while i < 10:
  i +=1
  if i == 4:
    continue
  print(i)




a = 0
b = 1
i = 1


while i < 10:
  print (a)

  c = a + b


  a = b
  b = c
  i += 1



a = 0
b = 1



for _ in range(10):
  print (a)

  c = a + b


  a = b
  b = c
  i += 1
  
  
  
  
  a = 0
b = 1

res = []

for i in range(10):
  res.append(a)
  print(res)

  c = a + b


  a = b
  b = c
  i += 1
  
  
  
  
  
  