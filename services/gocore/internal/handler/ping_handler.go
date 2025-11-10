// Package handler
package handler

import (
	rest "gocore/internal/service/rest"
	"net/http"

	"github.com/gin-gonic/gin"
)

// PingHandler end_to_end/rest_vs_grpc/k6_rest.js
func PingHandler(c *gin.Context) {
	var req map[string]string
	if err := c.BindJSON(&req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "invalid JSON"})
		return
	}

	message := rest.GetPingMessage()
	c.JSON(http.StatusOK, gin.H{
		"message":      message,
		"payload_data": req["payload"],
	})
}
