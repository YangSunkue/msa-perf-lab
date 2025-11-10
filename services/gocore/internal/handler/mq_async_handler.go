// Package handler
package handler

import (
	service "gocore/internal/service/rest"
	"net/http"

	"github.com/gin-gonic/gin"
)

// MqAsyncDelayHandler 1초 대기 후 응답 (동기 처리 시뮬레이션)
func MqAsyncDelayHandler(c *gin.Context) {
	var req map[string]string
	if err := c.BindJSON(&req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "invalid JSON"})
		return
	}

	// 비즈니스 로직 대체 (1초 대기)
	service.SimulateDelay()

	c.JSON(http.StatusOK, gin.H{
		"message": "processing completed",
		"action":  req["action"],
		"took":    "1s",
	})
}
