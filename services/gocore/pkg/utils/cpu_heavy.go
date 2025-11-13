// Package utils
package utils

import "log"

// HeavyCalculation 실제 CPU 연산 로직: 난이도(n)만큼 반복하며 CPU 점유
func HeavyCalculation(n int32) int64 {

	const baseLoop = 100_000
	loopCount := int(n) * baseLoop

	log.Printf("DEBUG: Starting CPU loop. Complexity: %d, Total Loop Count: %d", n, loopCount)

	var sum int64 = 0
	for i := 0; i < loopCount; i++ {
		sum += int64(i)*int64(i)%1_000 + 1
	}

	log.Printf("DEBUG: CPU loop finished.")

	return sum
}
