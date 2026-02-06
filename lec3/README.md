## q1.py Sequential Logic

Now, we must consider how can we "remember" or store information in our circuitry. Computation is great! But to truly make a computer, we must also have **stateful circuits** or circuits with "memory"!

In order to represent stateful circuits, we will create circuits with feedback loops.

Inspect the circuit below. 

Consider the labeled signal 0. What is the value on all other wires in the circuit?

<img src="../outputs/lec3/q1.svg"/>

Building off such "feedback" loops we can create stable storage.

## q2.py D-Latch Truth Table

Create a feedback loop, draw a wire connecting Q to Q' in the schematic below. This is a D-Latch.

Note, that we have labeled the "select bit" of the mux "WE". "WE" stands for write-enable. Does this make sense?

Now, fill out the truth table accordingly.

<img src="../outputs/lec3/q2.svg"/>

We will represent the mux with feedback loop as the module "D-Latch" with inputs D and WE, and output Q.

1. Which signal is the input data to write to the storage?
2. Which signal is the stored data value?

## q3.py Flip Flop - Draw the Waveform

The next question is a bit tricky. You may have noticed from the previous sections that circuits are timing dependent! We must carefully consider, how long does some particular output take to calculate.

In turn, enabling data to be stored, and then knowing when to read said data is also a question of timing. When is a d-latch taking in new inputs? Anytime WE is enabled! When is a d-latch emitting a new stable, output? After WE is flipped, the duration of the tpd of a mux.

Building circuits around this timing consideration can be troublesome. Instead, we find in practice, it is better to have **clocked storage**. Modern circuits have access to an oscillating clock signal. What if we could take in new inputs on the rising edge of a clock instead? Then, we can read stable values from our storage at any clock high?

Investigate the implementation of the flip flop below and complete the missing waveforms given the CLK and input data.


<img src="../outputs/lec3/q3.svg"/>


## q4.py FSM -- Binary Combination Lock

<img src="../outputs/lec3/q4.svg"/>
