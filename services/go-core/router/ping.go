// Package router
package router

import (
	"go-core/handler"

	"github.com/gin-gonic/gin"
)

func InitPingRoutes(r *gin.Engine) {
	api := r.Group("/ping")
	{
		api.GET("", handler.PingHandler)
	}
}
