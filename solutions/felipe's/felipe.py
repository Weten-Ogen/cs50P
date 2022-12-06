menu = {
     'bajo taco' : 4.00,
     'burrito'   : 7.50,
     'bowl'      : 8.50,
     'nachos'    : 11.00,
     'quesadilla': 8.50,
     'super burrito': 8.50, 
     'super quesadilla': 9.50,
     'taco': 3.00,
     'totilla salad': 8.00,

}


try: 
    cost = 0
    while True:
        order = input("What are you'r your orders : ").lower()
        if order in menu:
            cost = cost + menu[order]
            print(f"Item : ${cost:.2f}")
        
except EOFError:
    print(f"\n Item : ${cost:.2f}")
     
