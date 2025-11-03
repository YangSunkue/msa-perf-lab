// Package handler
package handler

import (
	service "gocore/internal/service/rest"
	"net/http"

	"github.com/gin-gonic/gin"
)

func PingHandler(c *gin.Context) {

	message := service.GetPingMessage()
	c.JSON(http.StatusOK, gin.H{
		"message": message,
	})
}
