# Jade Compiler Quick Reference
## welcome to Jade!

JADE is a programming language that will support math expressions (arithmetic, logical and relational),  statements (assignment, cycles, conditions, read, write), modules, arrays and object oriented programming. Below are representative examples that allow you to see the main functionalities and syntax of the program.

## Basic structure

1. Create a .ja extension file
2. Base structure consist in program __nameofprogram__
3. Inside base structure you can do the following:
    1. Declare variables
    2. Declare functions
    3. Assign values to variables
    4. Conditions
    5. Loops
    6. Class declaration
    7. Input and Output
4. It is mandatory to declare main scope as shown in the example below

```
program jade {
    main {

    }
}
``` 

## Types of variables

* INT
* FLOAT
* BOOL

## Variable declaration
The nomenclature to declare variables is the following, remember to always specify your variable type!

* Remember you can declare variables in your global scope or local scopes (main & functions)

```
program jade {
    var int ex1;
    var float ex2;
    var bool ex3;

    main {
        var int ja1;
        var float ja2;
        var bool ja3;
    }
}
``` 

## Variable value assignation
Now we know how to declare variables, now let's see how to give a value to our variables...

* Remember to assign the appropiate values according to the variable type!

```
program jade {
    var int ex1;
    var float ex2;
    var bool ex3;

    assign ex1 = 2;
    assign ex2 = 7.8;
    assign ex3 = True;

    main {
        var int ja1;
        var float ja2;
        var bool ja3;

        assign ja1 = 7;
        assign ja2 = 8.8;
        assign ja3 = False;
    }
}
``` 

## Conditionals

## For loops

## While loops

## Function declaration

## Function calls

## Arrays