# Basic Python Programming

## 1. Variables 

**Type of variables**

```py
10
186.5
"Hello worlds"
True
False
(1, 2)
{"name": "John Doe", "email": "john.doe@mail.com"}
[1, 2, 3, 4, 5, 8]
{1, 2, 3}
```

**Basic operators**

```py
print("Hello world!")
type(10) # type of the expression's value

10 + 15 # 25
10 - 7 # 3
10 * 2 # 20
10 / 5 # 2
10 // 3 # 3
10 % 3 # 1
10 ** 3 # 1,000


# Relational operator
5 > 2 # True
4 >= 5 # False
5 == 10 # False
'hello' == 'hello' # True
'Hello' == 'hello' # False
'hello' != 'hello' # False
'Hello' != 'hello'  # True
'orange' < 'apple' # compare by alphabetical order
```

**or, and, not Operator**

```py
digit = 3
digit == 8 or digit == 9 # False or False => False
not True # False
```

**if Statement**

```py
apple_total = 20
banana_total = 6
if apple_total > banana_total:
    print('A')


if apple_total > banana_total:
    print('A')
elif banana_total > apple_total:
    print('B')
else: # apple_total == banana_total
    print('T')
```

**For Loop Operator** 

```py
sum = 0
for i in range(10):
    sum += i
print(sum)

for fruit in ["apple", "orange", "tomato"]:
    print(fruit)

for i, fruit in enumerate(["apple", "orange", "tomato"]):
    print(fruit)
```

**While Loop Operator** 

```py
index = 0

while index < 10:
    print(index)
    index = index + 1

```

## 2. Functions

```py
def print_greeting():
    print("hello!")
    
def sum(a, b):
    return a + b 
```

## 3. Class

```py
class Human():
    age = 0
    name = ''
    
    def __init__(self, input_name, input_age):
        self.name = name
        self.age = age
    
    def self_intro(self):
        print("Hi! I'm" + self.name) # or print("Hi! I'm {self.name}")


john = Human('johnathan wick', 20)

# Artibute
print(john.name)
print(john.age)

# Methods
john.self_intro()
```

```py
class Student(Human):   

    def print_student_id(self):
        print("My ID is 1234")

    def self_intro(self):
        print("Hi! I'm a Student. Please call me " + self.name)
        # or 
        # print(f"Hi! I'm a Student. Please call me {self.name}.")
        
simon = Student('Simon Si', 21)

# Artibute
print(simon.name)
print(simon.age)

# Methods
simon.self_intro()
simon.print_student_id()


```

## 4. Useful Library (numpy, matplotlib, pandas)

### Numpy

```py
import numpy as np

# ndarray creation
number_array = np.array([0, 1, 2, 3, 4, 5])
print(number_array)

arange_array = np.arange(6)
print(arange_array)

zero_array = np.zeros(6)
print(zero_array)

# ndarray reshape

reshape_number_array = number_array.reshape(2,3)
print(reshape_number_array)


# Attributes of ndarray
def check_array_properties(array):
    print(f"Array type: {type(array)}" )
    print(f"Array Size {number_array.size}")
    print(f"Shape: {number_array.shape}")
    print(f"Dimesions: {number_array.ndim}")
    print(f"Dtype: {number_array.dtype}" )

print("----- number_array properties ------")
check_array_properties(number_array)
print("----- reshape_number_array properties ------")
check_array_properties(reshape_number_array)

# Array Indexing, Slicing, Iterations

print(number_array[0])
print(number_array[5])
print(number_array[-1])
print(number_array[-2])

print(number_array[0:2])
print(number_array[2:5])
print(number_array[2:])

for number in number_array:
    print(f"number {number} is in number_array")


### Min, Max, Mean, Std, Example

```

### Matplotlib

```py
import numpy as np
import matplotlib.pyplot as plt

# generate random signal (lowest value = 1, size of array = 50)
random_int = np.randint(1, size= 50) 

plt.plot(random_int)

```

### Pandas

```py

```



## Challenge

### 1. Basic python
  - Diamon Printing
  - Brick Pyramid Counter


### 2. Numpy, Matplotlib (Keyword : Functional Prog)
  - Find Min ,Max, Mean, Std
  - Plot Sinwave (2 waves combine. / diff / amp)
  - generate data (on pandas) + bar graph histogram

## pandas (Keyword : Data Representation)
  - Visualization (Table)
  - Get Specific Datarow and cal min.max, mean, std
  - plot specific axis (data access -> selec x, y then plot 2D -. Age vs BMI)
  