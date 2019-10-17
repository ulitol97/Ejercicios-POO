// ts - Exercise 5. Linked list of points

// Interface for any object representing coordinates of a point
interface Coordinate {
  x: number;
  y: number;
  z?: number; // optional 3rd dimension
}

// Point class, storing coordinates and a reference to the next point
class Point {
  public data: Coordinate = {x: 0, y:0}
  public next: Point


  // Set random values for the point in the range [-10, 10]
  constructor(){
    this.data.x = Math.floor(Math.random() * 21 - 10);
    this.data.y = Math.floor(Math.random() * 21 - 10);
    if (Math.random() >= 0.5) // Random value
      this.data.z = Math.floor(Math.random() * 21 - 10);
  }
}

// Creates a quick linked list of points and returns the initial one
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

// For a list of linked points, returns a list of all linked points with an X > 0
function positivePointsX (input: Point): Point {

  // Retrieve all positive X points
  let positive_points: Array<Point> = []

  if (input.data.x > 0) positive_points.push(input)
  while (input.next){
    input = input.next
    if (input.data.x > 0) positive_points.push(input)
  }

  let final_point = new Point() // Point that will be modified
  let return_point = final_point // Reference to the initial node of the linked points that we return
  
  // Insert all positive X points into a point that will be returned
  for (let i = 0; i < positive_points.length; i++){
    final_point.data = positive_points[i].data;
    final_point.next = positive_points[i+1];
    final_point = final_point.next
  }

  return return_point
}

let list = createLinkedPoints(5)
console.log(JSON.stringify(list))
let positive_list = positivePointsX(list)
console.log(JSON.stringify(positive_list))