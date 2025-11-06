import http from 'k6/http';
import { check } from 'k6';

const RATE = __ENV.RATE ? parseInt(__ENV.RATE) : 100;
const DURATION = __ENV.DURATION ? __ENV.DURATION : '30s';

// 쉘스크립트에서 넘겨줄 값들
const PAYLOAD_SIZE = __ENV.PAYLOAD_SIZE ? parseInt(__ENV.PAYLOAD_SIZE) : 10;
const SCENARIO_NAME = __ENV.SCENARIO_NAME || `grpc_ping_test_${PAYLOAD_SIZE}`;

export const options = {
    scenarios: {
        [SCENARIO_NAME]: {
            executor: 'constant-arrival-rate',
            rate: RATE,
            timeUnit: '1s',
            duration: DURATION,
            preAllocatedVUs: 50,
            maxVUs: 200,
            tags: {
                payload_size: `${PAYLOAD_SIZE}`,
                protocol: 'grpc'
            }
        }
    },
    thresholds: {
        'http_req_duration': ['p(95)<500'],
        'http_req_failed': ['rate<0.02']
    }
};

export default function () {
    const url = 'http://localhost:5001/grpc/ping';

    const payload = JSON.stringify({
        size: PAYLOAD_SIZE
    });

    const params = {
        tags: { payload_size: `${PAYLOAD_SIZE}`, protocol: 'grpc' },
        headers: {
            'Content-Type': 'application/json',
            'Accpet': 'application/json',
            'User-Agent': 'k6-grpc-test'
        }
    };

    const res = http.post(url, payload, params);

    check(res, {
        'status is 200': (r) => r.status === 200,
        'response not empty': (r) => r.body && r.body.length > 0
    });
}
