import http from 'k6/http';
import { check } from 'k6';

/*
  MQ 동기 처리 테스트용 스크립트 파일입니다.

  실행 예시:
    k6 run --out influxdb=http://localhost:8086/k6 tests/end_to_end/mq_async/k6_mq_sync.js
    환경변수: RATE=50 DURATION=1m k6 run ...
*/

const DURATION = __ENV.DURATION ? __ENV.DURATION : '30s';

// 쉘스크립트에서 넘겨줄 값들
const RATE = __ENV.RPS ? parseInt(__ENV.RPS) : 50;
const SCENARIO_NAME = __ENV.SCENARIO_NAME || `mq_sync_test_${RATE}`;

export const options = {
    scenarios: {
        [SCENARIO_NAME]: {
            executor: 'constant-arrival-rate',
            rate: RATE,
            timeUnit: '1s',
            duration: DURATION,
            preAllocatedVUs: 50,
            maxVUs: 100
        }
    },
    thresholds: {
        'http_req_duration': ['p(95)<3000'],  // 95%가 3초 이내 (1초 sleep 고려)
        'http_req_failed': ['rate<0.1']
    }
};

export default function () {
    const url = 'http://localhost:5001/rest/mq_async/sync';

    const payload = JSON.stringify({
        action: 'delay'
    });

    const params = {
        tags: { type: 'sync', protocol: 'rest' },
        headers: {
            'Content-Type': 'application/json'
        }
    };

    const res = http.post(url, payload, params);

    check(res, {
        'status is 200': (r) => r.status === 200,
        'has go_response': (r) => r.json('go_response') !== undefined
    });
}