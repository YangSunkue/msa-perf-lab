// Package router
package router

import (
	"gocore/internal/handler"

	"github.com/gin-gonic/gin"
)

func InitMqAsyncRoutes(r *gin.Engine) {
	api := r.Group("/mq_async")
	{
		api.POST("/delay", handler.MqAsyncDelayHandler)
	}
}
