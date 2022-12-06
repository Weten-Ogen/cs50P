menu = {
     'Bajo taco' : 4.00,
     'Burrito'   : 7.50,
     'Bowl'      : 8.50,
     'Nachos'    : 11.00,
     'Quesadilla': 8.50,
     'Super Burrito': 8.50, 
     'Super Quesadilla': 9.50,
     'Taco': 3.00,
     'Totilla Salad': 8.00,

}


try: 
    cost = 0
    while True:
        order = input("What are you'r your orders : ").title()
        if order in menu:
            print(order)
            cost = cost + menu[order]
            print(f"Item : ${cost:.2f}")
        
except EOFError:
    print(f"\n Item : ${cost:.2f}")
    
