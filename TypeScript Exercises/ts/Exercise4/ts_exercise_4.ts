// TypeScript - Exercise 4. Random dice throw

// Future style properties
let diceSize: number = 100;
let diceSizeStr: string = diceSize+'px'
let diceMargin: number = 15
let diceMarginStr: string = diceMargin+'px'

// HTML elements that each dice must have
interface ElementDice{
  div: Element
  span: Element
}

class Dice {
  constructor(public div: Element, public span: Element, ){
    // The span will contain the number inside the div, which is the dice
    div.appendChild(span)
    this.changeNumber()
  }

  changeNumber (): boolean {
    // Random number 1-6
    this.span.textContent = (Math.floor(Math.random() * 6) + 1).toString()
    return true
  }
}

let dices: Array<Dice> = []

// Insert 4 dices
for (let i=0; i < 4; i++) {

  // Create dice
  dices.push(new Dice(document.createElement('div'), document.createElement('span')));

  // Set the style of the dice
  (dices[i].div as HTMLElement).style.width = diceSizeStr;
  (dices[i].div as HTMLElement).style.height = diceSizeStr;
  (dices[i].div as HTMLElement).style.margin = diceMarginStr;
  (dices[i].div as HTMLElement).style.textAlign = 'center';
  (dices[i].div as HTMLElement).style.position = 'relative';
  (dices[i].div as HTMLElement).style.backgroundColor = 'grey';

  (dices[i].span as HTMLElement).style.color = 'white';
  (dices[i].span as HTMLElement).style.position = 'relative';
  (dices[i].span as HTMLElement).style.top = '40%';

  // Add to body
  document.body.appendChild(dices[i].div);
}

// Create throw button
let throw_button: HTMLButtonElement = document.createElement ('button')
document.body.appendChild(throw_button);

// Set button text
throw_button.textContent = 'Roll the dice'

// Set button style
throw_button.style.width = diceSizeStr
throw_button.style.height = diceSizeStr
throw_button.style.margin = diceMarginStr

// Set button behaviour
throw_button.onclick = (event) => {
  for (let i=0; i < dices.length; i++) {
    dices[i].changeNumber()
  }
}

// Adjust overall display
let body: Element = document.getElementsByTagName("BODY")[0];
(body as HTMLElement).style.display = 'flex'
