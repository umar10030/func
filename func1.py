def well_wishes():
    print("hello")
    print("how are u?")

well_wishes() # calling function

# activity 2
def weather_codition():
    spring = "March to May"
    autumn = "September to November"
    print('the wether is pleasant in:', spring)
    print('the wether is pleasant in:', autumn)

weather_codition()
# activity 3
# calulater
def add(p,q):
    return p + q
def subtract(p, q):
    return p - q
def multiply(p, q):
    return p * q
def divide(p, q):
    return p / q

print("please select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = input("Enter choice(1/2/3/4): ")

num1 = int (input("Enter first number: "))
num2 = int (input("Enter second number: "))
if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input, please select a valid operation.")
