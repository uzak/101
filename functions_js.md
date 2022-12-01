# Functions

## Basics
* holds an algorithm, solution to a problems
* called also logic 
    * formal step-by-step description on how to do/achieve/solve something
    * imagine a recipe for cooking
* _frozen thought_
* set of instructions for the computer to achieve something
  
* declaration:
    * name
    * input values (arguments)
    * return type
* definition: declaration + body. In JS no separate declaration.
* usage - call function. Apply recipe. Put arguments in parentheses after the name of the function. It returns your result.

```
function circleArea(radius) {
    return Math.PI * radius * radius; 
}
```

```
> circleArea(5)
78.53981633974483
```

* arrow functions
    * if one line, the expression will be returned automatically. No `return` needed
    * if in block use `{...}`; if you want to return you need to use return

```
> const circleArea2 = radius => Math.PI * radius * radius
```

* anonymous functions

```
> radius => Math.PI * radius * radius
[Function (anonymous)]
> (radius => Math.PI * radius * radius)(5)
78.53981633974483
```

* typeof function

```
> typeof (radius => Math.PI * radius * radius)      // parenthesis because of eval. priority
'function'
> typeof circleArea
'function'
> typeof circleArea2
'function'
```

* callback function
    * callback can be a parameter
    * which is applied by the code of the function
    * to perform some modification on the data processed in the function

## Functional Programming
* collections + functions
* heavy use of callbacks
  
### .forEach()
```
> let numbers = [3, 54, 4e1, 4]
> numbers
[ 3, 54, 40, 4 ]
> numbers.forEach((elem, index) => {
...     console.log(`${index} contains the value ${elem}`)
... })
0 contains the value 3
1 contains the value 54
2 contains the value 40
3 contains the value 4
> numbers.forEach((elem, index) => console.log(`${index} contains the value ${elem}`))
...
> numbers.forEach(number => console.log(number))
3
54
40
4
```

* task: compute and print the circleArea for all `numbers`
```
> numbers.map(circleArea)
[
  28.274333882308138,
  9160.884177867836,
  5026.548245743669,
  50.26548245743669
]
```

### .map()

* .forEach() returns undefined. .map() returns the list of modified values. Q: how many elements will the result have?
* task: double the integer of an array
```
> numbers.map(n => n*2)
[ 6, 108, 80, 8 ]
```
* task: lowercase and remove leading spaces of an string array

```
> let names = ["   PETER", "   john", "Marry  "]
> names.map(name => name.trim().toLowerCase())
[ 'peter', 'john', 'marry' ]
```

### .filter()
* task: remove empty strings from an array
```
> let tokens = ["", "one", "two", "", "three"]
> tokens.filter(t => t.length > 0)
[ 'one', 'two', 'three' ]
> tokens.filter(t => t)
[ 'one', 'two', 'three' ]
```
* task: return only even numbers
```
> numbers.filter(n => (n % 2) == 0)
[ 54, 40, 4 ]
> numbers.filter(n => !(n % 2))
[ 54, 40, 4 ]
```

### .reduce() - reduce down to one value while aggregating
`array.reduce(function(total, currentValue, currentIndex, arr), initialValue)`

* task: sum()

```
> numbers.reduce((acc, next) => acc + next, 0)
101
```


* task: max()
```
> numbers.reduce((acc, next) => (next > acc ? next : acc), numbers[0])
54
```