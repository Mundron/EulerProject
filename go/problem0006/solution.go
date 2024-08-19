// The sum of the squares of the first ten natural numbers is,
// 1^2 + 2^2 + ... + 10^2 = 385
// The square of the sum of the first ten natural numbers is,
// (1 + 2 + ... + 10)^2 = 55^2 = 3025
// Hence the difference between the sum of the squares of the first ten
// natural numbers and the square of the sum is 3025 - 385 = 2640.
//
// Find the difference between the sum of the squares of the first one hundred
// natural numbers and the square of the sum.
package main

import (
	"fmt"
	"math"
)

func sumOfSquares(n int) int {
	return n * (n + 1) * (2*n + 1) / 6
}

func squareOfSum(n int) int {
	return int(math.Pow(float64(n*(n+1)/2), 2.0))
}

func main() {
	input := 100
	s1, s2 := squareOfSum(input), sumOfSquares(input)
	fmt.Printf(
		"Difference of %v summed and squadred (%v) minus the sum of squares (%v) is:\n%v\n",
		input,
		s1,
		s2,
		s1-s2,
	)
}
