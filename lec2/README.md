## q1.py SOP Expression

## q2.py Logic Gates and Truth Tables

A fundamental computer of computer circuitry is the logic gate. Logic gates take in two signals (HIGH/LOW voltages) and output a HIGH or LOW signal in turn.

In this section, we will see how we can combine this gates to do complicated functions, like adding, storage, etc, and build up to a complete CPU (computer brain!).

Below, we have:

1. AND (produces a 1 if A and B are 1. Otherwise 0)
2. OR (produces a 1 if either A and B, or both, are 1. Otherwise 0.)
3. XOR (produces a 1 if either, but not both, A and B are 1. Otherwise 0.)
4. NAND (not and) (produces a 1 if A and B are 0. Otherwise 1)
5. NOR (not or) (produces a 0 if either A and B, or both, are 1. Otherwise 1.)
6. NOT XOR (produces a 0 if either, but not both, A and B are 1. Otherwise 1.)

The final gate takes is one input, and produces one output.

7. Inverter (not) (if A is 1, produces 0. Otherwise 1.)

We can represent logical statements as truth tables. 

On the left side of the bolded truth table line, fill in all the possible input values for A and B.
- done effectively, this will look like counting in binary: A=0,B=0 (00), A=0,B=1 (01), A=1... 
On the right side of the bolded line, fill in the output given the corresponding A and B values.

<img src="../outputs/lec2/q2.svg"/>

## q3.py Truth Table, SOP, Draw the circuit

Now, any logic table can be expressed as a "sum of products expression (SOP)". In turn, any SOP expression can be represented in circuitry! Thus, any truth table can be turned into a circuit.

For a given truth table, inspect each row. Say, that row 1, row 3, and row 4 output TRUE (1). 

Effectively, the entire truth table can be described as:

output = (condition for row 1) OR (condition for row 3) OR (condition for row 4)

Then, each condition is simply the AND of each variable. For example if we have A=1,B=0,C=1, we can describe that condition as

$$A\bar{B}C$$

Note, that OR is often represented by addition: $+$, AND is represented via multiplication $\cdot$, and NOT is often represented by a bar $\bar{A}$.

<img src="../outputs/lec2/q3.svg"/>

## q4.py Timing Delays

Now, circuits are real-world components. Like all real-world processes, they take time to run and compute!

How long? Each circuit module has a timing specification described in two parts:

Tpd is the **propagation delay** which means the time it takes from giving input to getting correct output.

Tcd is the **contamination delay** which means the time it takes from giving input to getting some incorrect (contaminated) reading.

Effectively, when building a circuit and combining modules, after giving new input, after the contamination delay elapses we do not want to read from the output until the propagation delay has passed.

1. To calculate Tpd, find the longest path of summed Tpds of each component, along the path form input->output.
2. To calculate Tcd, find the shortest path of summed Tcds of each component, along the path form input->output.

<img src="../outputs/lec2/q4.svg"/>


## q5.py Control circuits-- MUX Truth Table, Implementation

Now, a common control component that will be useful for us is known as the "multiplexer". 

A 2-way multiplexer takes in two inputs, and uses a third input, a "select bit" to indicate if we want the output to be the  0th input (S=0) or the 1st input (1st, S=1).

A n-way multiplexer takes in N inputs, and `ceil(log_2(N))` select bits to describe which of the N inputs to chose from.

<img src="../outputs/lec2/q5.svg"/>

## q6.py Full Adder

Now, remember from the last section how we did binary arithmetic. Can we represent that operation in circuitry?

First, we must break down and understand the operation between three 1-bit values, A and B and the carry-in bit (Cin). What are the possible outputs for S (the output value) and Cout (the carry out bit).

Just as before, we can represent this scenario as a truth table, then an SOP expression, and then a circuit.

<img src="../outputs/lec2/q6.svg"/>

## q7.py 4-bit full adder

Now, consider, can be combine this full-adder module into a 4-bit adder? To do so, we will build the conceptually simple (and slightly inefficient) **ripple carry adder**. This adder will work by first doing a 1-bit addition on A[0] and B[0], producing S[0] and then a carry out bit. This will be passed along to the next full adder module to calculate A[1],B[1] and so on and so forth.

<img src="../outputs/lec2/q7.svg"/>
