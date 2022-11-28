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

## Input and Output
In every program it is important to be able to receive and provide information to feed our procedures, to receive input and print output we use the following structure in jade

```
program inputoutput{

    main{
        var int num;
        read num;
        
        print(num);
    }
}
``` 

* __READ__ to receive input
* __PRINT()__ to print output

## Conditionals
Conditionals are fundamental part of the logic of our code, jade provides the well known if, else if, else statements

```
program jade {
    var int num1;
    var int num2;
    main{
        assign num1 = 1;
        assign num2 = 30;

        if(num1 >= num2){
            print(num1);
        }else{
            print(num2);
        }
    }
}
``` 


## For loops
In jade we have __for loops__ and __while loops__ with structures that are familiar conventions from popular programming languages.

* for loops require to have a pre-declared cycle controller variable which needs to be initialized when declaring the loop followed by the int value that represents the boundarie.

```
program forloop {
    var float num2;
    assign num2 = 25.3;

    main {
        var int j;
        
        for(j = 0 : 9){
            print(num2);
        }
        
    }
}
``` 

## While loops
While loops require a condition when declaring the loop and the cycle controller variable must be updated before the cycle ends, the structure is the following

```
program whileloop {

    main {
        var int i;
        assign i = 1;
        var int cont;
        assign cont = 4; 
        

        while(i <= cont;){
            print(cont);
            assign i = i + 1;
        }
        
    }
}
```

## Function declaration and calling
Functions can have a return type or no return at all, the valid function return types are:
* INT
* FLOAT
* BOOL
* VOID -> no return type

And must be stated in the function declaration, inside the function structure several procedures can be stated, for example:
1. Declare variables
2. Declare functions
3. Assign values to variables
4. Conditions
5. Loops
6. Input and Output

```
program functions {
    var int num3;

    fun int imprimeuno(int a){
        assign num3 = 3490;
        print(num3);
        print(a);

        return num3 + a;
    }

    main {
        var int ejemplo;
        assign ejemplo = 20;
        assign ejemplo = imprimeuno(5);;
        print(ejemplo);
    }

}
```

## Arrays
Jade allows the declaration of linear structure such as arrays, the nomenclature is similar to normal variable declarations because we also use the reserved word __var__ + __array__

Things you can do with arrays:
* Assign values to each array index
* Retreive information from a determined array index

```
program findinarray {
    main {
        var array int arreglo1 = [6];
        var int i;
        var int num;
        var int prov;
        var int existe;
        assign existe = 0;

        for(i = 0 : 6){
            assign array arreglo1[i] = i;
        }

        read num;

        for(i = 0 : 6){
            assign prov = arreglo1[i];
            if(prov == num){
                assign existe = 1;
            }
        }
        print(existe);
    }  
}
```

# You can also check how to run jade in __ManualUsuario_JADE__