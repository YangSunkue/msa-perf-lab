from sqlalchemy import select
from models import db, User

def count_users_by_email(email: str) -> int:
    """이메일로 사용자 수를 조회합니다.

    Args:
        email (str): 사용자 이메일

    Returns:
        int: 해당 이메일을 가진 사용자 수
    """
    stmt = select(db.func.count()).select_from(User).where(User.email == email)
    count = db.session.scalar(stmt)

    return count