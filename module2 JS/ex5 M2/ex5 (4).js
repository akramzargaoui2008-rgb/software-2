let numbers = [];
let duplicate = false;

while (!duplicate) {
    let input = Number(prompt("Enter a number:"));

    for (let i = 0; i < numbers.length; i++) {
        if (numbers[i] === input) {
            duplicate = true;
        }
    }

    if (duplicate) {
        alert(input + " has already been given.");
    } else {
        numbers.push(input);
    }
}

numbers.sort(function(a, b) { return a - b; });

for (let i = 0; i < numbers.length; i++) {
    console.log(numbers[i]);
}
