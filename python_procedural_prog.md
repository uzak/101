# Python: Procedural Programming 101

Introduction into procedural programming with Python. For more detailed intro, please see the official [tutorial](https://docs.python.org/3/tutorial/index.html).

## Love on the first input

* Immediate feedback: No compile, link, build cycle
* [Batteries](https://docs.python.org/3/library/index.html) included - powerful infrastructure
* Easy syntax
* [Intro](https://docs.python.org/3/tutorial/introduction.html):

```python
>>> 1 + 1
2
>>> len("Hello world")
11
```


## Variables
* placeholder for changing data
* clear, meaningful names important
* the longer the lifespan the longer the name
* use English only
* private names start with _, super-duper private __, magic start and end with __

```python
>>> result = 2**8       
>>> _protected = 42     # you better know what you're doing when you change it
>>> __name__            # python magic
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


### Collections

* Strings
* (few) operators (*, +, in), many methods
* fStrings
* immutable
* [tutorial: Data Structures](https://docs.python.org/3/tutorial/datastructures.html)

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
>>> name.index('n')
5
>>> "Hello WORLD".count("l")    # l vs. L
2
>>> "World" in "Hello World"
True
```

```python
>>> name = input("What's your name?\n")
What's your name?
Martin
>>> print(f"Hello {name}!")
Hello Martin!
>>> type(name)
<class 'str'>
```

### Collections contd.
* [tuple](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences) (not mutable)
* [list](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
* slicing
* sorted()

```python
>>> v = (1, 2, 3)    # tuple of three elements
>>> v
(1, 2, 3)
>>> v[0]
1
>>> v[0:-1]         # slicing
(1, 2)
>>> 1 in v
True
>>> l = [200, 150, 200] # list of three elements
>>> l[1] = 120          # lists are mutable
>>> l
[200, 120, 200]
>>> sorted(l)
[120, 200, 200]
>>> min(l)
120
>>> max(l)
200
>>> len(l)
3
```

### Collections contd.
* associative arrays (hashing), but also iterable
* [dictionary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) (key - value pairs)
* [set](https://docs.python.org/3/tutorial/datastructures.html#sets)

```python
>>> s = {200, 120, 200}         # no duplicates in a set
>>> s
{200, 120}
>>> 120 in s
True
>>> d = {'Martin': 20, 'Peter': 25} # `d` like dictionary 
>>> d
{'Martin': 20, 'Peter': 25}
>>> d['Peter']
25
>>> "Martin" in d
True
>>> for k, v in d.items():  # iterate over all dict items
...  print(k, v)
... 
Martin 20
Peter 25
>>> del d['Martin']
>>> d
{'Peter': 25}
>>> d['Joe'] = {'age': 20, 'scores': [1,2]} # keys can be complex datatypes
>>> d
{'Peter': 25, 'Joe': {'age': 20, 'scores': [1, 2]}}
```

## Control Structures
* bool datatype
* operators: ==, !=, is, not, <, >
* ```
  if expr: 
      block
    ```

```python
>>> 1 > 1       # comparison produces a bool value
False
>>> 1 == 1
True
>>> True and True  # boolean algebra
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
>>> 
```

All values can be used for logic operations. Non-empty values usually yield True. Use `bool()` to see what it yields.
```python
>>> if "":
...  print("This will never happen!")
... 
>>> bool(0)
False
>>> bool(1)
True
>>> bool(42)
True
>>> bool("")
False
>>> bool([])
False
>>> bool("something")
True
>>> bool([1])
True
```

## Loops
* iterate: go trough each element of a sequence
  * `for`: for sequences 
  * `while`: for repetition tied to a logical condition
* range(), enumerate()

```python
>>> for i in (1, 2, 3):
...  print(i**2)
... 
1
4
9
>>> for i in range(3):
...  print(i)
... 
0
1
2
>>> for idx, name in enumerate(["Peter", "John"]):
...  print(idx, name)
... 
0 Peter
1 John
>>> count = 3
>>> while count > 0:
...  # do something
...  count = count -1
...  print(count)
... 
2
1
0
```

<!--
[Recursion](https://gist.github.com/uzak/d7d38673ba25a63df319f354e96ac094)
```python
>>> def multiplicate(a, b):
...     if a == 1:
...         return b
...     else:
...         return multiplicate(a-1, b) + b
... 
>>> print(multiplicate(1, 5))
5
>>> # 5
>>> 
>>> print(multiplicate(2, 5))
10
>>> # multiplicate(1, 5) + 5
>>> # 5 + 5
>>> 
>>> print(multiplicate(3, 5))
15
>>> # multiplicate(2, 5) + 5
>>> #   multiplicate(1, 5) + 5  + 5
>>> #       5 + 5 + 5
>>> 
```
-->


## Functions
### Builtin functions
* [docs](https://docs.python.org/3/library/functions.html)
* dir(), locals()
* ord(), chr()
* eval(), exit()
* hash(), id(), type()
* abs(), min(), max()
* str(), repr()
* help()

### Custom
* blackbox, recipe
* [defining functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
* input: function [arguments](https://gist.github.com/uzak/d1c9ed717e2ee4f57a2c6de72c1f249a)
* function returns something, a procedure always returns None
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
* [tutorial](https://docs.python.org/3/tutorial/modules.html)
* sys
* math
* os



## IO
* [tutorial: IO](https://docs.python.org/3/tutorial/inputoutput.html) in scripts: input(), print()
