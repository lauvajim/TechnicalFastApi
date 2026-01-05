from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import get_password_hash

def create_initial_user(db: Session):
    email = "admin@test.com"

    user = db.query(User).filter(User.email == email).first()
    if not user:
        user = User(
            email=email,
            hashed_password=get_password_hash("admin123")
        )
        db.add(user)
        db.commit()
