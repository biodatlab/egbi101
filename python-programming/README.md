# Introduction to Python Programming

## 1. Installation

### 1.1 Run Jupytor Locally  

- Download [Anaconda](https://www.anaconda.com/products/individual) to your local computer

    #### A. Mac OSX / Linux

    - If you use the command line installer, run `bash Anaconda3-2021.11-MacOSX-x86_64.sh` (for MacOS)
    - Check if you point the path correctly to Anaconda by running following commands on terminal.

    ```sh
    which python
    which ipython
    ```

    #### B. Windows 

    - Run `Anaconda3-2021.11-Windows-x86_64.exe`
    - Check if you point the path correctly to Anaconda by running following commands on `Anaconda Prompt`.

    ```sh
    where python
    where ipython
    ```

## Create your first Jupyter notebook

Goes to directory you would like to work on. And run the following commands

```sh
jupyter notebook
```

Then goes to `localhost:8888` (default port) and the create a new notebook.
Generally, we use a 



## Basic Python Programming

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
10 + 15 # 25
type(10) # type of the expression's value

# Relational operator
5 > 2 # True
4 >= 5 # False
5 == 10 # False
'hello' == 'hello'
'Hello' == 'hello'
'orange' < 'apple' # compare by alphabetical order
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
elif apple_total == banana_total:
    print('T')
```

**or, and, not Operator**

```py
digit = 3
digit == 8 or digit == 9 # False or False => False
not True # False
```

**for Operator** 

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
