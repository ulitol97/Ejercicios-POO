// example TS to JS 2
class Greet {
	static say_hi (name: string) {
		console.log ("Hello " + name)
	}
}

let person_2 = {
	name: "Edu"
}

Greet.say_hi(person_2.name)