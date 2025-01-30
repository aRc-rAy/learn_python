myMap=dict()

myMap[0]=['apple','ant']
myMap[1]=['ball','bat']

myMap[0].append('apple')

for key,value in myMap.items():
      print(f"Key is : {key}  |  Value is : {value}")