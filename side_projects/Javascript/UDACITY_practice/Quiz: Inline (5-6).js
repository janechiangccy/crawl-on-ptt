/*
 * Programming Quiz: Inline Functions (5-6)
 */
 
 /*
 * QUIZ REQUIREMENTS
 * - Your code should have an `emotions()` function
 * - Your code should call the `emotions()` function
 * - Your `emotions()` function call should have an inline function expression passed as the second parameter
 * - Your function expression should return the expected output
 */


// don't change this code
// emotions() function definition
function emotions(myString, myFunc) {
    console.log("I am " + myString + ", " + myFunc(2));
}

// your code goes here
// Call the emotions() function with two arguments
// Argument 1 - "happy" string
// Argument 2 - an inline function expression

emotions('happy', function (num) {
    var word = 'ha';
    return word.repeat(num-1)+'ha!';
});


// Note: 注意 function 直接接 {}, 後面才接 emotions 的 ')'

/*
// Function declaration that takes in two arguments: a function for displaying a message, along with a name of a movie

function movies(messageFunction, name) {
  messageFunction(name);
}

// Call the movies function, pass in the function and name of movie

movies(function displayFavorite(movieName) {
  console.log("My favorite movie is " + movieName);
}, "Finding Nemo");

*/