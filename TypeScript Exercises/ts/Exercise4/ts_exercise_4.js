// TypeScript - Exercise 4. Random dice throw
// Future style properties
var diceSize = 100;
var diceSizeStr = diceSize + 'px';
var diceMargin = 15;
var diceMarginStr = diceMargin + 'px';
var Dice = /** @class */ (function () {
    function Dice(div, span) {
        this.div = div;
        this.span = span;
        // The span will contain the number inside the div, which is the dice
        div.appendChild(span);
        this.changeNumber();
    }
    Dice.prototype.changeNumber = function () {
        // Random number 1-6
        this.span.textContent = (Math.floor(Math.random() * 6) + 1).toString();
        return true;
    };
    return Dice;
}());
var dices = [];
// Insert 4 dices
for (var i = 0; i < 4; i++) {
    // Create dice
    dices.push(new Dice(document.createElement('div'), document.createElement('span')));
    // Set the style of the dice
    dices[i].div.style.width = diceSizeStr;
    dices[i].div.style.height = diceSizeStr;
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
var throw_button = document.createElement('button');
document.body.appendChild(throw_button);
// Set button text
throw_button.textContent = 'Roll the dice';
// Set button style
throw_button.style.width = diceSizeStr;
throw_button.style.height = diceSizeStr;
throw_button.style.margin = diceMarginStr;
// Set button behaviour
throw_button.onclick = function (event) {
    for (var i = 0; i < dices.length; i++) {
        dices[i].changeNumber();
    }
};
// Adjust overall display
var body = document.getElementsByTagName("BODY")[0];
body.style.display = 'flex';
