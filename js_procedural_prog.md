# JavaScript: Procedural Programming 101


## Prerequisites

* Install `node` and `npm`
* Be able to access your browser's developer tools
* Ideally use an UNIX OS (Linux, MacOS)

## Fundamentals

### Syntax and Semantics

* Grammar vs. semantics
* Computer is a grammar nazi.
* Computer doesn't think. Programmers (hopefully) do.

### Flow of execution
* Programmers direct the flow.
* Computer starts at the top and works down to the bottom. 
* Programmer's job is to manage the complexity. The tool to achieve that in procedural programming is functions and modules.

### Expressions, Statements, REPL

* Expression anything evaluated to produce a value.
* REPL: read-eval-print loop. Evaluates an expression and shows the result.
    * Also called "interactive mode". 
    * Useful to verify assumptions or as a calculator. E.g.:
```js
> 5
5
> 5 + 5
10
> Math.pow(5, 2) - 10/2
20
```
* Statement does something without producing a value. In Javascript this means the value `undefined` is produced.
```js
> let result            // introduce a new variable without assigning it a value
undefined
> nonExistingVariable   // opposite to non-existing variable
Uncaught ReferenceError: nonExistingVariable is not defined
```
* Each statement can optionally end with a semicolon (`;`).

### CLI (optional)

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

### Before we really begin
* Understanding is important. Computer doesn't think
* Proceed Step-by-Step. Verify.
    * `console.log()`
    <!--
    * debugging
    -->


## Variables

* labeled container
* naming super important
  * descriptive
  * qualification
* English only
* camelCase (CAMEL_CASE for constants)
* let vs. var, const
```js
> let sum = 0;
undefined
> const PI = 3.14;    // read-only
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
```
$ node test.js
What's your name: Martin
Hello Martin
```

**Exercises:**
* Write a program that asks the user for his age and prints it out.
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
* what the user enters via `prompt()` is always a string (even if he enters a number).
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
> "       test   ".trim()
'test'
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
* Go [here](https://www.w3schools.com/jsref/jsref_obj_string.asp) and get acquainted with all the string methods. Test all of the methods at least with three different strings in `node`'s REPL.
* Create a variable `name` with your name (containing both first and last name)
    * split your name into two variables `firstName` and `lastName`
        * using string's `slice()` method
        * using string's `split()` and `trim()` methods
        * give out your name where your `lastName` is in upper case. Use string interpolation (string templates).
    * print the length of the `name`
* Create a program that asks the user for any input. Print the first and the last character he enters.

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
> 51 % 6                  // modulo operator (division rest)
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
> sum += 5      // works for any math operator with two operands
8
```
* [NaN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN) (Not A Number) is a special datatype used for indicating that the value is a number:
```js
> parseInt("this is a string")
NaN
> isNaN("hello")    // check if value is not a number
true
> isNaN("5.5")
false
```


**Exercises**
* Read [First Steps in Math in JS](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Math])
* Read [Number objectx reference](
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number) and practice all the listed operations and properties of the `Number` object in `node`.
* Assign your age to the variable `ageString` as string. Convert to integer and assign this value to the variable `age`.
    * Increment your age using `+=` by 5 years.
    * Decrement your age using `--` by 3 years.
    * Compute the rest of the division when your age is now divided by 2. Print out the rest.
* Ask the user for this age. Print out how many years are missing to the 100th birthday. Make sure to convert the number entered into an integer using `parseInt()`

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
> "Yes" === "yes"     // case sensitivity
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

### Array
* Mutable collection of elements with a defined order
* Can contain duplicates
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
> numbers.pop()       // remove last element
5
> numbers
[ 2, 3, 4, 9 ]
> numbers.shift()     // remove first element
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
* Create a program that will ask the user for the ages of three friends. Print out the median and the average age of the friends.

