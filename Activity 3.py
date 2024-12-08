subject1 = int(input("Enter the marks for your first subject:"))
subject2 = int(input("Enter the marks for your second subject:"))
subject3 = int(input("Enter the marks for your third subject:"))
subject4 = int(input("Enter the marks for your last subject:"))

sum = subject1 + subject2 + subject3 + subject4

print(sum)

avg = sum/400
percent = avg*100
print("The percentage of the subjects are ", percent)