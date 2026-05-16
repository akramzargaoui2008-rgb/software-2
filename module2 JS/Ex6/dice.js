function rollDice() {
  const result = Math.floor(Math.random() * 6) + 1;
  return result;
}

const rolls = [];

let roll;
do {
  roll = rollDice();
  rolls.push(roll);
} while (roll !== 6);

for (let i = 0; i < rolls.length; i++) {
  console.log(rolls[i]);
}
