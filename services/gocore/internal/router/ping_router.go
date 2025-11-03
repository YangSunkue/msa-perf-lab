// Package router
package router

import (
	"gocore/internal/handler"

	"github.com/gin-gonic/gin"
)

func InitPingRoutes(r *gin.Engine) {
	api := r.Group("/ping")
	{
		api.GET("", handler.PingHandler)
	}
}
