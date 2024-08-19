// Euler project problem 4
// A palindromic number reads the same both ways. The largest palindrome made
// from the product of two 2-digit numbers is 9009 = 91 x 99

// Find the largest palindrome made from the product of two 3-digit numbers.
package main

import (
	"fmt"
	"strconv"
)

func isPalindrom(value int) bool {
	number := strconv.Itoa(value)
	for i, c := range number {
		if uint8(c) != number[len(number)-i-1] {
			return false
		}
	}
	return true
}

func main() {
	rvalue, rx, ry := 0, 0, 0

	for x := 100; x < 999; x++ {
		for y := x + 1; y < 1000; y++ {
			if prod := x * y; isPalindrom(prod) {
				if prod > rvalue {
					rvalue, rx, ry = prod, x, y
				}
			}
		}
	}
	fmt.Printf("Biggest palindrom: %v x %v = %v\n", rx, ry, rvalue)
}
