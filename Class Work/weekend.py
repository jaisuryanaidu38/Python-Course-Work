amount = int(input("Enter the amount:"))

if amount > 10000:
    print("Trip to Goa")
elif 8000 <= amount < 10000:
    print("clubings")
elif 5000 <= amount < 10000:
    print("G0 for cafe")
elif 3000 <= amount < 5000:
    print("Shopping")
elif 1000 <= amount < 3000:
    print("Vist to local places")
elif 500 <= amount < 1000:
    print("Order something")
else:
    print("Go for chai&sleep")