### Object
* An object is a collection of key value pairs. Keys are strings, values can be anything.
* Also called "hashtable" or "dictionary" in other languages
```js
> let person = {
...  name: "Peter",
...  age: 30
... }
undefined
> person
{ name: 'Peter', age: 30 }
> person.age
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
* Create a program that will ask the user for the data about a person. The user can specify name, age, profession. Three persons can be entered. Store them in an array and print them alphabetically sorted by the name. to the console before the program exits.

### Set
* A `Set` is a collection of unique values. 
* There is no order defined - iteration order might be differnt each time.
* Value Lookups are very efficient.

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

**Exercises**
* Write a program that asks the user for this name and age. It converts the age to a number and if it is between 13 and 19 it will print out his name and call him teenager.
    * Extend the program to call the user "child" if he's less than 13 years old and "adult" if he's more than 19 years old.
    * Extend the program so that it will say "Invalid input. Please enter a number" in the case something other than a number is entered.


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
5           // this 5 comes due to the last expression (i++). only visible in REPL
```
* for
```js
> for (let i=0; i<3; i++) {
... console.log(i)
... }
0
1
2
undefined       // undefined comes from the last console.log(i). Only visible in REPL
```
* for of (iterate through a collection)
```js
> let fruits = ["banana", "orange", "apple"]
undefined
> for (let fruit of fruits) {
...  console.log(fruit)
... }
banana
orange
apple
undefined
``` 
* for in (iterate through object keys)
```js
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
* Create an infinite loop
    * using `while`.
    * using `for`.
* Write a loop that will print out numbers from 1 to 10
    * using `while`.
    * using `for`.
* Write a loop that will print out every number divisible by 3 (use modulo operator) from 1 to 100.
* Create an array with the names of your hobbies. 
    * Iterate through the array and print the index and the hobby.
        * Use `for`
        * Use `for of`
    * Iterate through your hobbies from the end of the list to the start.
    * Iterate through your hobbies from the end of the list to the start printing every second hobby.
* Create an object with the names of your friends as keys. The value the friend's age. Have at least 5 friends in the list. Print out 
    * the friends and their age sorted by the name alphabetically.
    * the friends and their age sorted by the age.
    * the names of 3 youngest friends.

## Functions
* Centerpiece of procedural programming
* Divide and conquer
* Example: 
    * travel expense -> accountant -> money
    <!--
    * painter(room_color)
    -->
* Procedure vs. function
* logic of a program
* [Builtin functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects#function_properties)
* namespace, universe on it's own
* blackbox
* anonymous/lambda/arrow functions 

### Custom functions
* Magic, powerful words. Analogy: spell.
* Components: 
  1. name
  2. arguments (input)
  3. return value

**Example**
```js
// definition of a function
function circleArea(radius) {
    return Math.PI * radius * radius; 
}

// calling a function
console.log(circleArea(5));
```

**Exercise**
* Write a function that will sum two numbers and return the result.
* Write a procedure that will print out the current time. 
* Write a function without arguments that will return a random integer number up to 100.
    * Make the upper range (previously 100) configurable by a parameter called `limit`.
* Write a small program that will compute the circumference of a circle for the numbers 0 to 10. Make sure to create and use for this a function which computes the circumference.
* Write a function that will compute the third side of a triangle. Use it to compute the side for a triangle with the sides 2 and 5. Pint out the result.


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

## Modules
* Also called "library"
* Collection of useful functions.
* Namespace (see functions)
* Use npm to install.

```js
> const fs = require("fs")                  // module for working with the FileSystem
> fs.readFileSync("/etc/hostname", "utf8")  // read the file with the hostname
't480s\n'
```

<!--
### Custom Modules
* [Module Pattern](https://javascript.plainenglish.io/data-hiding-with-javascript-module-pattern-62b71520bddd)

```js
function Person() {
    let firstName = "John";
    let lastName = "Peterson";
    let age = 20;

    var fullName = function() {
        return `${firstName} ${lastName}`;
    }

    return {
        firstName: firstName,
        lastName: lastName,
        age: age,
        fullName: fullName
    }
}

var person = Person();

console.log(person.fullName());
console.log(person.age);
```
-->


## Software Engineering

* KISS
* DRY
* Garbage in, garbage out
* Clean programming
* 80x24
* Complexity: 0 -> great, 1 -> good, 2 -> OK, 3 and more -> too complex
* Bulgarian constants

## Resources

* https://www.javascripttutorial.net/
* https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics


<!--
# TODO

* Control questions
* More exercises
-->
