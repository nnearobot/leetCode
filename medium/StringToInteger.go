package main

import "fmt"

func main() {
	fmt.Println(myAtoi("92233720368547758083453455"))
	fmt.Println(myAtoi("42"))
	fmt.Println(myAtoi("2147483648"))
	fmt.Println(myAtoi("9999999999"))
	fmt.Println(myAtoi("2147483649"))
	fmt.Println(myAtoi("-2147483649"))
	fmt.Println(myAtoi("-2147483646"))
	fmt.Println(myAtoi("-10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000522545459"))
	fmt.Println(myAtoi("10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000522545459"))
	fmt.Println(myAtoi("   -345r Kbk "))
	fmt.Println(myAtoi("  0000000000012345678"))
}

func myAtoi(s string) int {
	var digits = map[rune]int{
		'0': 0,
		'1': 1,
		'2': 2,
		'3': 3,
		'4': 4,
		'5': 5,
		'6': 6,
		'7': 7,
		'8': 8,
		'9': 9,
	}
	var sign rune
	var foundDigits = []int{}

	for _, runeVal := range s {
		if sign == 0 {
			if runeVal == ' ' {
				continue
			} else {
				if runeVal == '-' || runeVal == '+' {
					sign = runeVal
					continue
				} else {
					sign = '+'
				}
			}
		}

		val, ok := digits[runeVal]
		if !ok {
			break
		}

		if val != 0 || len(foundDigits) > 0 {
			foundDigits = append(foundDigits, val)
		}
	}

	if len(foundDigits) == 0 {
		return 0
	}

	if len(foundDigits) > 10 {
		if sign == '-' {
			return -2147483648
		}

		return 2147483647
	}

	var length = len(foundDigits)
	var curSum int
	var res int

	for i := length - 1; i >= 0; i-- {
		if foundDigits[i] == 0 {
			continue
		}

		curSum = foundDigits[i]

		if sign == '-' {
			curSum *= -1
		}
		for j := 1; j < (length - i); j++ {
			curSum *= 10
		}
		res += curSum

		if res < -2147483648 {
			res = -2147483648
			break
		}

		if res > 2147483647 {
			res = 2147483647
			break
		}
	}

	return res
}
