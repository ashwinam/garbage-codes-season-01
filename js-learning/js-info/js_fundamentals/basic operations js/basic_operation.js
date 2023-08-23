/* 
# Math Operators
1. addition (+)
2. substraction (-)
3. multplication (*)
4. division (/)
5. exponentiation (**)
6. remainder (%)


# String concatenation

* 'my' + ' string'  = my string
it will concatenate the string

Note: if any of the operand is string and other is number then concatenation is happening that time

ex = '2'+3 = 23


See, it doesn’t matter whether the first operand is a string or the second one.

alert(2 + 2 + '1' ); // "41" and not "221"
Here, operators work one after another. The first + sums two numbers, so it returns 4, then the next + adds the string 1 to it, so it’s like 4 + '1' = '41'.

alert('1' + 2 + 2); // "122" and not "14"
Here, the first operand is a string, the compiler treats the other two operands as strings too. The 2 gets concatenated to '1', so it’s like '1' + 2 = "12" and "12" + 2 = "122".

The binary + is the only operator that supports strings in such a way. Other arithmetic operators work only with numbers and always convert their operands to numbers.

let apples = "2";
let oranges = "3";

// both values converted to numbers before the binary plus
alert( +apples + +oranges ); // 5

// the longer variant
// alert( Number(apples) + Number(oranges) ); // 5

*/


/*
"" + 1 + 0
'10'
"" - 1 + 0
-1
true + false
1
6 / "3"
2
"2" * "3"
6
4 + 5 + "px"
'9px'
"$" + 4 + 5
'$45'
"4" - 2
2
"4px" - 2
NaN
"  -9  " + 5
'  -9  5'
"  -9  " - 5
-14
null + 1
1
undefined + 1
NaN
" \t \n" - 2
-2
*/