# create a defined function
def greet_user():
    print('Hi there!')
    print('Welcome aboard!')


# execution of program starts here
print("Start")
greet_user()
print("Finish")


# how to pass information to functions
def greet_user(name):
    print(f'Hi {name}!')
    print('Welcome aboard!')


print("Start")
greet_user("John")
greet_user("Mary")
print("Finish")


# name is argument put into parameters (holes)
# in positional arguments order matters

def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard!')


print("Start")
greet_user("Smith", "John")
print("Finish")

# in keyword arguments positions doesnt matter

greet_user(last_name="Smith", first_name="John")
