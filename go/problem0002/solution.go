package main

import "fmt"

type fib struct {
	current, next int
}

func (f *fib) Next() int {
	f.current, f.next = f.next, f.current+f.next
	return f.current
}

func main() {
	sum, f := 0, fib{0, 1}
	for fn := f.Next(); fn < 4000000; fn = f.Next() {
		if fn%2 == 0 {
			sum += fn
		}
	}
	fmt.Println(sum)
}
