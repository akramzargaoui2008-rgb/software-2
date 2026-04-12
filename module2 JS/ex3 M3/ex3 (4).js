let dogs = [];

for (let i = 0; i < 6; i++) {
    dogs[i] = prompt("Enter dog name " + (i + 1) + ":");
}

dogs.sort();
dogs.reverse();

document.write("<ul>");
for (let i = 0; i < dogs.length; i++) {
    document.write("<li>" + dogs[i] + "</li>");
}
document.write("</ul>");
