package main

import "fmt"

func main() {
	var counter int64
	for counter = 0; counter < 10_000_000_000; counter++ {
	}
	fmt.Println(counter)
}
