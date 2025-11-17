import http from 'k6/http';
import { check } from 'k6';

const RATE = __ENV.RATE ? parseInt(__ENV.RATE) : 50;
const DURATION = __ENV.DURATION || '30s';
const SCENARIO_NAME = __ENV.SCENARIO_NAME || `with_cache_${RATE}RPS`;

const commonEmails = JSON.parse(open('./common_emails.json'));

export const options = {
    scenarios: {
        [SCENARIO_NAME]: {
            executor: 'constant-arrival-rate',
            rate: RATE,
            timeUnit: '1s',
            duration: DURATION,
            preAllocatedVUs: 50,
            maxVUs: 500
        }
    },
    thresholds: {
        'http_req_duration': ['p(95)<2000'],
        'http_req_failed': ['rate<0.02']
    }
};

export default function () {
    const email = commonEmails[Math.floor(Math.random() * commonEmails.length)];
    const url = `http://localhost:5001/rest/redis-cache/with-cache/${email}`;

    const params = {
        tags: { rps: `${RATE}`, type: 'with-cache' },
        headers: {
            'Accept': 'application/json'
        }
    };

    const res = http.get(url, params);

    check(res, {
        'status is 200': (r) => r.status === 200,
        'has user_count': (r) => r.json('user_count') !== undefined
    });
}
