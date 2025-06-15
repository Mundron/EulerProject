// Package primes for prime generator and methods to return divisors of numbers
package primes

import (
	"math"
)

var foundPrimes = []int{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43}

// Primes can return prime numbers
type Primes struct {
	found []int
	index int
}

// NewPrimes creates new object for prime numbers
func NewPrimes() Primes {
	return Primes{foundPrimes, 0}
}

// Next returns next prime number
func (p *Primes) Next() int {
	p.index++
	if p.index < len(p.found) {
		return p.found[p.index]
	}

	nextPrime := p.found[len(p.found)-1] + 2
	for {
		isPrime := true
		for _, fp := range p.found {
			if nextPrime%fp == 0 {
				isPrime = false
				break
			}
		}
		if isPrime {
			p.found = append(p.found, nextPrime)
			return nextPrime
		}
		nextPrime += 2
	}
}

// Reset resets prime object index
func (p *Primes) Reset() {
	p.index = 0
}

// Get returns prime number at index
func (p *Primes) Get() int {
	return p.found[p.index]
}

type number interface {
	~int8 | ~uint8 | ~int16 | ~uint16 | ~int32 | ~uint32 | ~int64 | ~uint64 | ~int
}

// PrimeFactorIterator returns function which iterates over the divisors of the
// number
func PrimeFactorIterator[T number](n T, p Primes) func() int {
	p.Reset()
	m := uint64(n)
	return func() int {
		if m <= uint64(1) {
			return 0
		}
		fp := uint64(p.Get())
		for {
			// fmt.Printf("Test divisibility of %v by %v\n", n, fp)
			if m%fp == 0 {
				m /= fp
				return int(fp)
			}
			fp = uint64(p.Next())
		}
	}
}

// PrimeList returns a slice of prime factors with repeatition
func PrimeList[T number](n T, p Primes) []int {
	result := []int{}
	divs := PrimeFactorIterator(n, p)
	for d := divs(); d > 0; d = divs() {
		result = append(result, d)
	}
	return result
}

// GetPrimeFactorization returns mapping from primes to their count
func GetPrimeFactorization[T number](n T, p Primes) map[int]int {
	result := make(map[int]int)
	divs := PrimeFactorIterator(n, p)
	for d := divs(); d > 0; d = divs() {
		result[d]++
	}
	return result
}

// ReducePrimeFactorization returns corresponding number
func ReducePrimeFactorization(fact map[int]int) uint64 {
	result := uint64(1)
	for k, v := range fact {
		result *= uint64(math.Pow(float64(k), float64(v)))
	}
	return result
}
