from app import app, db
from models.user import User

with app.app_context():
    users = [
        User(username='양선규', email='ysk9526@gmail.com'),
        User(username='최주희', email='wngmlchoi@gmail.com'),
        User(username='양선희', email='sunhee@gmail.com'),
    ]
    db.session.add_all(users)
    db.session.commit()
    print("데이터가 성공적으로 삽입되었습니다!")