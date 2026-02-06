# Building the Beta

## q0.py Goal Program
 - fibonacci

```
    1. LD R3
    2. 
    3. BZ R5 7
    4. SUBC R3 1 R5
    5. MUL R3 R5 R5
    6. JMP 3
    7. ST R5
```

Instruction Set Architecture:
- **Load and Store** 
- **Arithemtic**
- **Control Flow**

Notice the types of instructions we have:

How does PC change through execution?

How does R4 change through execution?

What is the final value stored in memory?

## q1.py Register File

<img src="../outputs/lec5/q1.svg">

## q2.py 2-Register ALU operations, signals, encoding

- `draw_beta_processor()`

<img src="../outputs/lec5/q2.svg">

- fill in control FSM-- given this class of opcode, what should ALUFN, WERF be?
- fill in the instruction `ADD(r1,r2,r3)`


## q3.py Register and Constant ALU operation, signals, encoding

- `draw_beta_processor(mode="opc")`
    - this must draw an additional BSEL mux

<img src="../outputs/lec5/q2.svg">

- fill in control FSM-- given this class of opcode, what should ALUFN, WERF, BSEL be?
- fill in the instruction `ADDC(r1,-3,r3)`

## q4.py Instruction Memory
 - Given the following view of instruction memory, find and highlight all the ADDC instructions.
 - Find and highlight all the LD instructions.


## q5.py Data Memory
 - The unit of memory is the **word**
 - Memory is connected to CPU via a BUS
 - RAM internals--
 - memory is byte addressable.
    - given byte address, pull out the word at that address

- let's say a word is one byte, what data will be on the bus given the input address?
- if a word is two bytes, which direction should we read for the additional byte?
    - little-endian:
    - big-endian:


## q5.py LD operation

- `draw_beta_processor(mode="opc+ld")`
    - this must draw an additional BSEL mux
    - this must include WDSEL

<img src="../outputs/lec5/q2.svg">

- fill in control FSM-- given this class of opcode, what should ALUFN, WERF, BSEL, MOE, MWE, WDSEL be?
- fill in the instruction `LD(r1,-3,r3)`

## q6.py ST operation

- `draw_beta_processor(mode="opc+ld+st")`
    - this must draw an additional BSEL mux
    - this must include WDSEL
    - this must include RASEL 

<img src="../outputs/lec5/q2.svg">

- fill in control FSM-- given this class of opcode, what should ALUFN, WERF, BSEL, MOE, MWE, WDSEL, RA2SEL be?
- fill in the instruction `ST(r1,-3,r3)`

## q7.py JMP operation

- `draw_beta_processor(mode="opc+ld+st+branch")`
    - this must draw an additional BSEL mux
    - this must include WDSEL
    - this must include PCSEL operation

<img src="../outputs/lec5/q2.svg">

- fill in control FSM-- given this class of opcode, what should ALUFN, WERF, BSEL, MOE, MWE, WDSEL,RA2SEL, PCSEL be?

- fill in the instruction `JMP(r5,r2)`


## q8.py Branch Operation

- fill in the instruction `BZ(r1,-3,r3)`


