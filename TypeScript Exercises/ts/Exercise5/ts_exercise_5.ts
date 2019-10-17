// ts - Exercise 5. Linked list of points

// Interface for coordinates of each point
interface Coordinate {
  x: number;
  y: number;
  z?: number; // optional 3rd dimension
}

class Point implements Coordinate {
  x: number;
  y: number;
  z?: number;

  // Set random values for the point in the range [-10, 10]
  constructor(){
    this.x = Math.floor(Math.random() * 21 - 10);
    this.y = Math.floor(Math.random() * 21 - 10);
    if (Math.random() >= 0.5) // Random value
      this.z = Math.floor(Math.random() * 21 - 10);
  }
}

interface ListNode<T> {
  data: T;
  next?: ListNode<T>;
}

class LinkedList<T>{
  public head: ListNode<T> = null
  public tail: ListNode<T> = null

  public append (value: T): LinkedList<T> {

    let node = {data: value}

    if (this.head == null) {
        this.head = node;
        this.tail = node;
    }
    else {
      this.appendToTheEnd(node);
    }
    return this;
  }

  private appendToTheEnd (node: ListNode<T>) {
    this.tail.next = node;
    this.tail = node;
  }
}

// Creates a quick linked list of points
function createLinkedPoints (n: number): LinkedList<Point> {
  let points: LinkedList<Point> = new LinkedList<Point>()
  for (let i=0; i < n; i++){
    points.append(new Point())
  }
  return points
}

function positivePointsX (points: LinkedList<Point>): LinkedList<Point>{
  let positive_points: LinkedList<Point> = new LinkedList<Point>();

  let pointNode: ListNode<Point> = points.head
  while (pointNode != null){
    if (pointNode.data.x > 0){
      positive_points.append(pointNode.data)
    }
    pointNode = pointNode.next
  }

  return positive_points
}

let points = createLinkedPoints(15)
console.log(JSON.stringify(points.head || {}))

let positive_points = positivePointsX(points)
console.log(JSON.stringify(positive_points.head || {}))