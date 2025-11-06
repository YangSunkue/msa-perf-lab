// Package handler
package handler

import (
	service "gocore/internal/service/rest"
	"net/http"

	"github.com/gin-gonic/gin"
)

// end_to_end/rest_vs_grpc/k6_rest.js
func PingHandler(c *gin.Context) {
	var req map[string]string
	if err := c.BindJSON(&req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "invalid JSON"})
		return
	}

	message := service.GetPingMessage()
	c.JSON(http.StatusOK, gin.H{
		"message":      message,
		"payload_data": req["payload"],
	})
}
