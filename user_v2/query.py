from user_v2.user_storage import UserStorage
from user_v2.sq_uow import Session, SQAAUnitOfWork
from user_v2.models import UserName, User

class SQAAUserStorage(UserStorage):
    @staticmethod
    def get_current_session() -> Session:
        return SQAAUnitOfWork.get_current_session()

    def get_user(self, username: UserName) -> User:
        session = self.get_current_session()
        row = session.query(User).filter_by(username=username).one()
        return row

    def create_user(self, user: User) -> None:
        session = self.get_current_session()
        session.add(user)

    def user_exists(self, username: UserName) -> bool:
        session = self.get_current_session()
        return session.query(User).filter(User.username == username).count() > 0
