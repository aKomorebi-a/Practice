def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name} ")
    print("Welcome aboard!")
# 1

# greet("ale", "ramos")

# 1- perfom a task
# 2- return a value


# def get_greeting(name):
#     return f"Hi {name}"


# message = get_greeting("alee")
# print(message)

# keyword arguments
def increment(number, by=1):
    return number + by


# result = increment(2, 1)
# print(result)
# print(increment(2, by = 1))

# default arguments

# print(increment(2, 10))  # opcional, by = 1

# x args

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5, 6))
