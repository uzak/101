## Unit Testing 101: pytest, doctest

Martin Užák   
2022-03-03

---

How do you spot a

## Professional Developer ?

* Clothes?
* Years of experience?
* Preference for a specific OS or IDE?

NOTE: like breathing, might seem boring but of utmost importance.

----

* His code works. He's got tests as a proof thereof, i.e.
 a comprehensive test suite.

---

## Tests

* What is a test?
* What kind of tests do you know about?

----

* **Unit**
* Integration
* E2E
* **Smoke**
* Regression
* Stress
* Acceptance
* ...

---

## Tools

_In theory, there is no difference between theory and practice. But, in practice, there is._

* python3
* pytest

NOTE:


unittest, doctest - part of stdlib
nose

---

## Unit Tests 

_divide and conquer_

* Tests for smallest building blocks of SW we create
* Input/output is in our control
* Prerequisite: specification

NOTE:

OOP makes it easy to to add new classes without changing existing functions. Procedural code makes it easy to add new functions without changing existing data structures.

----

### Task
Write a function for validating a serial number (SN):

* 10 characters of total length,
* starts with 3 letters (country code) and
* contains further 7 digits (SN).

Example: **AUT1234567**

----

### Code 

```
def validate(sn: str) -> bool:
    if len(sn) != 10:
        return False

    if not sn[:3].isalpha():
        return False
    if not sn[3:].isnumeric():
        return False

    return True
```
----

### Tests (pytest)

test_sn.py

```
from sn import validate

def test_sn_validate():
    assert validate("") == False

    assert validate("ABC1234567") == True

    assert validate("ABC12345678") == False

    assert validate("AB12345678") == False

    assert validate("ABCD123456") == False
```

pytest test_sn.py

NOTE:

Start with trivial example: def test_validate(): ...

* test positive, OK input (pass)
* test negative inputs
* test edge cases

Congrats, you can write now basic unit tests in python.
    
---

## Doctests

_There must be a better way_

```
def validate(sn: str) -> bool:
    """
    Validate that `sn` is 10 characters in length, out of which the first
    three are letters and last seven are numerical.

    >>> validate("")
    False
    >>> validate("CZK1234567")
    True
    >>> validate("CZK2345678")
    False
    >>> validate("CZSK123456")
    False
    >>>
    """
    if len(sn) != 10:
        return False

    if not sn[:3].isalpha():
        return False
    if not sn[3:].isnumeric():
        return False

    return True
```
        
<small>
<code>pytest --doctest-modules sn_doc.py</code>
</small>
    

---

## Exceptions

```
def validate(sn: str) -> bool:
    """
    Validate that `sn` is 10 characters in length, out of which the first
    three are letters and last seven are numerical.

    Any validation error results in a ValueError being thrown.
    """
    if len(sn) != 10:
        raise ValueError("Length doesn't match")

    if not sn[:3].isalpha():
        raise ValueError("Invalid country code")
    if not sn[3:].isnumeric():
        raise ValueError("Invalid serial number")

    return True
```
        
----

### Unit Tests

```
from sn import validate

import pytest

def test_sn_validate_len():
    with pytest.raises(ValueError):
        assert validate("")
```

----

### Doctests 

```
def validate(sn: str) -> bool:
    """
    Validate that `sn` is 10 characters in length, out of which the first
    three are letters and last seven are numerical.

    Any validation error results in a ValueError being thrown.

    >>> validate("SVK1234567")
    True
    >>> validate("invalid")
    Traceback (most recent call last):
    ...
    ValueError: Length doesn't match
    """
    if len(sn) != 10:
        raise ValueError("Length doesn't match")

    if not sn[:3].isalpha():
        raise ValueError("Invalid country code")
    if not sn[3:].isnumeric():
        raise ValueError("Invalid serial number")
```

---

## Structuring tests

Structure your tests by:

* modules
* **classes**
* functions

NOTE:

always begin with names with `test` or `Test`

