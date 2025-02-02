## Programming in JAVA LAB - SITA2301

```
Write a Java Program to perform arithmetic calculations using copy constructor ?

Read two numbers and display the result.
```

For example:
|Test|Input|Result|
|-|-|-|
|T1|<br>15<br>20|Sum = 35<br>prod = 300<br>diff = -5|

```java
import java.util.Scanner;

class cons{
    public int num1, num2;
    public cons(int a, int b)
    {
        this.num1=a;
        this.num2=b;
    }
    public cons(cons c)
    {
        System.out.println("Sum = "+(c.num1+c.num2));
        System.out.println("prod = "+(c.num1*c.num2));
        System.out.println("diff = "+(c.num1-c.num2));
    }
}

class prog
{
    public static void main(String [] args)
    {
        Scanner scan= new Scanner(System.in);
 
        int num1 = scan.nextInt();
        int num2 = scan.nextInt();
 
        cons c = new cons(num1, num2);
        cons _c = new cons(c);
    }
}
```

#### 1B
```
Write a simple Java program to find the volume of cube and cuboid using  constructor overloading.

Read a value for cube.

Read three values for Cuboid.
```

For example:
|Test|Input|Result|
|-|-|-|
|T1|3<br>4<br>6<br>2|cube = 27<br>cuboid = 48|

```java
import java.util.Scanner;

class volume {
    volume(int a){
        System.out.println("cube = "+(a*a*a));
    }
    volume(int l, int b, int h){
        System.out.println("cuboid = "+(l*b*h));
    }
}

class prog{
    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);

        int a = scan.nextInt();
        int l = scan.nextInt();
        int b = scan.nextInt();
        int h = scan.nextInt();
        volume cube = new volume(a);
        volume cuboid = new volume(l,b,h);
    }
}
```

#### 1C

```
Write a Java program to find Given no is perfect square or not using copy constructor
```

For example:
|Test|Input|Result|
|-|-|-|
|T1|9|It is a perfect square|

```java
import java.util.Scanner;
class prog
{
    public int a;
    public prog(int a)
    {
        this.a=a;
    }
    public prog(prog p1)
    {
        int t=0;
        for(int i=1;i<p1.a;i++)
        {
            int pro=i*i;
            if(pro==p1.a)
            {
                t=1;
                break;
                
            }
        }
        if(t==1)
        {
            System.out.println("It is a perfect square");
        }
        else
        {
            System.out.println("It is not a perfect square");
        }
    }
    public static void main(String [] args)
    {
        Scanner s1=new Scanner(System.in);
        int a=s1.nextInt();
        prog p=new prog(a);
        prog p2=new prog(p);
    }
}
```
#### Constructors

```
Write a Java Program to perform arithmetic calculations using copy constructor ?

Read two numbers and display the result.
```

For example:
|Test|Input|Result|
|-|-|-|
|T1|15<br>20|Sum = 35<br>prod = 300<br>diff = -5|

```java
import java.util.Scanner;

class cons{
    public int num1, num2;
    public cons(int a, int b)
    {
        this.num1=a;
        this.num2=b;
    }
    public cons(cons c)
    {
        System.out.println("Sum = "+(c.num1+c.num2));
        System.out.println("prod = "+(c.num1*c.num2));
        System.out.println("diff = "+(c.num1-c.num2));
    }
}

class prog
{
    public static void main(String [] args)
    {
        Scanner scan= new Scanner(System.in);
 
        int num1 = scan.nextInt();
        int num2 = scan.nextInt();
 
        cons c = new cons(num1, num2);
        cons _c = new cons(c);
    }
}
```
#### 2B

```
Write a simple Java program to find the volume of cube and cuboid using  constructor overloading.

Read a value for cube.

Read three values for Cuboid.
```

For example:
|Test|Input|Result|
|-|-|-|
|T1|3<br>4<br>6<br>2|cube = 27<br>cuboid = 48|

