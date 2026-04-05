let numbers = [];
let input = Number(prompt("Enter a number (0 to stop):"));

while (input !== 0) {
    numbers.push(input);
    input = Number(prompt("Enter a number (0 to stop):"));
}

numbers.sort(function(a, b) { return b - a; });

for (let i = 0; i < numbers.length; i++) {
    console.log(numbers[i]);
}
