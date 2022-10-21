def say(n: int) -> str: 
    """Meow n times"""
    return "meow\n" * n

number:int = int(input("Number: "))

print(say(number), end="")