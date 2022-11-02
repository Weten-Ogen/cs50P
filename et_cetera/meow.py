def say(n: int) -> str: 
    """Meow n timesgit"""
    return "meow\n" * n

number:int = int(input("Number: "))

print(say(number), end="")