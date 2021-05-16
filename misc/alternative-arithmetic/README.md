# Alternative Arithmetic (Intermediate Flag)
## Misc - Medium
| author | prereq chals | first blood | solves | final points |
| --- | --- | --- | --- | --- |
| k3v1n | none | **st98** from **Team zer0pts** | 28 | 259 |

### prompt
Java has provided an alternative mathematical system.

Connect via: `nc java.sdc.tf 1337`

**attachments**: `None, don't give out the source code`
### original specification
Make a Java program that asks the participant to complete a series of challenges before giving the flag:
1. Find a nonzero int x such that x == -x. (Correct answer: Integer.MIN_VALUE)
2. Find 2 different long's l and m such that Long.hashCode(l) == Long.hashCode(m).
3. Find a value t of any numerical type such that incrementing t++ (no matter how many times) has no effect on the value. (Correct answer: any large float number)
- Note maybe add a twist by making an array of 256 values {1337, 1338, 1339, ...} and use a for loop to index the array using array[(byte)(t++)] and expect that the result is all 1337.

**flag**: `sdctf{JAVA_Ar1thm3tIc_15_WEirD}`
### writeups
- https://hackmd.io/@ptr-yudai/BJ3BCl8dd#Alternative-Arithmetic-Intermediate-Flag
- https://github.com/thewhitecircle/ctf_writeups/blob/main/sdctf_2021/misc.md#alternative-arithmetic
- https://qiita.com/mikecat_mixc/items/5a0c45751b15c8a8513b#alternative-arithmetic-intermediate-flag

# Alternative Arithmetic (Final Flag)
## Misc - Hard
| author | prereq chals | first blood | solves | final points |
| --- | --- | --- | --- | --- |
| k3v1n | Alternative Arithmetic (Intermediate) | **MikeCAT** from **Team MikeCAT** | 16 | 537 |

### prompt
Please submit the final flag of this challenge (after correctly answering the 5 questions)

Connect via: `nc java.sdc.tf 1337` (same as the intermediate flag)

**attachments**: `None, don't give out the source code`
### original specification
Make a Java program that asks the participant to complete a series of challenges before giving the flag:
4. Find 3 numbers between 0.0 and 500.0 with at most one decimal point (as strings not double's) such that new BigDecimal(numStr1) + new BigDecimal(numStr2) == new BigDecimal(numStr3) but Double.parseDouble(numStr1) + Double.parseDouble(numStr2) != Double.parseDouble(numStr3). (One possible correct answer: 0.1, 0.2, 0.3) Using the fact that numbers can't be represented exactly in IEEE floating point.
5. (Violation of the law of trichotomy): Fill in the <type> (obtained by allowing the user to input any string, check that it contains only characters allowed as valid Java identifiers to avoid turning this into a PyJail escape, and then evaluate the expression using jdk.jshell.JShell) in addition to providing 2 non-NaN i and j of any numerical type to violate the law of trichotomy: var ii = (<type>) i; var jj = (<type>) j; if(!(ii == jj || ii < jj || ii > jj)) System.out.println("Yay here's the flag:"); (Correct answer: type is Integer or Long, i and j are large but equal numbers. Comparing between Objects will not work as expected with equality)

**flag**: `sdctf{MATH_pr0f:iS_tH1S_@_bUG?CS_prOF:n0P3_tHIS_iS_A_fEATuRe!}`
### writeups
- https://hackmd.io/@ptr-yudai/BJ3BCl8dd#Alternative-Arithmetic-Final-Flag
- https://github.com/thewhitecircle/ctf_writeups/blob/main/sdctf_2021/misc.md#alternative-arithmetic-final-flag
- https://qiita.com/mikecat_mixc/items/5a0c45751b15c8a8513b#alternative-arithmetic-final-flag