amount = int(input("Enter your amount: "))

a1 = amount//100
a2 = (amount %100)//50
a3 = ((amount %50)%100)//10

print("The note of 100 are " ,a1)
print("The notes of 50 are " ,a2)
print("The notes of 10 are " ,a3)