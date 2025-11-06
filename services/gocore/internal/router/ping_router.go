// Package router
package router

import (
	"gocore/internal/handler"

	"github.com/gin-gonic/gin"
)

// end_to_end/rest_vs_grpc/k6_rest.js
func InitPingRoutes(r *gin.Engine) {
	api := r.Group("/ping")
	{
		api.POST("", handler.PingHandler)
	}
}