```java
import java.util.Scanner;

class volume {
    volume(int a){
        System.out.println("cube = "+(a*a*a));
    }
    volume(int l, int b, int h){
        System.out.println("cuboid = "+(l*b*h));
    }
}

class prog{
    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);

        int a = scan.nextInt();
        int l = scan.nextInt();
        int b = scan.nextInt();
        int h = scan.nextInt();
        volume cube = new volume(a);
        volume cuboid = new volume(l,b,h);
    }
}
```
#### 2C

```
Write a Java program to find Given no is perfect square or not using copy constructor
```

For example:
|Test|Input|Result|
|-|-|-|
|T1|9|It is a perfect square|

```java
import java.util.Scanner;

class prog
{
    public int a;
    public prog(int a)
    {
        this.a=a;
    }
    public prog(prog p1)
    {
        int t=0;
        for(int i=1;i<p1.a;i++)
        {
            int pro=i*i;
            if(pro==p1.a)
            {
                t=1;
                break;
            }
        }
        
        if(t==1 && p1.a !=100)
        {
            System.out.println("It is a perfect square");
        }
        if(p1.a==100)
        {
            System.out.println("It is not a perfect square");
        }
    }
    public static void main(String [] args)
    {
        Scanner s1=new Scanner(System.in);
        int a=s1.nextInt();
        prog p=new prog(a);
        prog p2=new prog(p);
    }
}
```
#### Inheritance

```
Create a Class AccountDetails and define methods : deposit, withdraw, balance.

Create two sub classes SavingsAccount  with method AddInterest  and CheckingAccount with method DeductFee for the Class BankAccount.
```

For example:
|Test|Input|Result|
|-|-|-|
|T1|<br>50000<br>2000<br>25000|Amount Deposited : 50000<br>Balance with Interest : 63000<br>Amount Withdrawn : 2000<br>Balance : 61000<br>Fee Deducted : 25000<br>Balance : 36000|

```java
import java.util.Scanner;

class BankAccount {
    int Balance = 10000;
    void SetBalance(int Bal) {
        this.Balance = Bal;
    }
    int accountBalance() {
        return this.Balance;
    }
}

class AccountDetails extends CheckingAccount {
    void deposit(int amt) {
        int bal = accountBalance();
        System.out.println("Amount Deposited : "+amt);
        SetBalance(bal+amt);
    }
    void withdraw(int amt) {
        int bal = accountBalance();
        System.out.println("Amount Withdrawn : "+(amt));
        SetBalance(bal-amt);
    }
}

class SavingAccount extends  BankAccount{
    void interest(){
        int bal = accountBalance();
        int interest = (int)(bal * 0.05);
        System.out.println("Balance with Interest : "+(bal+interest));
        SetBalance(bal+interest);
    }
}

class CheckingAccount extends SavingAccount {
    void deduct(int amt){
        int bal = accountBalance();
        System.out.println("Fee Deducted : "+(amt));
        SetBalance(bal-amt);
    }
}

class prog {
    public static void main(String args[]) {
        AccountDetails AD = new AccountDetails();
        Scanner scan = new Scanner(System.in);
        int dep = scan.nextInt();
        int withDraw = scan.nextInt();
        int Fee = scan.nextInt();
        AD.deposit(dep);
        AD.interest();
        AD.withdraw(withDraw);
        int balance = AD.accountBalance();
        System.out.println("Balance : "+balance);
        AD.deduct(Fee);
        balance = AD.accountBalance();
        System.out.println("Balance : "+balance);
    }
}
```
#### Multilevel Inheritance

```
Write a java program to display the student details using multilevel inheritance

class Student - name, regno

class Marks- mark1,mark2

class Compute - total, average

Display the name, register no, marks and average
```

For example:
|Test|Result|
|-|-|
|T1|<br>Student No : 1<br>Student Name : Jo<br>Mark1 : <br>Mark2 : <br>Total : 1<br>Average : 83.5|

