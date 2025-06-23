print("Hello World!")

name = "Noelle"
print("Hello" , name, "!")  # with a comma
print("Hello" + name + "!")  # with a +

age = 42
print("Hello", age, "!")  # with a comma
# print("Hello" + age + "!")  # with a + (this will cause an error)
print("Hello" + str(age) + "!")  # with a + and converting age to string

food1 = "sushi"
food2 = "pizza"
print(" {} {}".format(food1, food2))  # with .format()
print(f"I like {food1} and {food2}!")  # with an f string