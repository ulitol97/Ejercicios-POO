// ts - Exercise 4. Random dice throw
let diceSize = 100;
let diceSizeStr = diceSize + 'px';
let diceMargin = 15;
let diceMarginStr = diceMargin + 'px';
class Dice {
    constructor(div, span) {
        this.div = div;
        this.span = span;
        // The span will contain the number inside the div, which is the dice
        div.appendChild(span);
    }
    changeNumber() {
        // Random number 1-6
        this.span.textContent = (Math.floor(Math.random() * 6) + 1).toString();
        return true;
    }
}
let dices = [];
// Insert 4 dices
for (let i = 0; i < 4; i++) {
    // Create dice
    dices.push(new Dice(document.createElement('div'), document.createElement('span')));
    // Place a random number in range 1-6
    dices[i].changeNumber();
    // Set the style place a random number
    dices[i].div.style.width = diceSizeStr;
    dices[i].div.style.height = diceSizeStr;
    dices[i].div.style.margin = diceMarginStr;
    dices[i].div.style.margin = diceMarginStr;
    dices[i].div.style.textAlign = 'center';
    dices[i].div.style.position = 'relative';
    dices[i].div.style.backgroundColor = 'grey';
    dices[i].span.style.color = 'white';
    dices[i].span.style.position = 'relative';
    dices[i].span.style.top = '40%';
    // Add to body
    document.body.appendChild(dices[i].div);
}
// Create throw button
let throw_button = document.createElement('button');
document.body.appendChild(throw_button);
// Set text
throw_button.textContent = 'Throw dices';
// Set style
throw_button.style.width = diceSizeStr;
throw_button.style.height = diceSizeStr;
throw_button.style.margin = diceMarginStr;
// Set behaviour
throw_button.onclick = (event) => {
    for (let i = 0; i < dices.length; i++) {
        dices[i].changeNumber();
    }
};
// Adjust overall display
let body = document.getElementsByTagName("BODY")[0];
body.style.display = 'flex';
//# sourceMappingURL=ts_exercise_4.js.map