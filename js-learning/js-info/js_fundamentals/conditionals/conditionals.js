/*
Conditionals

If else 

if true then evaluate if clause
else clause

if(condition){ // evaluate a boolean or truthy or falsy values
    // true part
} else{
    //false part
}



*/

let accessAllowed;
let age = prompt('How old are you?', '');

if (age > 18) {
  accessAllowed = true;
} else {
  accessAllowed = false;
}

alert(accessAllowed);

// Convert above code in a shorter hand using question operator or ternary operator

let ans = age > 18 ? alert('You are eligible') : alert('You are not eligible.');


// Multiple ternary

age = prompt('age?', 18);

let message = (age < 3) ? 'Hi, baby!' :
  (age < 18) ? 'Hello!' :
  (age < 100) ? 'Greetings!' :
  'What an unusual age!';

alert( message );


// Task 2
/*
Using the if..else construct, write the code which asks: ‘What is the “official” name of JavaScript?’

If the visitor enters “ECMAScript”, then output “Right!”, otherwise – output: “You don’t know? ECMAScript!”
 */

let question = (prompt('What is the “official” name of JavaScript?: ') === 'ECMAScript') ? alert('Right!') : alert('You don’t know? ECMAScript!')

// Rewrite if following in question operator

let result;

if (a + b < 4) {
  result = 'Below';
} else {
  result = 'Over';
}

// answer
result = (a + b < 4) ? 'Below': 'Over'


// Rewrite multiple if else in  ternary operator 

message;

if (login == 'Employee') {
  message = 'Hello';
} else if (login == 'Director') {
  message = 'Greetings';
} else if (login == '') {
  message = 'No login';
} else {
  message = '';
}

// answer
message = (login == 'Employee') ? 'Hello': (login == 'Director') ? 'Greetings' : (login == '') ? 'No Login' : '' 
