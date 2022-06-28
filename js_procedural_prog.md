# JavaScript: Procedural Programming 101


## Prerequisites

* Install `node` and `npm`
* Be able to access your browser's developer tools
* Ideally an UNIX OS (Linux, MacOS)

## Fundamentals

### Syntax and Semantics

* Gramar. A computer is a gramar nazi.
* Computer doesn't think. Programmers (hopefully) do.

### Flow of execution
* Programmers direct the flow.
* Computer starts at the top and works down to the bottom. 
* Programer's job is to manage the complexity. The tool to achieve that in procedural programming is functions and modules.

### Expressions, Statements, REPL

* Expression anything evaluated to produce a value.
* REPL: read-eval-print loop. Evaluates an expression and shows the result. E.g. node:
```js
> 5
5
> 5 + 5
10
> Math.pow(5, 2) - 10/2
20
```
* Statement does something without producing a value. In javascript this means the value `undefined` is produced.
```js
> let result    // introduce a new variable without assigning it a value
undefined
> nonExistingVariable
Uncaught ReferenceError: nonExistingVariable is not defined
```
* Each statement needs can optionally end with a semicolon (`;`).

### CLI

* terminal/console/command line
* GUI vs. CLI
* textual way of communicating with the computer
* powerful. Learn basic commands:
```sh
$ pwd             # print current working directory
/Users/m
$ cd repos        # change into repos direcotry
$ ls              # list it
101      blog     dotfiles
$ pwd
/Users/m/repos
$ cd              # go back to home
$ pwd
/Users/m
```

