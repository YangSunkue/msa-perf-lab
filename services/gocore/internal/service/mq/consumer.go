// Package mq
package mq

import (
	"encoding/json"
	"gocore/pkg/utils"
	"log"
	"os"

	amqp "github.com/rabbitmq/amqp091-go"
)

const queueName = "mq_async_tasks"

// StartConsumer RabbitMQ consumer 시작
func StartConsumer() {

	// RabbitMQ 접속 정보
	mqUser := os.Getenv("MQ_USER")
	mqPassword := os.Getenv("MQ_PASSWORD")
	mqHost := os.Getenv("MQ_HOST")
	mqPort := os.Getenv("MQ_PORT")

	connURL := "amqp://" + mqUser + ":" + mqPassword + "@" + mqHost + ":" + mqPort + "/"

	// 연결
	conn, err := amqp.Dial(connURL)
	if err != nil {
		log.Fatalf("Failed to connect to RabbitMQ: %v", err)
	}
	defer conn.Close()

	// 채널 생성
	ch, err := conn.Channel()
	if err != nil {
		log.Fatalf("Failed to open a channel: %v", err)
	}
	defer ch.Close()

	// 큐 선언
	q, err := ch.QueueDeclare(
		queueName, // name
		true,      // durable
		false,     // delete when unused
		false,     // exclusive
		false,     // no-wait
		nil,       // arguments
	)
	if err != nil {
		log.Fatalf("Failed to declare a queue: %v", err)
	}

	// 메시지 수신
	// msgs(컨슈머)는 스트림 형태로 동작하며, 메시지가 삽입될 시 Notification을 받아 즉시 처리 가능하게 한다.
	msgs, err := ch.Consume(
		q.Name, // queue
		"",     // consumer
		false,  // auto-ack (false - 수동 ack)
		false,  // exclusive
		false,  // no-loacl
		false,  // no-wait
		nil,    // args
	)
	if err != nil {
		log.Fatalf("Failed to register a consumer: %v", err)
	}

	log.Printf("RabbitMQ Consumer started. Waiting for messages...")

	// 메시지 처리 (goroutine 활용 병렬 처리)
	// 메인 고루틴과 별개로 실행되며, 큐에 메시지가 들어오면 감지해 즉시 처리
	go func() {
		for msg := range msgs {
			// 각 메시지를 goroutine으로 처리
			go func(m amqp.Delivery) {
				processMessage(m)
			}(msg)
		}
	}()

	// 버퍼 없는 채널 생성하여 무한 대기
	// 메인 고루틴이 중지되지 않게 하여, 메시지 처리 로직이 계속 돌게 한다
	forever := make(chan bool)
	<-forever
}

// processMessage 메시지 처리
func processMessage(msg amqp.Delivery) {
	var task map[string]interface{}

	// JSON 파싱
	if err := json.Unmarshal(msg.Body, &task); err != nil {
		log.Printf("Failed to parse message: %v", err)
		msg.Nack(false, false) // 재시도 안 함
		return
	}

	log.Printf("Processing task: %v", task)

	// 비즈니스 로직 대체 유틸 (1초 대기)
	utils.SleepForOneSecond()

	log.Printf("Task completed: %v", task)

	// 처리 완료 확인 (Ack)
	msg.Ack(false)
}
