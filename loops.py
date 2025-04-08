# for number in range(3):
#     print("Attempt", number + 1, (number + 1) * ".")

# for number in range(1, 4):
#     print("Attempt", number, number * ".")

# for number in range(1, 10, 2):
#     print("Attempt", number, number * ".")

# successful = True

# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break

# successful = False

# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break
# else:
#     print("Attempted 3 times and failed")

# nested loops

# for x in range(5):
#     for y in range(3):
#         print(f"({x}, {y})")

# iterables
# print(type(5))
# print(type(range(5)))

# for x in range(5):
#     print(x)

# for x in "Python":
#     print(x)

# for x in [1, 2, 3, 4]:
#     print(x)

# while loops

# number = 100
# while number > 0:
#     print(number)
#     number //= 2

# command = ""
# while command != "quit" and command != "QUIT":
#     command = input(">")
#     print("Echo", command)

# while command.lower() != "quit": #no importa si es mayus o minus
#     command = input(">")
#     print("Echo", command)

# while True:
#     command = input(">")
#     if command.lower() == "quit":
#         break

# for number in range(1, 10):
#     if number % 2 == 0:
#         print(number, "is even")

# solution
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")
