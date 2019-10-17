// ts - Exercise 5. Linked list of points
class Point {
    // Set random values for the point in the range [-10, 10]
    constructor() {
        this.x = Math.floor(Math.random() * 21 - 10);
        this.y = Math.floor(Math.random() * 21 - 10);
        if (Math.random() >= 0.5) // Random value
            this.z = Math.floor(Math.random() * 21 - 10);
    }
}
class LinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
    }
    append(value) {
        let node = { data: value };
        if (this.head == null) {
            this.head = node;
            this.tail = node;
        }
        else {
            this.appendToTheEnd(node);
        }
        return this;
    }
    appendToTheEnd(node) {
        this.tail.next = node;
        this.tail = node;
    }
}
// Creates a quick linked list of points
function createLinkedPoints(n) {
    let points = new LinkedList();
    for (let i = 0; i < n; i++) {
        points.append(new Point());
    }
    return points;
}
function positivePointsX(points) {
    let positive_points = new LinkedList();
    let pointNode = points.head;
    while (pointNode != null) {
        if (pointNode.data.x > 0) {
            positive_points.append(pointNode.data);
        }
        pointNode = pointNode.next;
    }
    return positive_points;
}
let points = createLinkedPoints(15);
console.log(JSON.stringify(points.head || {}));
let positive_points = positivePointsX(points);
console.log(JSON.stringify(positive_points.head || {}));
//# sourceMappingURL=ts_exercise_5.js.map