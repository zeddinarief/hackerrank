package main

import(
	"fmt"
)

func main() {
	path := "UDDUUDDU"
	valleys := countingValleys(path)
	fmt.Println(valleys)
}

func countingValleys(path string) int32 {
    // Write your code here
	var seaLevel int32
    var valleys int32
    var level int32

	for _, val := range path {
		if string(val) == "U" {
			if seaLevel - level == 1  {
				valleys++
			}

			level++	
		} else if string(val) == "D" {
			level--
		}
	}

	return valleys
}