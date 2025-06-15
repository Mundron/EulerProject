// Find the sum of all primes below two million
package main

import (
	"eulerproject/utils/primes"
	"fmt"
)

func main() {
	limit := 2000000
	p := primes.NewPrimes()
	result := p.Get()
	fmt.Println("This can run a few seconds")
	for fp := p.Next(); fp < limit; fp = p.Next() {
		result += fp
	}
	fmt.Printf("Final result:\n%v\n", result)
}
