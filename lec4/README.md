

# q3.py - Full 4-bit Arith Unit for ADD/SUB
- V,F,N flags

<img src="../outputs/lec4/q3.svg"/>

# q1.py - mini computer for N*(N-1) and N! 
    - or A*B using adder and decrement module?
    - data path logic
    - control logic

- modules : `-1`, `*`, `?=0`, control logic
- input: N
- input: Clock
- add 2 registers, draw control logic FSM, to create N! computer

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




