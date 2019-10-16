// example TS to JS 4
class Control {
  private state: any
}

// In orden to implement SelectableControl, we must implement a void method 'select' + extend Control
interface SelectableControl extends Control {
  select(): void
}

class Button extends Control {
  select() {}
}

class Picture {
  select() {}
}

// A function that needs a SelectableControl implementation
function f (param: SelectableControl){
}

// Button is a SelectableControl
f (new Button())

// Picture is NOT a SelectableControl
f (new Picture())