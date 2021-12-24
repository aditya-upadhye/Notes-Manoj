## Unit 1

**Certain steps to be followed in designing and analyzing an algorithm**
<p align="center">
<img src="https://imgur.com/AfU0478.jpg">
</p>

**Understand the problem**

**Decisions:**

**1. Computational capabilities:** Check which device can run your program (Deciding on System Requirements)
**2. Exact / Approx.  Solutions**: Examining the correctness for all legal inputs (Deciding on Input constraints)
**3. Data Structure:** Choosing the best data structure method to store data (Deciding on Data Structure Method)
**4. Algorithm design techniques:** Finding solution for the problem statement with existing algorithm techniques to create a new algo for the problem statement (Deciding on Algorithm method to be followed)

__***Algorithm + Data structure = Programs***__

**Prove Correctness:** testing to get desired output for all values. this can be tested with mathematical induction method. If Algo fails then it has to be redesign with the same decisions of data structures design technique, etc.,

**Analyze the Algorithm:** Examine the time and space complexity for the algorithm solution

**Coding:** Programming the algorithm by using some programming language. Formal verification is done for small programs. **Validity is done by testing and debugging.** **Inputs should fall within a range** and hence require no verification. Some compilers allow code optimization which can speed up a program by a constant factor whereas a better algorithm can make a difference in their running time. The analysis has to be done in various sets of inputs

--- 

`...`

**__Complexity__**
**Performance of a program:**  Performance of a program is measured based on amount of computer memory and time required to run a program
Two ways to check the performance 

Analytical method 🡪 called the Performance Analysis.<br>
Experimental method 🡪  called the Performance Measurement

**__Performance Analysis__ estimates space and time complexity in advance,**
**while __Performance Measurement__ measures the space and time taken in actual runs**

`...`

**Space Complexity:**
The amount of memory it needs to run to completion.

**Reason for estimating space complexity before execution**
1. Sometimes program may consume more memory than the available memory. this may leads to insufficient error or system crash or severe damage to the system
2. In multiple user system, the programs should be lesser size. If less memory is used for a single program then many multiple users can use that software at a time.

Space Complexity is **Sum of Instruction Space, Data Space, and Environment Space**

**Instruction Space** is the sum of **Source Code Size, Compiled File Size, Executable File Size**

**The instruction space depends on the following factors:**
> **Compiler used** – Some compiler generate optimized code which occupies less space.

> **Compiler options** – Optimization options may be set in the compiler options.

> **Target computer** – The executable code produced by the compiler is dependent on the processor used.

`...`

**Data Space** is the sum of  **constants, simple variables, arrays, structures and other data structures will account for the data space.**

**The Data space depends on the following factors:**
> **Structure size** – It is the sum of the size of component variables of the structure.

> **Array size** – Total size of the array is the product of the size of the data type and the number of array locations.

`...`

**Environment Space** is the data used to store the information to resume the paused program. If processes shifts to another function. It will store some information to resume the partially completed functions.
**The environment stack space depends on the following factors:**
> Return address

> Values of all local variables and formal parameters

`...`

**Space complexity S(P) = c + Sp**
> **c**    - Fixed space or constant space

> **Sp** - Variable space

**Fixed space** - The space occupied by the instruction space, simple variables and constants.

**Variable space** – The dynamically allocated space to the various data structures and the environment stack space varies according to the input from the user.

`...`

**Constant Space Complexity**: If any algorithm requires a fixed amount of space for all input values then that space complexity is said to be Constant Space Complexity

**Linear Space Complexity:** the amount of memory depends on the input value of 'n'. This space complexity is said to be Linear Space Complexity

__**Time complexity:**__
Time complexity of the program is defined as the amount of computer time it needs to run to completion

**Reason for estimating time complexity before execution**
1) If the time complexity is estimated before execution then the time complexity is measured beforehand. Further improvement in performance will be done after estimation. No need to wait for complete program execution
2) It will help to specify upper limit time to monitor timeout and to prevent from infinite loop

`...`

**The time complexity of the program depends on the following factors:**
> **Compiler used** – some compilers produce optimized code which consumes less time to get executed.

> **Compiler options** – The optimization options can be set in the options of the compiler.

> **Target computer** – The speed of the computer or the number of instructions executed per second differs from one computer to another.

**Compile time** – The time taken for the compilation of the program to produce the **intermediate object code** or the compiler version of the program.  The compilation time is taken only once as it is enough if the program is compiled once.  If optimized code is to be generated, then the compilation time will be higher.

**Run time or Execution time** - The time taken for the execution of the program.  The optimized code will take less time to get executed. 

**Time complexity T(P) = c + Tp**
> **c**   - Compile time

> **Tp** - Run time or execution time
