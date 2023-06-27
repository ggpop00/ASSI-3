while True:
        print("\nPlease select an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. Exponentiation (**)")      
        print("7. Floor Division (//)")
        print("8. Exit")
        Cal = input("Enter choice (1-8): ")
        num1 = float(input("Enter number: "))
        num2 = float(input("Enter number: "))
        if  Cal == "1":
            ans = num1 + num2
        elif Cal == "2":
            ans = num1 - num2
        elif Cal == "3":
            ans = num1 * num2
        elif Cal == "4":
            ans = num1 / num2
        elif Cal == "5":
            ans = num1 % num2
        elif Cal == "6":
            ans = num1 ** num2
        else:
            result = num1 // num2
        print(ans)
