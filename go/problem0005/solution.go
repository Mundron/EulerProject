// 2520 is the smallest number that can be divided by each of the numbers from
// 1 to 10 without any remainder.
// What is the smallest positive number that is evenly divisible by all of
// the numbers from 1 to 20?
package main

import (
	"eulerproject/utils/primes"
	"fmt"
)

func main() {
	limit := 20
	resultMap := make(map[int]int)
	p := primes.NewPrimes()
	for n := 2; n <= limit; n++ {
		for k, v := range primes.GetPrimeFactorization(n, p) {
			resultMap[k] = max(resultMap[k], v)
		}
	}
	fmt.Printf("Final result:\n%v\n", primes.ReducePrimeFactorization(resultMap))
}
