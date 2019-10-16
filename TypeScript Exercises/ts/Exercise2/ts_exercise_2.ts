// ts - Exercise 2. Improve exercise 1 to have extra buttons and create them dynamically 

let color :string = "magenta"

let squareSizeNum: number = 100;
let squareSizeStr: string = squareSizeNum+'px'


// Exercise 2
class ColorChange {
  constructor(public div: Element){
  }

  changeColor (color: string): boolean {
    (this.div as HTMLElement).style.backgroundColor = color
    return true
  }
}

enum Colors {
  Green,
  Red,
  Magenta,
  Yellow
}

interface ElementSet{
  div: Element
  button: Element
}

let elementSets: Array<ElementSet> = []

// Insert 4 pairs div+button
for (let i=0; i < 4; i++) {
  elementSets.push({div: document.createElement ('div'), button: document.createElement ('button')})
}

// For each pair div/button, set the size, change the color, set the OnClick event of each button
// and add them to the body
elementSets.map ((element, index) => {
      let colorChange = new ColorChange(element.div);
      
      (element.div as HTMLElement).style.width = squareSizeStr;
      (element.div as HTMLElement).style.height = squareSizeStr;
      (element.button as HTMLElement).style.width = squareSizeStr;
      element.button.textContent = "Change color";

      document.body.appendChild(element.div);
      document.body.appendChild(element.button);

      (element.button as HTMLElement).onclick = (event) => {
               colorChange.changeColor (Colors[index])
    }
  }
)