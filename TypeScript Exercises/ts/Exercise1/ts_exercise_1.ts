// ts - Exercise 1.Generate a button to change the background color of the <div> tag 

let color :string = "magenta"

let squareSizeNum: number = 100;
let squareSizeStr: string = squareSizeNum+'px'

let button: Element = document.createElement ('button')
let div: Element = document.createElement ('div')


button.textContent = 'Go magenta';
document.body.appendChild(button);
document.body.appendChild(div);


// Function in TS controlling types
let colorChange: Function = (elem: Element, color: string) : boolean => {
  (elem as HTMLElement).style.backgroundColor = color;
  return true;
}

(div as HTMLElement).style.width = squareSizeStr;
(div as HTMLElement).style.height = squareSizeStr;
(button as HTMLElement).style.width = squareSizeStr;

(button as HTMLElement).onclick = (event) => {
  colorChange (div, color)
}
