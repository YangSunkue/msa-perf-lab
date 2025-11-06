import http from 'k6/http';
import { check } from 'k6';

/*
  grpc 단일 테스트용 스크립트 파일입니다.

  실행 예시:
    테스트 + 데이터 저장: k6 run --out influxdb=http://localhost:8086/k6 tests/end_to_end/rest_vs_grpc/k6_grpc.js
    테스트만: k6 run tests/end_to_end/rest_vs_grpc/k6_grpc.js
*/

const RATE = __ENV.RATE ? parseInt(__ENV.RATE) : 100;
const DURATION = __ENV.DURATION ? __ENV.DURATION : '30s';

export const options = {
    scenarios: {
        grpc_ping_test: {
            executor: 'constant-arrival-rate',
            rate: RATE,                 // 초당 요청 수
            timeUnit: '1s',             // rate 기준 단위
            duration: DURATION,         // 전체 테스트 시간
            preAllocatedVUs: 50,        // 최소 VU
            maxVUs: 200                 // 최대 VU
        }
    },
    thresholds: {
        'http_req_duration': ['p(95)<500'], // 전체 요청 95%의 응답속도는 500ms 미만이어야 함
        'http_req_failed': ['rate<0.02']    // 실패율 2% 미만이어야 함
    }
};

export default function () {
    const url = 'http://localhost:5001/grpc/ping';

    const payload = JSON.stringify({
        size: 1000000
    });

    const params = {
        tags: { payload_size: '1000000', protocol: 'grpc'},
        headers: {
            'Content-Type': 'application/json',
            'Accpet': 'application/json',
            'User-Agent': 'k6-grpc-test'
        }
    };

    const res = http.post(url, payload, params);

    // 성공/실패 체크 함수
    check(res, {
        'status is 200': (r) => r.status === 200,
        'response not empty': (r) => r.body && r.body.length > 0
    });
}