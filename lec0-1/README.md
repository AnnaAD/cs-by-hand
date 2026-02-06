
# q2.py Binary Representations

As humans, we are used to counting in base 10, we have 10 distinct digits: 0,1,2,3,4,5,6,7,8,9.
When we parse a number, 1,431 for example, we understand this value as being 1*1000 + 4*100 + 3*10 +1. Effectively, each digit is a *weight* applied to a power of 10.

Computers, naturally, however only have access to 2 distinct values LOW (voltage) and HIGH. Thus, it is natural to represent values in **base 2** when we are talking about data in computing systems.

To work with **base 2** or **binary**, the basic same idea of weights and powers applies. However, now when we see a value 11011, we should understand this to mean 1*2^4 + 1*2^3 + 0*2^2 + 1*2^1 + 1 *2^0.

To represent a decimal value in binary, work from left to right. Take out the largest possible power of two from the decimal value, write a 1 in the corresponding digit, and continue to work until you reach the "one's place".

<img src="../outputs/lec0-1/q2-1.svg"/>

<img src="../outputs/lec0-1/q2-2.svg"/>

# q1.py - 2's Complement Circle

Now, what about negative values? 

The most common convention to represent **signed integers** in binary is 2's complement.

To represent a negative value in 2's complement:
1. Write the positive version of the number in binary
2. Flip each digit (0->1 or 1->0)
3. Add 1 in binary (remember to carry if needed!)

Doing the procedure again (starting with a negative version of the number in binary) will flip a negative value to a positive.
Notice, that positive values will always have a zero as the highest order bit, while negative values will have a 1 in the highest order bit.
As such, we call the highest order bit, the **sign bit**. Consider: To represent the value positive 4 in 2's complement, you will need 4 bits: 0100. 

Fill in the circle with the decimal value of the following 4-bit 2's complement binary around the circle.

<img src="../outputs/lec0-1/q1.svg"/>

Consider drawing arrows on the circle representing:

1. Add 4 to 1.
2. Add 2 to -1.
3. Subtract 3 from 2.
4. Subtract 3 from -1.

Notice how adding always goes clockwise around the circle and subtracting goes counter-clockwise. 2's complement representation makes binary arithmetic continuos, with no special cases for negatives, positives, etc.

Except-- consider what happens when we add 3 to 6...

This would result in **overflow** as we can not represent 9 in 4-bit 2's complement. Instead, the operation leaves us with a representation of a negative value in 4-bit 2's complement.

# q2.py Binary Representations with Negatives

Write the following signed integer in 2's complement binary.

<img src="../outputs/lec0-1/q2-3.svg"/>

<img src="../outputs/lec0-1/q2-4.svg"/>

# q3.py Binary Arithmetic

Consider we can also do arithmetic with binary values just as we can with decimal values.

However, now when we do 1+1 in a single column, we must carry a 1 (from the resulting 10), to the next column. (This is similar to how we would carry a "1" to the tens place from adding 5+5 in decimal.)

<img src="../outputs/lec0-1/q3-1.svg"/>
<img src="../outputs/lec0-1/q3-2.svg"/>


# q4.py Hex/Binary Table

Now, in computer systems it can become unwieldy and error-prone to transcribe long binary values by hand!
Furthermore, we have seen that translating from decimal->binary or vice versa requires a bit of math.

However, let's now consider **base 16** or **hexidecimal**. Why introduce a new base? 

1. Base 16, like base 10, has enough digits to be compact and easy for humans to read and write.
2. Base 16 has a nice property-- four binary digits correspond to exactly one hex digit. 
Thus, converting a binary value to hex is as simple as grouping digits into fours, and then a one-to-one translation! 

If you understand base 10 as the base for humans, and base 2 as the base for computers, base 16 is the base for programmers (the middle man so to speak)!

Complete the table below.

<img src="../outputs/lec0-1/q4.svg"/>


# q5.py Hex Representation

Complete the following binary->hex conversions or hex->binary conversions. This should be far easier than working with binary->decimal for example! 

**Hint:** Feel free to use the table you completed above.

<img src="../outputs/lec0-1/q5-1.svg"/>
<img src="../outputs/lec0-1/q5-2.svg"/>
<img src="../outputs/lec0-1/q5-3.svg"/>
<img src="../outputs/lec0-1/q5-4.svg"/>

