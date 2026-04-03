Now we will start to build up to constructing a full mini computer processor that can perform 2 operations: addition and subtraction.

# q3.py - Full 4-bit Arith Unit for ADD/SUB

Remember the 4-bit full adder you implemented in lec2.q7? 
We want to expand the logic of the 4-bit adder to be a full "arith" unit.

This unit should use the 4-bit adder to perform addition, if the ALU bit is 0. 
The unit should use the 4-bit adder to preform 2's-complement subtraction if the ALU bit is 1.

Eventually, we will also want to use this arith unit to perform comparison, for example.
To do so, we will also compute 3 1-bit outputs, called "flag" bits.

- The "Z" flag should be 1 if your four-bit output is equal to 0000.
- The "N" flag should be 1 if your four-bit output is negative in 2's complement.
- The "V" flag should be 1 if overflow occured. 

The logic for this is equivalent to:
$$V = XA_{3} * XB_{3} * \overline{S_{3}} + \overline{XA_{3}} * \overline{XB_{3}} * S_{3}$$

Consider, how can we use SUB and this Z bit to check if two values are equal? _______________

Complete the implementation of the 4-bit arith unit below.

<img src="../outputs/lec4/q3.svg"/>

# q1.py - mini computer for N! 

Let's create a mini computer that can compute $N!$.

To complete this task you will be creating two things:


- **The Data path**-- wires, muxes, registers, etc. that combine to move the data of our computation from our two computation modules (multiplication and -1).
- **The Control path** -- when should our computation stop? To do this, you can compute a control signal as input to our control logic module. This control logic module can implement a finite state machine and output any needed *control signals*, which our circuit can use as input.
    - Consider, that the registers' write enable signals should likely be output of our control logic.


Complete the circuit by adding wires, registers, and control logic description.

<img src="../outputs/lec4/q1.svg"/>


# q2.py - mini general purpose 4-bit computer w/ instruction memory? (zero/add)?

- Fetch, Decode, Execute
- 1 register
- Arith Unit
- Program Counter
- Instruction Memory
- CLK

```
ZERO
ADD 0
ADD 3
ADD -3
```
<img src="../outputs/lec4/q2.svg"/>

- Draw the wires to compelte the mini-computer
- Highlight the "control path", highlight the "data" path.
- What must CLK cycle be set to?

# q4.py - add subtraction operation?

- 1 register
- Arith Unit w/ subtraction logic, new control signal for ALUFN
- Program Counter

```
ZERO
ADD 0
ADD 3
SUB 2
ADD -3
```

<img src="../outputs/lec4/q2.svg"/>





