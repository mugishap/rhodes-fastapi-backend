from sqlalchemy.orm import Session

from api.models.user import User, UserSchema

def post(db_session: Session, payload: UserSchema):
    user = User(names=payload.names, email=payload.email, address=payload.email, mobile = payload.mobile, password=payload.password)
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user


def get(db_session: Session, id: int):
    return db_session.query(User).filter(User.id == id).first()


def get_all(db_session: Session):
    return db_session.query(User).all()


def put(db_session: Session, user: User, title: str, description: str):
    user.names = names
    user.email = email
    user.address = address
    user.mobile = mobile
    db_session.commit()
    return user


def delete(db_session: Session, id: int):
    user = db_session.query(User).filter(User.id == id).first()
    db_session.delete(user)
    db_session.commit()
    return user


