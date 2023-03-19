//Quiz: Laugh it Off 2 (5-1)

/*
 * Programming Quiz: Laugh it Off 1 (5-1)
 */

/*
 * QUIZ REQUIREMENTS
 * - Your code should have a `laugh()` function
 * - Your `laugh()` function should return the correct output
 * - Your code should print `\"hahahahahahahahahaha!\"` by calling the `laugh()` function inside `console.log()`
 * - BE CAREFUL ABOUT THE PUNCTUATION AND THE EXACT WORDS TO BE PRINTED.
 */


// your code goes here
function laugh(){
    var word = "hahahahahahahahahaha!";
    return word;
}


console.log(laugh());

// Quiz: Laugh it Off 2 (5-2)

/*
 * Programming Quiz: Laugh it Off 2 (5-2)
 *
 * Write a function called `laugh` with a parameter named `num` that represents the number of "ha"s to return.
 *
 * Note:
 *  - make sure your the final character is an exclamation mark ("!")
 *  - make sure that your function produces the correct results when it is called multiple times
 */

/*
 * QUIZ REQUIREMENTS
 * - Your code should have a `laugh()` function
 * - Your `laugh()` function should have one parameter named `num`
 * - Your `laugh()` function should return the correct number of laughs
 */

function laugh(num){
    var ha = 'ha';
    ha = ha.repeat(num-1)+'ha!';
    return ha;
}

console.log(laugh(3))

/*
var totn_string = 'TechOnTheNet';

console.log(totn_string.repeat(0));
console.log(totn_string.repeat(1));
console.log(totn_string.repeat(2));
console.log(totn_string.repeat(3));
*/

//Quiz: Laugh (5-4)

/*
 * Programming Quiz: Laugh (5-4)
 */

/*
 * QUIZ REQUIREMENTS
 * - Your code should have a variable `laugh`
 * - Your code should include an anonymous function expression stored in the variable `laugh`
 * - Your anonymous function expression should take one argument
 * - Your anonymous function expression should return the correct number of `hahaha`\'s
 */


var laugh = function(num){
    var y = 'ha';
    y = y.repeat(num-1) + 'ha!';
    return y;
}

console.log(laugh(10));
