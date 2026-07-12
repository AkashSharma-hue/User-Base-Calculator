#Calculator Project Using Functions

history = {}

while True:
    print("\n------CALCULATOR------\n")
    print("1. HISTORY (H) \n2. ADD (+) \n3. SUBTRACT (-) \n4. MULTIPLY (X) \n5. DIVISION (/) \n6. REMAINDER (rem) \n7. PERCENTAGE (%) \n8. AVERAGE (avg) \n9. EXIT (E) \n")
    
    choice = input("Enter your choice : ")
    print(f"Yours choice : {choice}")
    
    #Addition
    if choice == '+':
        li = []
        while True:
            num = int(input("Enter your number : "))
            li.append(num)
            
            sign = input("Enter (+) or (=) or default is + : ")
            if sign == '+':
                continue
            elif sign == '=':
                break
            else:
                continue

        add = li[0]
        for i in li[1:]:
            add += i
        print("SUM :",add)
        history[f"Calculation {len(history) + 1}"] = f"SUM : {add}"
    
    #Subtraction
    elif choice == '-':
        li = []
        while True:
            num = int(input("Enter your number : "))
            li.append(num)
            
            sign = input("Enter (-) or (=) or default is - : ")
            if sign == '-':
                continue
            elif sign == '=':
                break
            else:
                continue

        sub = li[0]
        for i in li[1:]:
            sub -= i
        print("SUBTRACT :", sub)
        history[f"Calculation {len(history) + 1}"] = f"SUBTRACT : {sub}"
        
    #Multiplication
    elif choice == 'X':
        li = []
        while True:
            num = int(input("Enter your number : "))
            li.append(num)
            
            sign = input("Enter (X) or (=) or default is X : ")
            if sign == 'X':
                continue
            elif sign == '=':
                break
            else:
                continue

        mul = li[0]
        for i in li[1:]:
            mul *= i
        print("MULTIPLY :", mul)
        history[f"Calculation {len(history) + 1}"] = f"MULTIPLICATION : {mul}"
    
    #Division
    elif choice == '/':
        li = []
        while True:
            num = int(input("Enter your number : "))
            li.append(num)
            
            sign = input("Enter (/) or (=) or default is / : ")
            if sign == '-':
                continue
            elif sign == '=':
                break
            else:
                continue

        div = li[0]
        for i in li[1:]:
            div /= i
        print("DIVISION :", div)
        history[f"Calculation {len(history) + 1}"] = f"DIVISION : {div}"
    
    #Remainder
    elif choice.lower() == 'rem':
        li = []
        while True:
            num = int(input("Enter your number : "))
            li.append(num)
            
            sign = input("Enter (rem) or (=) or default is rem : ")
            if sign == 'rem':
                continue
            elif sign == '=':
                break
            else:
                continue

        rem = li[0]
        for i in li[1:]:
            rem %= i
        print("Remainder :", rem)
        history[f"Calculation {len(history) + 1}"] = f"REMAINDER : {rem}"
    
    #Percentage
    elif choice == '%':
        li = []
        while True:
            num = int(input("Enter your number : "))
            li.append(num)
            
            sign = input("Enter (%) or (=) or default is % : ")
            if sign == '%':
                continue
            elif sign == '=':
                break
            else:
                continue

        total_obtain = li[0]
        for i in li[1:]:
            total_obtain += i
            
        total_possible = len(li) * 100
        percent = (total_obtain / total_possible) * 100
        print("PERCENTAGE :", percent)
        history[f"Calculation {len(history) + 1}"] = f"PERCENTAGE : {percent}"
    
    #Average
    elif choice.lower() == 'avg':
        li = []
        while True:
            num = int(input("Enter your number : "))
            li.append(num)
            
            sign = input("Enter (avg) or (=) or default is avg : ")
            if sign == 'avg':
                continue
            elif sign == '=':
                break
            else:
                continue
        
        total = li[0]
        for i in li[1:]:
            total += i
        
        avg = total/len(li)
        print("AVERAGE :", avg)
        history[f"Calculation {len(history) + 1}"] = f"AVERAGE : {avg}"
    
    #History
    elif choice.lower() =='h':
        print("\n---Calculation History---\n")
        if not history:
            print("No calculations made yet")
        else:
            for key, value in history.items():
                print(f"{key} -> {value}")
    
    #Exit
    elif choice.lower() == 'e':
        print("Exiting the program....")
        break
    
    #Default
    else:
        print("We don't know this! Congratulations for your discovery :)")

