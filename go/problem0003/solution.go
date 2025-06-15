package main

import "fmt"

type primes struct {
	found []uint64
	index int
}

func GetPrimes() primes {
	return primes{[]uint64{2, 3}, 0}
}

func (p *primes) Next() uint64 {
	p.index++
	if p.index < len(p.found) {
		return p.found[p.index]
	}

	next_prime := p.found[len(p.found)-1] + 2
	for {
		is_prime := true
		for _, fp := range p.found {
			if next_prime%fp == 0 {
				is_prime = false
				break
			}
		}
		if is_prime {
			p.found = append(p.found, next_prime)
			return next_prime
		}
		next_prime += 2
	}
}

func (p *primes) Reset() {
	p.index = 0
}

func (p *primes) Get() uint64 {
	return p.found[p.index]
}

type number struct {
	value uint64
}

func (n *number) Divisor(p *primes) uint64 {
	if n.value <= 1 {
		return 0
	}
	fp := p.Get()
	for {
		if n.value%fp == 0 {
			n.value /= fp
			return fp
		}
		fp = p.Next()
	}
}

func main() {
	ps := GetPrimes()
	n := number{600851475143}
	result := n.Divisor(&ps)
	for n.value > 1 {
		result = n.Divisor(&ps)
	}
	fmt.Println(result)
}