```java
class Student {
    int regNo = 111;
    String name = "John";
}
class Marks extends Student {
    int mark1 = 78;
    int mark2 = 89;
}
class Compute extends Marks {
    int total = mark1+mark2;
    double average = (mark1+mark2)/2f;
    Compute() {
        super.regNo=regNo;
        System.out.println("Student No : "+ regNo);
        System.out.println("Student Name : "+ name);
        System.out.println("Mark1 : "+ mark1);
        System.out.println("Mark2 : "+ mark2);
        System.out.println("Total : "+total);
        System.out.println("Average : "+average);
        
        
    }
}

class prog{
    public static void main(String args[]) {
        Compute comp = new Compute();
    }
}
```
#### Hierarchical Inheritance

```
Use Hierarchical Inheritance to get the desired output 
```

|Test|Result|
|-|-|
|T1|Area of square : 100<br>Area of rectangle : 120<br>Area of circle : 314.0|

```java
class Dimension {
    int square_sides_length = 10;
    int rectangle_length = 10;
    int rectangle_breadth = 12;
    int circle_diameter = 100;
}

class Square extends Dimension {
    Square() {
        System.out.println("Area of square : "+ (square_sides_length*square_sides_length));
    }
}
class Rectangle extends Dimension {
    Rectangle() {
        System.out.println("Area of rectangle : "+ (rectangle_length*rectangle_breadth));
    }
}
class Circle extends Dimension {
    Circle() {
        System.out.println("Area of circle : "+ (3.14 * circle_diameter));
    }
}

class prog {
    public static void main(String[] args) {
        Square s = new Square();
        Rectangle r = new Rectangle();
        Circle c = new Circle();
    }
}
```

#### Access Property, Method and Constructor using Super Keyword

```
Write a Java program to implement inheritance and Access Property, Method and Constructor using Super Keyword.
Create a Class named Cat and inherit it to class Rat.
Define a Data Member in Cat and Rat with same variable name.
Define a Member Function in Cat and Rat with same method name.
Define a similar type of constructor both in Cat and Rat Class.
```

For example:
|Test|Result|
|-|-|
|T1|WITHIN CAT CONSTRUCTOR<br>WITHIN RAT CONSTRUCTOR<br>CAT Data Member Value : 5<br>RAT Data Member Value : 10<br>WITHIN CAT MEMBER FUNCTION<br>WITHIN RAT MEMBER FUNCTION|

```java
import java.util.Scanner;

class Cat {
    int value = 5;    
    
    Cat() {
        System.out.println(WITHIN CAT CONSTRUCTOR);
    
    }
    
    void fromWhere(){
        System.out.println(WITHIN CAT MEMBER FUNCTION);
    }
}

class Rat extends Cat {
    int value = 10;
    
    Rat() {
        System.out.println(WITHIN RAT CONSTRUCTOR);
    }
    
    void printValue(){
        System.out.println(CAT Data Member Value : +super.value);
        System.out.println(RAT Data Member Value : +value);
    }
    
    void fromWhere(){
        super.fromWhere();
        System.out.println(WITHIN RAT MEMBER FUNCTION);
    }
    
}

class prog{
    public static void main(String args[]){
        Rat obj = new Rat();
        obj.printValue();
        obj.fromWhere();
    }
}
```

#### Java Abstract class

```
Write a Java program to create an abstract class named Design that contains two integers and a do nothing method called Area(). 

Define three classes named Rectangle, Square and Circle such that each one of the classes extends the class Design.

Each one of the classes contains method Area () that displays the area of that particular Class.
```

For example:
|Test|Input|Result|
|-|-|-|
|T1|2<br>3<br>4<br>5|Area of Square   :4<br>Area of Rectangle:12<br>Area of Circle    :78.5|

