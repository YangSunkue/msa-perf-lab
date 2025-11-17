from faker import Faker
import random, json
from app import app
from models import db, User

fake = Faker()

def seed_users(count: int=1_000_000):
    """User 테이블에 더미 데이터 삽입

    80%는 100개의 공통 이메일 사용 (Cache Hit 유도)
    20%는 유니크 이메일

    Args:
        count (int, optional): 삽입할 데이터 수. Defaults to 1_000_000.
    """
    print(f'{count:,}개의 User 데이터 생성 시작...')

    # 자주 조회될 이메일 100개 생성
    common_emails = [fake.email() for _ in range(100)]
    common_usernames = [fake.user_name() for _ in range(100)]

    users = []
    for i in range(count):
        if i % 10 < 8:  # 80%는 common 데이터
            email = random.choice(common_emails)
        else:
            email = fake.email()
        
        username = f'user_{i}'
        
        users.append(User(
            username=username,
            email=email
        ))

        # 10,000개씩 배치 커밋 (메모리 절약)
        if (i + 1) % 10_000 == 0:
            db.session.bulk_save_objects(users)
            db.session.commit()
            users = []
            print(f'{i + 1:,}개 삽입 완료')
    
    if users:
        db.session.bulk_save_objects(users)
        db.session.commit()
    
    print(f'총 {count:,}개 User 데이터 생성 완료!')

    # 공통 이메일을 JSON 파일로 저장
    with open('common_emails.json', 'w') as f:
        json.dump(common_emails, f, indent=2)
    
    print("common_emails.json 파일 생성 완료")


if __name__ == "__main__":
    with app.app_context():
        # 기존 데이터 삭제 (옵션)
        db.drop_all()
        db.create_all()
        
        seed_users(1_000_000)