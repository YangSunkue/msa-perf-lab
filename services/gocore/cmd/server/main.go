// Package main
package main

import (
	"gocore/internal/router"
	servicegrpc "gocore/internal/service/grpc"
	"gocore/internal/service/mq"
	pb "gocore/pkg/proto"
	"log"
	"net"
	"net/http"

	"google.golang.org/grpc"
	"google.golang.org/grpc/reflection"
)

func main() {

	// gRPC 서버 시작
	go func() {
		lis, err := net.Listen("tcp", ":50051")
		if err != nil {
			log.Fatalf("failed to listen: %v", err)
		}

		grpcServer := grpc.NewServer()
		pb.RegisterCoreServiceServer(grpcServer, &servicegrpc.CoreServiceServer{})
		pb.RegisterCpuHeavyServiceServer(grpcServer, &servicegrpc.CPUHeavyServiceServer{})

		reflection.Register(grpcServer)

		log.Println("gRPC server started on port 50051")
		if err := grpcServer.Serve(lis); err != nil {
			log.Fatalf("failed to serve gRPC: %v", err)
		}
	}()

	// RabbitMQ Consumer 시작
	go mq.StartConsumer()

	// REST 서버 시작
	r := router.SetupRouter()

	log.Println("Rest server started on port 8080")
	if err := http.ListenAndServe(":8080", r); err != nil {
		log.Fatalf("failed to start REST server: %v", err)
	}
}