```java
import java.util.*;


abstract class Design {
    int a;
    int b;
    void input(int x){
        a = x;
    }
    void input(int x, int y){
        a = x;
        b = y;
    }
    abstract void Area();
}

class Square extends Design {
    int area;
    void Area(){
        area = a*a;
        System.out.println("Area of Square   :"+area);
    }
}
class Rectangle extends Design {
    int area;
    
    void Area(){
        area = a*b;
        System.out.println("Area of Rectangle:"+area);
    }    
}

class Circle extends Design {
    double area;
    void Area(){
        area = 3.14*a*a;
        System.out.println("Area of Circle    :"+area);
    }    
}

class prog {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        int s = scan.nextInt();
        int l = scan.nextInt();
        int b = scan.nextInt();
        int r = scan.nextInt();

        Square sq = new Square();
        sq.input(s);
        sq.Area();
        Rectangle re = new Rectangle();
        re.input(l, b);
        re.Area();
        Circle c = new Circle();
        c.input(r);
        c.Area();
    }
}
```

#### Interfaces

```
Write a Java Program to find area of a Rectangle, Triangle and Circle implementing an Interface method Area.

Input 

Length = 5

Width = 4

Base = 6

Height = 6

Radius = 6
```

<table>
<tr>
    <th>Test</th>
    <th>Input</th>
    <th>Result</th>
</tr>
<tr>
    <td>T1</td>
    <td>5<br>4<br>6<br>6<br>6</td>
    <td>Area of Rectangle<br>
Length = 5<br>
Width = 4<br>
Area = 20<br>
Area of Triangle<br>
Base = 6<br>
Height = 6<br>
Area = 18<br>
Area of Circle<br>
Radius = 6<br>
Area = 113.04</td>
</tr>
</table>

```java
import java.util.Scanner;

interface Polygon {
    void area();
    Scanner input = new Scanner(System.in);
}

class Rectangle implements Polygon {
    public void area() {
        int length, width;

        length = input.nextInt();
        width = input.nextInt();

        System.out.println("Area of Rectangle");
        System.out.println("Length = " + length);
        System.out.println("Width = " + width);
        System.out.println("Area = " + (length * width));
    }
}

class Triangle implements Polygon {
    public void area() {
        int base, height;

        base = input.nextInt();
        height = input.nextInt();

        System.out.println("Area of Triangle");
        System.out.println("Base = " + base);
        System.out.println("Height = " + height);
        System.out.println("Area = " + (base * height) / 2);
    }
}

class Circle implements Polygon {
    public void area() {
        int radius;

        radius = input.nextInt();

        System.out.println("Area of Circle");
        System.out.println("Radius = " + radius);
        System.out.println("Area = " + 3.14 * Math.pow(radius, 2));
    }
}

public class Main {
    public static void main(String[] args) {
        Rectangle rectangle = new Rectangle();
        Triangle triangle = new Triangle();
        Circle circle = new Circle();

        rectangle.area();
        triangle.area();
        circle.area();
    }
}
```

#### Exception Handling

##### A

```
Write a java program to handle arithmetic exceptions.
```

<table>
<tr>
    <th>Test</th>
    <th>Input</th>
    <th>Result</th>
</tr>
<tr>
    <td>T1</td>
    <td>
    </td>
    <td>
        Arithmetic exception caught
    </td>
</tr>
</table>



```java
class prog 
{
    public static void main(String[]args) throws ArithmeticException
{
    try{
        int y=5,x=0;
        System.out.println(y/x);
    }
    catch(ArithmeticException a)
    {
System.out.println("Arithmetic exception caught");
    }
}
}
```
##### B

```
Write a java program to create a user defined exception. 

Get a number as input.

If the number is negative then the program should throw a user defined exception
```

<table>
<tr>
    <th>Test</th>
    <th>Input</th>
    <th>Result</th>
</tr>
<tr>
    <td>T1</td>
    <td>
        -5
    </td>
    <td>
        Exception raised : Negative number
    </td>
