# Python: procedural programming 101

Introduction into procedural programming with Python. For more detailed intro, please see the official [tutorial](https://docs.python.org/3/tutorial/index.html).

## Love on the first input

* Immediate feedback: No compile, link, build cycle
* [Batteries](https://docs.python.org/3/library/index.html) included - powerful infrastructure
* Easy syntax

```python
>>> users = [l.split(":")[0] for l in open("/etc/passwd")]
>>> users
['root',
 'daemon',
 ...
 'sshd',
]
>>> len(users)
52
>>> 1 + 1
2
>>> len("Hello world")
11
```


## Variables
* placeholder for changing data
* meaningful names important
* English
* private names start with _, super-duper private __, magic start and end with __

```python
>>> result = 2**8
>>> __name__
'__main__'
```

## Datatypes (Values)
### Primitive 

* Calculator
    * integer
    * float
        * never compare for equality! 
            ```python
            >>> 2.2 * 3.0 == 6.6
            False
            ```
* Operators: +, -, /, *, %, **, ==
* Expression vs. statements

```python
>>> (2 + 5) ** 2
49
>>> 55 % 2
1
>>> 55 % 10
5
>>> 55 / 2
27.5
>>> 55 // 2
27
```


### Complex

* Strings
* (few) operators, many methods
* fStrings
* immutable
* IO in scripts: input(), print()

```python
>>> name = "Martin"
>>> f"Hello {name}"
'Hello Martin'
>>> "-"*50
'--------------------------------------------------'
>>> "Hello" + " Martin"
'Hello Martin'
>>> name.isupper()
False
>>> name.upper()
'MARTIN'
>>> name.count("a")
1
>>> name.index('n')
5
```

```shell
➜  ~ cat console_io.py 
name = input("What's your name?\n")
print(f"Hello {name}!")
➜  ~ python console_io.py
What's your name?
Martin
Hello Martin!
```

### Complex contd.
* sequences, like string
* tuple - not mutable
* list
* sorted()

```python
>>> v = (1, 2, 3)
>>> v
(1, 2, 3)
>>> v[0]
1
>>> v[0:-1]
(1, 2)
>>> 1 in v
True
>>> l = [200, 150, 200]
>>> l[1] = 120
>>> l
[200, 120, 200]
>>> sorted(l)
[120, 200, 200]
>>> min(l)
120
>>> max(l)
200
>>> 
```

### Complex contd.
* associative arrays (hashing), but also iterable
* dictionary
* set

```python
>>> s = {200, 120, 200}
>>> s
{200, 120}
>>> d = {'Martin': 20, 'Peter': 25}
>>> d
{'Martin': 20, 'Peter': 25}
>>> d['Peter']
25
>>> "Martin" in d
True
>>> del d['Martin']
>>> d
{'Peter': 25}
```

## Control Structures
* bool
* operators: ==, !=, is, not, <, >
* if expr: block

```python
>>> 1 > 1
False
>>> 1 == 1
True
>>> True and True
True
>>> True and False
False
>>> True or False
True
>>> False or False
False
>>> not True
False
>>> value = 42
>>> if value > 0:
...  print("Value is positive")
... elif value == 0:
...  print("Value is zero)
... else:
...  print(f"{value} is negative")
... 
Value is positive
None
>>> 
```

## Loops
* iterate: for for sequences 
* range(), enumerate()
* while for repetition tied to a logical condition
* recursion

```python
>>> for i in (1, 2, 3):
...  i**2
... 
1
4
9
>>> for i in range(3):
...  i
... 
0
1
2
>>> for idx, name in enumerate(["Peter", "John"]):
...  idx, name
... 
(0, 'Peter')
(1, 'John')
>>> 
>>> to_be_done = 3
>>> while to_be_done > 0:
...  # do something
...  to_be_done = to_be_done -1
...  to_be_done
... 
2
1
0
```


## Functions
### Builtin functions
* dir(), locals()
* ord(), chr()
* eval(), exit()
* hash(), id(), type()
* abs(), min(), max()
* str(), repr()
* help()

### Custom
* blackbox, recipe
* def NAME(POS_ARG, OPT_ARG): code
* a procedure returns None
* None is returned if no explicit return statement is used

```python
>>> import math
>>> def pythagoras(a, b):
...  c2 = a**2 + b**2
...  return math.sqrt(c2)
... 
>>> pythagoras(2, 3)
3.605551275463989
>>> pythagoras(1, 1)
1.4142135623730951
>>> 
```

## Modules
* sys
* math
* os