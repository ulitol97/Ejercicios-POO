// example TS to JS 2
function sqrt(list: number[]) {
  return list.map(Math.sqrt)
}

// Ejemplo correcto
let numbers: number[] = [4, 9, 16, 25]
let result = sqrt(numbers) // Type of 'result' inferred from the return of sqrt
console.log('Square roots: ' + result)

// Ejemplo incorrecto
//let letters: string[] = ['a', 'b', 'c', 'd']
//let result_2 = sqrt(letters)
//console.log('Square roots: ' + result_2)
