# Building the Beta

## q0.py Goal Program
 - fibonacci

```
    1. LD R3
    2. 
    3. BZ R4 
    4. SUBC R3 1
    5. MUL R3 R3 R3
    6. ST
```

Notice the types of instructions we have:

How does PC change through execution?

How does R4 change through execution?

What is the final value stored in memory?

## q1.py Register File

<img src="../outputs/lec5/q1.svg">

## q1.py 2-Register ALU operations, signals, encoding

- `draw_beta_processor()`

<img src="../outputs/lec5/q2.svg">

- fill in control FSM-- given this class of opcode, what should ALUFN, WERF be?
- fill in the instruction `ADD(r1,r2,r3)`


## q3.py Register and Constant ALU operation, signals, encoding

- `draw_beta_processor(mode="opc")`
    - this must draw an additional rasel mux

<img src="../outputs/lec5/q2.svg">

- fill in control FSM-- given this class of opcode, what should ALUFN, WERF, RASEL be?
- fill in the instruction `ADDC(r1,-3,r3)`

## q4.py Instruction Memory
 - Given the following view of instruction memory, find and highlight all the ADDC instructions.
 - Find and highlight all the LD instructions.

## q5.py LD/ST operation

- 

## q6.py BZ operation