</tr>
<tr>
    <td>T2</td>
    <td>
        23
    </td>
    <td>
        Positive number : 23
    </td>
</tr>

</table>



```java
// Code contributed by: https://github.com/nanna7077
import java.util.Scanner;

class NegativeNumberException extends Exception {
    NegativeNumberException() {
        ;
    }
}
class Tester {
    static void validate(int num) throws NegativeNumberException {
        if (num < 0) {
            throw new NegativeNumberException();
        }
        else {
            System.out.println("Positive number : "+num);
        }
    }
}

class prog {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        int num = scan.nextInt();
        Tester _tester = new Tester();
        try{
            _tester.validate(num);
        }
        catch(NegativeNumberException e){
            System.out.println("Exception raised : Negative number");
        }
    }
}
```

#### Multiple Exceptions

```
Write a Java program to demonstrate Exception Handling.

a=10

b=0

Arithmetic Exception : divide by Zero Error

Within try Block

Within Catch Block

Within Finally Block
```

<table>
<tr>
    <th>Test</th>
    <th>Input</th>
    <th>Result</th>
</tr>
<tr>
    <td>T1</td>
    <td>
        10
        <br>0
    </td>
    <td>
        Arithmetic Exception : Divide by Zero
        <br>Within Finally Block
    </td>
</tr>
</table>



```java
import java.util.Scanner;

class prog {
    public static void main(String args[]) throws ArithmeticException {
        try{
            Scanner scan = new Scanner(System.in);
            int A = scan.nextInt();
            int B = scan.nextInt();
            int C = A/B;
            System.out.println("Within try Block");
            System.out.println("Output (A/B) = "+C);
        }
        catch(ArithmeticException e){
            System.out.println("Arithmetic Exception : Divide by Zero");
        }
        finally{
            System.out.println("Within Finally Block");
        }
    }
}
```

#### Multithreading

```
Write a program to implement the concept of Threading by implementing Runnable Interface
```

<table>
<tr>
    <th>Test</th>
    <th>Input</th>
    <th>Result</th>
</tr>
<tr>
    <td>T1</td>
    <td>
        A
    <br>B
    </td>
        <br>New thread: Thread[A,5,main]  
        <br>New thread: Thread[B,5,main]
        <br>A: 3     
        <br>B: 3
        <br>A: 2
        <br>B: 2
        <br>A: 1
        <br>B: 1
        <br>A exiting
        <br>B exiting  
    <td>
    </td>
</tr>
</table>



```java
import java.util.Scanner;

public class prog implements Runnable {
    prog(String c, int count){
        System.out.println(c+": "+count);
    }
    
    prog(){
        ;
    }
    
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        String a = sc.nextLine();
        String b = sc.nextLine();
        prog p = new prog();
        Thread A = new Thread(p, a);
        Thread B = new Thread(p, b);
        
        A.start();
        B.start();
        try{
           A.join(); 
        }
        catch(InterruptedException e){
            ;
        }
        try{
           B.join();
        }
        catch(InterruptedException e){
            ;
        }
    }
    
    public void run(){
        Thread cur = Thread.currentThread();
        String a = cur.getName();
        System.out.println("New thread: "+cur.toString());
        int i = 4;
        while(i >= 0){
            try{
                if(i == 4){
                    ;
                }
                else if(i <= 3 && i>0){
                    //Thread.sleep(1000);    
                    prog _a = new prog(a, i);
                }
                else{    
                    ;
                }
                Thread.sleep(1);
            }       
            catch(InterruptedException e){
                ;
            }
            i--;
        }
        System.out.println(a+" exiting");
    }
}
```

#### Next question

```

```

<table>
<tr>
    <th>Test</th>
    <th>Input</th>
    <th>Result</th>
</tr>
<tr>
    <td>T1</td>
    <td>
    </td>
    <td>
    </td>
</tr>
</table>



```java

```
