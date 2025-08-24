from abc import ABC, abstractmethod
from user_v2.models import User, UserName
from user_v2.unit_of_work import UnitOfWorkFactory
from user_v2.models import using_validation_context

class UserStorage(ABC):
    @abstractmethod
    def get_user(self, username: UserName) -> User:
        raise NotImplementedError()

    @abstractmethod
    def create_user(self, user: User) -> None:
        raise NotImplementedError()

    @abstractmethod
    def user_exists(self, username: UserName) -> bool:
        raise NotImplementedError()

class CreateUserUsecase:
    def __init__(
        self, user_storage: UserStorage, uow_factory: UnitOfWorkFactory
    ) -> None:
        self.user_storage = user_storage
        self.uow_factory = uow_factory

    def execute(self, user: User) -> None:
        with self.uow_factory() as uow:

            with using_validation_context(False):
                if self.user_storage.user_exists(user.username):
                    raise ValueError("User already exists")

                self.user_storage.create_user(user)
                uow.commit()
