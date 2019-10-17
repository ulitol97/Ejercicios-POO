// ts - Exercise 5. Linked list of points

// Interface for coordinates of each point
interface Coordinate {
  x: number;
  y: number;
  z?: number; // optional 3rd dimension
}

class Point {
  private data: Coordinate = {x: 0, y:0}
  public next: Point


  // Set random values for the point in the range [-10, 10]
  constructor(){
    this.data.x = Math.floor(Math.random() * 21 - 10);
    this.data.y = Math.floor(Math.random() * 21 - 10);
    if (Math.random() >= 0.5) // Random value
      this.data.z = Math.floor(Math.random() * 21 - 10);
  }
}


// Creates a quick linked list of points
function createLinkedPoints (n: number): Point {
  let og_point: Point = new Point()
  let point = og_point
  for (let i=0; i < n; i++){
    if (i != n-1){
      point.next = new Point
      point = point.next
    }
  }
  return og_point
}

console.log(JSON.stringify(createLinkedPoints(3)))