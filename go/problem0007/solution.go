// By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
// we can see that the 6th prime is 13.
//
// What is the 10001st prime number?
package main

import (
	"fmt"
	"utils/primes"
)

func main() {
	input := 10001
	p := primes.NewPrimes()
	for i := 1; i < input; i++ {
		_ = p.Next()
	}
	fmt.Printf("The %vth prime number is %v\n", input, p.Get())
}