create /tests and tests_integration/ dirs and put your tests there

----

### Example

```
from sn import validate

class TestValidateSN:

    def test_len_ok(self):
        assert validate("ABC1234567") == True

    def test_len_too_short(self):
        assert validate("") == False

    def test_len_too_long(self):
        assert validate("ABC12345678") == False

    def test_alpha_nok(self):
        assert validate("AB12345678") == False

    def test_sn_nok(self):
        assert validate("ABCD123456") == False
```

<small>
This allows for: <code>pytest test_sn.py::TestValidateSN::test_len_ok</code>
</small>

NOTE:

https://github.com/uzak/pytest-zsh

---

## Integration Tests

_E pluribus unum_

* integration effort is always underestimated,
* no control over (other) components
* some remedy: patching & mocking

NOTE: cumbersome

----

### patching 

* Replacing part of the system in a way so it behaves predictably
* Works well with procedural/functional programming
* See `unittest.mock.Mock` and `@unittest.mock.patch`

----

### Example `return_value`

```
@unittest.mock.patch('time.time', return_value=1234567890)
def test_something(mock_time):
    ...
    result = code_under_test()  # uses time.time
    assert result['timestamp'] == 1234567890
```

----

### Example `side_effect`

* Powerful: your function will be called

```
from unittest.mock import patch

import pytest
import mymodule

@patch('time.time', side_effect=[1,2,3])
def test_foo(time_time):
    assert time_time() == 1
    assert time_time() == 2
    assert time_time() == 3

@patch('mymodule.myfunction', side_effect=ValueError())
def test_foo(mocked_fct):
    with pytest.raises(ValueError):
        mymodule.code_under_test()  # uses mymodule.myfunction()
```

NOTE:
* produce values from an generator
* throw an exception

---

### Pytest 
## Fixtures

* _fixed baseline so that tests execute reliably and produce consistent, repeatable, results_
* Suited for OOP
* Easy to use

NOTE:

There must be a better way

----
### Example

```
from pytest import fixture

@fixture
def user123():
    return {
        "id": 123,
        "public_name": "John Foo",
        "email": "user123@server.com",
        "avatar": "/avatars/200x200/123.png"
    }

def test_get_details(user123):
    assert user123["id"] == 123
    assert user123["public_name"] == "John Foo"
    ...

```
----

Scope (function, class, module, package, session):

```python
@fixture(scope="session")           # one for all tests
```

`yield`, do not `return` -> setup() and teardown():
```
@fixture(scope="session")
def user():
    user = create_user_in_db()      # setup for code under test
    yield user
    delete_user_in_db()             # teardown
```

NOTE:

Scope = lifecycle mgmt

---
## Test Driven Development

<div class="fragment">
Regular SW dev: Requirement -> Code -> Tests?
</div>
<div class="fragment">
TDD cycle: Requirement -> Tests -> Code
</div>


NOTE: discipline

Tests - guidelines

The basic concept of TDD is to write a failing test first, before writing any code. TDD is a cycle so that once you have your failing tests you can begin coding.

TDD gives you great confidence that each new piece of functionality you write in your code is backed by a test, which confirms how it behaves.

---

## RECAP

<img src="recap.png">

NOTE:

blue is code, blood of TDD

---
### Further Topics

* pytest test suites: markers and conftest.py,
* coverage,
* acceptance tests and BDD,
* maximizing performance: stress testing

NOTE:

If unit testing verifies that the code does exactly what the programmer expects it to do, then acceptance testing verifies that the code does what the user expects it to do.


1. Development cycle with unit and acceptance testing:
2. write failing acceptance tests.
3. write failing unit tests
4. write the code.
5. check that the unit tests still pass.
6. ensure your acceptance tests pass now.

---

## finally:

Thank you for your attention!

$SPEAKER_CONTACT


<!--
ideas: python test frameworks
hausaufgabe:  
further study
integration: assumptions -> tests
recommendations?
-->
