
#  COMPREHENSION IN PYTHON


squared = []
for i in range(1,11):
  squared.append(i ** 2)
print(squared)


squared = [i**2 for i in range(1,11) if i % 2 != 0]
squared





adjectives = [ "red", "green", "blue"]
fruits = ["apple", "banana", "orange"]

for a in adjectives:
  for b in fruits:
    print (a , b)
    
    
    
    adjectives = [ "red", "green", "blue"]
fruits = ["apple", "banana", "orange"]

pair = [(a,b) for a in adjectives for b in fruits]
pair





squared = {i : i**2 for i in range(1,11) if i % 2 != 0}
squared



sent = "A single training set that has already been processed is usually split into several types of datasets in machine learning which is needed to check how well the training of the model went"
res = {}
for word in sent.split():
  if len(word) > 4:
    print(word)
    
    
    
    
    sent = "A single training set that has already been processed is usually split into several types of datasets in machine learning which is needed to check how well the training of the model went"
res = {}
for word in sent.split():
  if len(word) > 4:
   res[word] = len(word)
   
   
   
   
   
   sent = "A single training set that has already been processed is usually split into several types of datasets in machine learning which is needed to check how well the training of the model went"
res = {word : len(word) for word in sent.split() if len(word) > 4}
print(res)




chars = ["c", "a", "b"]
pairs = { char1 + char2 for char1 in chars for char2 in chars}
pairs




raw_data = ['150', 'invallid','80','204','999','STOP','300','450']
# filter data , str remove


#listcomprehension , with if condition
numbers= [int(num) for num in raw_data if num.isdigit() and int(num)<=999 and int(num)>100]
print(numbers)





