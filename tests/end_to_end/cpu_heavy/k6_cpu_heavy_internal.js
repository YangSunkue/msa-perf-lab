import http from 'k6/http';
import { check } from 'k6';

/*
  CPU Heavy Internal 테스트용 스크립트 파일입니다.

  실행 예시:
    k6 run --out influxdb=http://localhost:8086/k6 tests/end_to_end/cpu_heavy/k6_cpu_heavy_internal.js
    환경변수: RATE=50 DURATION=1m k6 run ...
*/

// 고정값
const DURATION = __ENV.DURATION || '30s';
const RATE = __ENV.RPS ? parseInt(__ENV.RPS) : 50;

// 변동값
const COMPLEXITY_LEVEL = __ENV.COMPLEXITY_LEVEL ? parseInt(__ENV.COMPLEXITY_LEVEL) : 1;
const SCENARIO_NAME = __ENV.SCENARIO_NAME || `cpu_heavy_internal_test_${COMPLEXITY_LEVEL}`;

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
        'http_req_duration': ['p(95)<2000'],
        'http_req_failed': ['rate<0.02']
    }
};

export default function () {
    const url = 'http://localhost:5001/internal/cpu_heavy';

    const payload = JSON.stringify({
        complexity_level: COMPLEXITY_LEVEL
    });

    const params = {
        tags: { type: 'internal', protocol: 'rest' },
        headers: {
            'Content-Type': 'application/json'
        }
    };

    const res = http.post(url, payload, params);

    check(res, {
        'status is 200': (r) => r.status === 200,
        'has status accepted': (r) => r.json('status') === 'ok'
    });
}