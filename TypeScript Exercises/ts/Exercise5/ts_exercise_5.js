// TypeScript - Exercise 5. Linked list of points.
// Point class, storing coordinates and a reference to the next point
var Point = /** @class */ (function () {
    // Set random values for the point in the range [-10, 10]
    function Point() {
        this.data = { x: 0, y: 0 };
        this.data.x = Math.floor(Math.random() * 21 - 10);
        this.data.y = Math.floor(Math.random() * 21 - 10);
        if (Math.random() >= 0.5) // Random value
            this.data.z = Math.floor(Math.random() * 21 - 10);
    }
    return Point;
}());
// Stores an array of points. Can return them all nested from the first one as if it was a linked list.
var LinkedListPoints = /** @class */ (function () {
    function LinkedListPoints() {
        this.points = [];
    }
    LinkedListPoints.prototype.add = function (point) {
        this.points.push(point);
    };
    // Return the array of points arranged as a LinkedList
    LinkedListPoints.prototype.list = function () {
        if (this.points.length == 0)
            return {};
        var final_point = new Point(); // Point that will be modified
        var return_point = final_point; // Reference to the initial node that we will return
        // Insert all positive points nested into a point that will be returned
        for (var i = 0; i < this.points.length; i++) {
            final_point.data = this.points[i].data;
            final_point.next = this.points[i + 1];
            final_point = final_point.next;
        }
        return return_point;
    };
    return LinkedListPoints;
}());
// Returns a linked list of 'n' points
function createLinkedPoints(n) {
    var linked_list = new LinkedListPoints();
    for (var i = 0; i < n; i++) {
        linked_list.add(new Point());
    }
    return linked_list.list();
}
// For a LinkedList of  points, returns a LinkedList of all points with x > 0
function positivePointsX(input) {
    // If a wrong input is given return nothing
    if (!input.data)
        return {};
    // Store all positive X points into a LinkedList
    var linked_list = new LinkedListPoints();
    if (input.data.x > 0)
        linked_list.add(input);
    while (input.next) {
        input = input.next;
        if (input.data.x > 0)
            linked_list.add(input);
    }
    return linked_list.list();
}
// Program
var list = createLinkedPoints(-4);
console.log(JSON.stringify(list));
var positive_list = positivePointsX(list);
console.log(JSON.stringify(positive_list));
