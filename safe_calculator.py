while True:
    print("\n1. Addition")
    print("\2. Substraction")
    print("\3. Multiplication")
    print("\4. Division")
    print("5. Exit")

    try:
        choice = input("Choose: ").strip()
    except KeyboardInterrupt:
        print("\nprogram stopped safely.")
        break

    if choice == 5:
        print("Goodbye!")
        break

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except:
        print("Invalid number imput")
        continue

    if choice == "1":
        print("Result:", num1 + num2)
    elif choice == "2":
        print("Result:", num1 - num2)
    elif choice == "3":
        print("Result:", num1 * num2)
    elif choice == "4":
        if num2 == 0:
            print("Cannot divided by zero")
        else:
            print("Result:", num1/num2)