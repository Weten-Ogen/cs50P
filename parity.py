def main():
  x = int(input("what's X? "))
  print(is_even(x))



def is_even(n):
  return n % 2 == 0
main()