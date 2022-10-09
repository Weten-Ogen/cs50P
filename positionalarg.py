def foo(x=0,y=0, /):
  return x  + y

print(foo(3,2))

def foo1(x,y):
  return x * y

print(foo1(x=5,y=6))
def hexadec(n):
  return f'{n:#x}'

print(hexadec(255))