**Exercises**
* Learn UNIX basics [here](https://linuxsurvival.com/).

## Variables

* labeled container
* naming super important
  * descriptive
  * qualification
* english only
* camel case
* let vs. var, const
```js
> const PI = 3.14;    // read-only
undefined
> let sum = 0;
undefined
```

## IO

* `prompt()`
* `console.log()`
```bash
$ npm instal prompt-sync    # install module 

added 3 packages, and audited 4 packages in 588ms

found 0 vulnerabilities
```
```js
$ cat test.js                             # code stored in a file
prompt = require("prompt-sync")();        // load module

let answer = prompt("What's your name: ") // ask the user 
console.log("Hello " + answer)            // print out the answer
```
```bash
$ node test.js
What's your name: Martin
Hello Martin
```

**Exercises:**
* Write a program that asks the user for his age and print it out.
* Write a program that asks the user for his name and age and prints out both out.

## Data Types and Operators

* primitive (single value) vs. complex. 
* typeof
```js
> let name = "Martin"
undefined
> let age = 42
undefined
> typeof result
'number'
> typeof name
'string'
```

### String
* complex data type
* enclose with either `"` or `'` for definition.
* what the user enters via `prompt()` is always a string (even if the enters a number).
```js
> prompt = require("prompt-sync")();
> typeof prompt("Input: ")
Input: 123
'string'
```
* indexing (sequential data types). Starts with 0.
* slicing 

```js
> name[0]
'M'
> name[1]
'a'
> name.slice(1)       // all from 1st character
'artin'
> name.slice(1, 4)    // all from 1st to 4th
'art'
> name.slice(1, -1)
'arti'
> "Hello " + name     // plus operator joins strings
'Hello Martin'
> `Hello ${name}`     // interpolation of variables
'Hello Martin'
> name.startsWith("Mar")
true
> name.startsWith("Peter")
false
> name.toUpperCase()
'MARTIN'
> "one:two:three".split(":")    // split String into an array
[ 'one', 'two', 'three' ]
```
* Strings are immutable!
```js
> let s = 'hello'
undefined
> s[0] = 'M'
'M'
> s
'hello'
```

**Exercises**
* Go [here](https://www.w3schools.com/jsref/jsref_obj_string.asp) and get acquinted with all the string methods. Test all of the methods at least with three different strings in `node`.

### Number
* For the computer everything is a number. That's why it is a computer. Only we give it a different meaning (data type) and representation.

```js
> 1 + 1
2
> 2 * 2
4
> 3 - 1
2
> 51 / 6
8.5
> 51 % 6
3
> Math.floor(51/6)        // round down
8
> 4 ** 2                  // power
16
> Math.sqrt(9)            // square root
3
> (Math.sqrt(9) - 2) % 2  // expressions can be complex
> "1"                     // string, not a number!
'1'
> parseInt("1")           // convert a string to a number
1
```
* Increment and decrement a variable
```js
> let counter = 0
undefined
> counter++     // first use (-> 0) and then increment
0
> counter       // that's why counter is now 1
1
> ++counter     // first increment and then use (2)
2
```
* Short notation
```js
> let sum = 1
undefined
> sum
1
> sum = sum + 2
3
> sum += 5      // works for any number operator with two operands
8
```

**Exercises**
* Read [First Steps in Math in JS](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Math])
* Read [Number objectx reference](
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number) and practice all the listed operations and properties of the `Number` object in `node`.

### Boolean
* `true` and `false`
* always use `===` unless you know what you're doing
```js
> 1 === 3 - 2
true
> 1 !== 2
true
> 2 === 3
false
> 3 >= 2
true
> "Yes" === "yes"     // case sensitive
false
```
* logical operators (important for conditionals and loops)
```js
> x === 1 && y <= 2     // true && true -> true
true
> x === 42 || y == 1    // false || true -> true
false
> !true                 // negation
false
```
* ternary operator
```js
> let randNumber = Math.random() * 10 // generate a random number from 0 to 10.
undefined
> randNumber
8.233034570095928
> what = randNumber >= 5 ? "bigger or equal" : "smaller"
'bigger or equal'
> `${randNumber} is ${what} than 5`
'8.233034570095928 is bigger or equal than 5'
>
```

**Exercises**
* Write a program that asks the user for this name and age. It converts the age to a number and if it is between 13 and 19 it will print out his name and call him teenager.


### Array
* Mutable collection of elements with a defined order
```js
> let numbers = [1, 2, 3, 4]
undefined
> numbers
[ 1, 2, 3, 4 ]
> numbers[1]
2
> numbers.slice(1, -1)
[ 2, 3 ]
> numbers[0] = 9
9
> numbers
[ 9, 2, 3, 4 ]
> numbers.sort() 
[ 2, 3, 4, 9 ]
> numbers.length      // number of elements
4
> numbers.push(5)     // append to the end
5
> numbers
[ 2, 3, 4, 9, 5 ]
> numbers.pop()       // remove last from the end
5
> numbers
[ 2, 3, 4, 9 ]
> numbers.shift()     // remove first from the beginning
2
> numbers
[ 3, 4, 9 ]
> numbers.unshift(1)  // add at the first place; return number of elements
4
> numbers
[ 1, 3, 4, 9 ]
```

**Exercises**
* Read about [Arrays](https://javascript.info/array) and try out all methods and properties of `Arrays` in `node` at least three times.

### Object
* An object is a collection of key value pairs. Keys are strings, values can be anything.

```js
> let person = {
...  name: "Peter",
...  age: 30
... }
undefined
> person
{ name: 'Peter', age: 30 }
> person.age          // same as above
30 
> person.hobbies = ['Running', 'Cooking']   // values can be anything
[ 'Running', 'Cooking' ]
> person
{
  name: 'Peter',
  age: 30,
  hobbies: [ 'Running', 'Cooking' ]
}
> delete person.hobbies
true
> person
{ name: 'Peter', age: 30 }
```

**Exercise**
* Create a program that will ask the user for the data about a person. The user can specify name, age, profession. Three persons can be entered. Store them in an array and log it to the console before the program exits.

### Set
* A `Set` is a collection of unique values. There is no order defined for it. Value Lookups are very efficient.

```js
> let set = new Set()
undefined
> set
Set(0) {}
> set.add(1)
Set(1) { 1 }
> set.add(2)
Set(2) { 1, 2 }
> set.add(1)          // duplicate values are not stored
Set(2) { 1, 2 }
```

## Conditionals
* control the flow 
* `if / else if / else`

```js
> let num = Math.floor(Math.random() * 10) // generate random int from 0 to 9
undefined
> if (num > 5) {
...  console.log("big")
... } else if (num === 5) {
...  console.log("five")
... } else {
...  console.log("small")
... }
big
```
* [NaN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN) (Not A Number) is a special datatype used for checking if the value is a number:
```js
> isNaN("hello")
true
> isNaN("5.5")
false
> let input = "42.01"  // something from the user
undefined
> if (!isNaN(input)) {
... console.log("Your input is a valid number")
... }
Your input is a valid number
undefined
> NaN * 34
NaN
> NaN - NaN
NaN
```

## Loops
* DRY -> automatization
* while
```js
> let i = 0
undefined
> while (i < 5) {
... console.log(i)
... i++
... }
0
1
2
3
4
5
5
```
* for, for of, for of
```js
> for (let i=0; i<3; i++) {
... console.log(i)
... }
0
1
2
undefined

> let fruits = ["banana", "orange", "apple"]
undefined
> for (let fruit of fruits) {
...  console.log(fruit)
... }
banana
orange
apple
undefined

> let person = {
... name: "Peter",
... age: 21,
... profession: "IT expert",
... }
undefined
> for (key in person) {
... console.log(`${key} -> ${person[key]}`)
... }
name -> Peter
age -> 21
profession -> IT expert
undefined
```
* break, continue
```js
> for (let fruit of fruits) {
... console.log(fruit)
... if (fruit === "banana") {
..... break
..... }
... }
banana
undefined

> for (let i=0; i<3; i++) {
... if (i === 1) {
..... continue      // let's go to next loop iteration
..... }
... console.log(i)
... }
0
2
undefined
```
* iteration

**Exercises**
* Read about [while @ MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while)

## Functions
* Centerpiece of procedural programming
* Divide and conquer
* Example: 
    * travel expense -> accountant -> money
    * painter(room_color)
* Procedure vs. function
* logic of a program
* [Builtin functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects#function_properties)
* namespace, universe on it's own
* blackbox
* anonymous/lambda/arrow functions 

**Exercise**
* Write a function that will sum two numbers and return the result.
* Write a small program that will compute the circumference of a circle for the numbers 0 to 10. Make sure to create in it a function which computes the circumference.

### Custom functions
* Magic, powerful words. Analogy: spell.
* Components: 
  1. name
  2. arguments (input)
  3. return value

## Comments
* The less the better
* Hints where factoring a function could be useful
```js
> /* multiline
... comments */
undefined
> // single line comments
undefined
```

## Error handling

## Modules

## Software Engineering

* KISS
* DRY
* Garbage in, garbage out
* Clean programming
* 80x24
* 0 -> great, 1 -> good, 2 -> OK, 3 and more -> too complex
* Bulgarian constants
* Step-by-Step
* Debugging vs. console.log

## Resources

https://www.javascripttutorial.net/

https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics


# TODO
* Control questions
* Basic formatting guidelines?
