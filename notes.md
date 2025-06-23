is_hungry = True //Boolean
age = 35 // int
weight = 160.57 // Float
name = "Joe" // String

Tuples // can't be modified, contains mixed data types
dog = ('Bruce', 'cocker spaniel', 19, false)
print(dog[0]) // Bruce
dog[1] = 'dachshund' //Error, cannot be modified

Lists // data that is mutable, hold a group of values
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2]) // Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas) // ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas) // ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas) // ['Francis', 'Oliver']

Dictionaries // group of key-value pairs. Dictionary elements are indexed by unique keys which are used to access values
new_person = {'name': 'John, 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack' //updates if key exists, adds a key value pair if not
new_person['hobbies'] = ['climbing', 'coding']
print(new_person) // {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
w = new_person.pop('weight') // removes the specified key and returns the value
print(w) // 160.2
print(new_person) // {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}

Type // allows you to check a variables data type
print(type(2.63)) // Float
print(type(new_person)) // Dict

Len // Returns number of items in an object
string = "Hello"
list = [1, 2, 3, 4, 5]
dict = {'a': 1, 'b': 2, 'c': 3}
print(len(string)) // 5
print(len(list)) // 5
print(len(dict)) // 3

Conversion // Convert number types from one to another
int_to_float = float(35)
float_to_int = int(44.2)
print(int_to_float) // 35.0
print(float_to_int) // 44

Random
import random
random_float = random.random() // Random float between 0 and 1
random_int = random.randint(1, 10) // Random integer between 1 and 10
my_list = ['apple', 'banana', 'cherry'] 
random_element = random.choice(my_list)
print(random_element) // Banana
random.shuffle(my_list)
print(my_list) // ['banana', 'cherry', 'apple']

Strings Fundamentals
    Concatenating Strings & Variables
name = 'Zen'
print('My name is', name)
print('My name is ' + name)

Type Casting
print("Hello" + 42) // TypeError
print("Hello" + str(42)) // Hello 42
total = 35
user_val = '26'
total = total + user_val // TypeError
total = total + int(user_val) // 61

F-Strings
first_name = 'Zen'
last_name = 'Coder'
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.)

Built-In String Methods
x = 'hello world'
print(x.title()) // "Hello World"

