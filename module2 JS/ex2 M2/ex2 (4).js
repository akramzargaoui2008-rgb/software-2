let count = Number(prompt("How many participants?"));
let names = [];

for (let i = 0; i < count; i++) {
    names[i] = prompt("Enter name of participant " + (i + 1) + ":");
}

names.sort();

document.write("<ol>");
for (let i = 0; i < names.length; i++) {
    document.write("<li>" + names[i] + "</li>");
}
document.write("</ol>");
