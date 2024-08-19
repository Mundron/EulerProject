// A Pythagorean triplet is a set of three natural numbers, a < b < c,
// for which, a^2 + b^2 = c^2
// For example, 3^2 + 4^2 = 25 = 5^2.
//
// There exists exactly one Pythagorean triplet for which a+b+c=1000.
// Find the product abc.
package main

import "fmt"

func main() {
	limit := 1000
	result := 0
	// since a+b+c==1000 and a < b < c we get
	// 3a < 1000 < 3c hence a < 1000/3 and c > 1000/3
	// further a > 0 so 2b < a+b+c = 1000 and b < 1000/2
	for a := 1; a < (limit-2)/3; a++ {
		for b := a + 1; b < (limit-1)/2; b++ {
			c := limit - a - b
			if a*a+b*b == c*c {
				fmt.Printf(
					"Found %v / %v / %v -> sum = %v, squares %v + %v = %v -> %v\n",
					a,
					b,
					c,
					a+b+c,
					a*a,
					b*b,
					c*c,
					a*b*c,
				)
				result = max(result, a*b*c)
			}
		}
	}
	fmt.Printf("Result is:\n%v\n", result)
}
