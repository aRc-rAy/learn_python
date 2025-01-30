from functools import reduce

def add_2(x):
    return x + 2

def multiply_3(x):
    return x * 3

def compose(f, g):
    return lambda x: f(g(x))

composed_function = compose(add_2, multiply_3)
print(composed_function(5)) 


def pipeline(data,funs):
      return reduce(lambda a,b:b(a),funs,data)

steps = [
    lambda x: x + 1,
    lambda x: x * 2,
    lambda x: x - 3
]

result = pipeline(5, steps)
print(result) # Output: ((5 + 1) * 2) - 3 = 9