// ts - Exercise 5. Linked list of points
// Point class, storing coordinates and a reference to the next point
class Point {
    // Set random values for the point in the range [-10, 10]
    constructor() {
        this.data = { x: 0, y: 0 };
        this.data.x = Math.floor(Math.random() * 21 - 10);
        this.data.y = Math.floor(Math.random() * 21 - 10);
        if (Math.random() >= 0.5) // Random value
            this.data.z = Math.floor(Math.random() * 21 - 10);
    }
}
// Creates a quick linked list of points and returns the initial one
function createLinkedPoints(n) {
    let og_point = new Point();
    let point = og_point;
    for (let i = 0; i < n; i++) {
        if (i != n - 1) {
            point.next = new Point;
            point = point.next;
        }
    }
    return og_point;
}
// For a list of linked points, returns a list of all linked points with an X > 0
function positivePointsX(input) {
    // let point = input
    // // The first point of the new linked points must be the first fulfilling the condition
    // while (point.data.x <= 0 && point.next){
    //   point = point.next
    // }
    // let og_point = point
    // while (point.next){
    //   if (point.next.data.x <= 0){
    //     point.next = point.next.next
    //     point = point.next
    //   }
    //   else {
    //     point = point.next
    //   }
    // }
    // let return_point = new Point()
    // // The first point of the new linked points must be the first fulfilling the condition
    // while (input.data.x <= 0){
    //   input = input.next
    // }
    // return_point.data = input.data
    // while (input.next){
    //   input = input.next
    //   if (input.data.x > 0){
    //     return_point.next = new Point();
    //     return_point.next.data = input.data;
    //   }
    // }
    let positive_points = [];
    if (input.data.x > 0)
        positive_points.push(input);
    while (input.next) {
        input = input.next;
        if (input.data.x > 0)
            positive_points.push(input);
    }
    let final_point = new Point();
    let return_point = final_point;
    for (let i = 0; i < positive_points.length; i++) {
        final_point.data = positive_points[i].data;
        final_point.next = positive_points[i + 1];
        final_point = final_point.next;
    }
    return return_point;
}
let list = createLinkedPoints(5);
console.log(JSON.stringify(list));
let positive_list = positivePointsX(list);
console.log(JSON.stringify(positive_list));
//# sourceMappingURL=ts_exercise_5.js.map