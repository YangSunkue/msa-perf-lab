// Package main
package main

import (
	"go-core/router"
)

func main() {
	r := router.SetupRouter()
	r.Run(":8080")
}
