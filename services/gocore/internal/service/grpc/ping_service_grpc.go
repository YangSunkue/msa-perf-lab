// Package servicegrpc
package servicegrpc

import (
	"context"
	pb "gocore/pkg/proto"
)

type CoreServiceServer struct {
	pb.UnimplementedCoreServiceServer
}

func (s *CoreServiceServer) Ping(ctx context.Context, req *pb.PingRequest) (*pb.PingResponse, error) {
	return &pb.PingResponse{
		Reply: req.Payload,
	}, nil
}
