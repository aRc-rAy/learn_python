import time

def generate_numbers(start,end):
      while start<=end:
            print(f"produced : {start}")
            yield start
            start+=1
            time.sleep(4)
            
      
gen=generate_numbers(1,5)
print(f"gen is : {gen}")

for value in gen:
      print(f"consumed : {value}")
      time.sleep(3)

def generate_numbers():
    yield 1
    yield 2
    yield 3
    return "End of sequence"

gen = generate_numbers()

try:
    while True:
        print(next(gen))
except StopIteration as e:
    print(f"Generator finished with message: {e.value}")
