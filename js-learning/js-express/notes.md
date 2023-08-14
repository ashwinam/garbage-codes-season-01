### JavaScript data types

1. Primitive types: Boolean, Number, String
2. Object types: Array, Object, Function
3. nullability: null, undefined

### 7 types of Primitive types.

1. undefined
2. null
3. boolean
4. Number
5. String
6. BigInt
7. symbol

\_We declare primitive types using primitive values.

const myBoolean = true

let myNumber = 42

let myString = 'Hello, world!'

### There are library methods.

const myString = 'Hello, world!'

// Find an index
console.log(myString.indexOf('world'))

// Replace a substring
console.log(myString.replace('world', 'universe'))

### There are type casting (There are library methods for casting strings to numbers and vice versa)

const myNumber = 42
2
const myString = '100.5'
3
​
4
// Anything to string
5
console.log(myNumber.toString())
"42"
6
​
7
// String to number
8
console.log(Number(myString))
100.5
9
​
10
// Alternately, the global parseInt or parseFloat
11
console.log(parseInt(myString))
100
