// Package router
package router

import (
	"github.com/gin-gonic/gin"
)

func SetupRouter() *gin.Engine {
	r := gin.Default()
	r.RedirectTrailingSlash = false

	InitPingRoutes(r)
	InitMqAsyncRoutes(r)

	return r
}
