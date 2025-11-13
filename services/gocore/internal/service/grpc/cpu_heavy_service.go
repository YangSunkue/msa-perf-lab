// Package servicegrpc
package servicegrpc

import (
	"context"
	pb "gocore/pkg/proto"
	"gocore/pkg/utils"
	"log"
)

// CPUHeavyServiceServer CpuHeavyService의 요청을 처리하는 구조체
type CPUHeavyServiceServer struct {
	pb.UnimplementedCpuHeavyServiceServer
}

// ExecuteHeavyCalculation CPU-Heavy 연산을 수행하는 핸들러 함수
func (s *CPUHeavyServiceServer) ExecuteHeavyCalculation(ctx context.Context, req *pb.HeavyCalculationRequest) (*pb.HeavyCalculationResponse, error) {

	result := utils.HeavyCalculation(req.GetComplexityLevel())

	log.Printf("INFO: Calculation completed. Checksum: %d", result)

	return &pb.HeavyCalculationResponse{
		Success:        true,
		ResultChecksum: result,
	}, nil
}
