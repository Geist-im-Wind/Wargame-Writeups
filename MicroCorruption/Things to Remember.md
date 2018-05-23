All numbers in the debugger are base-16.

Instructions:
  * CLR - Clears value in given register
  * MOV - Makes the second argument equal the first (Mov arg1 arg2 -> arg2 = arg1)
  * ADD - Runs += on the second argument using the first (ADD arg1 arg2 -> arg2 += arg1)
  * SUB - Does the opposite of ADD
  * XOR - Checks if two values are not equal. If they are, returns 0.
  * BIS - Checks if either arg1 or arg2.
  * BIC - Clear bits in arg1 from arg2 (BIC arg1 arg2 -> arg2 &= arg1)
  * CMP - Compute arg1 - arg2, set the flags, discard result
  * BIT - computer arg1 & arg2, set the flags, and discord the results (TEST on x86)
  * PUSH - Push arg1 onto the stack; subtract 2 bytes from the sp register (r1) and store arg1 in the resulting location in memory.
  * POP - MOV @r1+, arg1; move the value located at the stack pointer into arg1, and add 2 to the stack pointer.
  * JMP - arg1 jumps to the location arg1 points to.
  * CALL - arg1 jumps to arg1, but first pushes the next address in memory to the stack
  * RET is just MOV @r1+, r0.
  * Jxx arg1 for xx are conditional jumps, which decide based on the flag bits Z (zero), N (negative), and C (carry):
    * NZ (not zero)
    * Z (zero)
    * LO (lower)
    * HS (higher or same)
    * N (negative)
    * L (less)

The current instruction at any time can be seen in the top right.
