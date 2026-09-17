# Password Generator

A simple command-line password generator written in Python.

This project was created as a learning project to practice Python fundamentals, functions, loops, input validation, and the secrets module.

# Features
* Generate passwords from 12 to 40 characters
* Choose whether to use:
  * Letters
  * Digits
  * Special characters
* Input validation for ``` Y/N ``` answers
* Prevents generating a password when no character types are selected
* Uses Python's ``` secrets ``` module for random password generation  
# Requirements
* Python 3.x

No external packages are required.

# Installation

Clone the repository:  

git clone https://github.com/zxcresp/password-generator.git

cd password-generator  

Run the program:

python password_generator.py

# Usage

When the program starts, it asks for the desired password length:  


Enter the password length: 30  


The allowed length is **12–40 characters.**  


Then choose which character types to include:  

```
Do you want the digits? (Y/N): y
Do you want the special characters? (Y/N): y
Do you want the letters? (Y/N): y
```

The program then generates the password:


vt*Lp3!%_rXr[xxc!|8jKq?A0p3nkS

If no character type is selected, the program asks for the settings again:

At least one character type must be selected

# Functions  
```get_length()```  
  
   Gets and validates the requested password length.

```get_digits()```  

  Asks whether digits should be included and returns True or False.

```get_specials()```  

  Asks whether special characters should be included.
  
```get_letters()```

  Asks whether letters should be included.

```create_chars()```  
 
  Builds the character pool based on the user's choices.


# It uses:

* string.ascii_letters
* string.digits
* string.punctuation
* generate_password()

# Generates the password using:

secrets.choice()

The ```secrets``` module is used instead of ```random``` because it is designed for security-sensitive random generation.

# What I Practiced

This project helped me practice:

* Variables and data types
* Functions
* Function parameters and return values
* if statements
* while loops
* for loops
* break and continue
* Boolean values
* String manipulation
* Input validation
* Python modules
* Basic secure random generation
* Debugging and reading tracebacks
* Future Improvements

***This project is intended for educational purposes and personal use.***
