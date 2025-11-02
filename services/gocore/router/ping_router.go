// Package router
package router

import (
	"gocore/handler"

	"github.com/gin-gonic/gin"
)

func InitPingRoutes(r *gin.Engine) {
	api := r.Group("/ping")
	{
		api.GET("", handler.PingHandler)
	}
}
