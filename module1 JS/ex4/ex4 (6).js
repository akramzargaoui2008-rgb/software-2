let name = prompt("Enter student's name:");
let roll = Math.floor(Math.random() * 4) + 1;
let house;

if (roll === 1) {
    house = "Gryffindor";
} else if (roll === 2) {
    house = "Slytherin";
} else if (roll === 3) {
    house = "Hufflepuff";
} else {
    house = "Ravenclaw";
}

document.write(name + ", you are " + house + ".");
