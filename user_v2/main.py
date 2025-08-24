from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, Integer, String

from user_v2.models import User
from user_v2.sq_uow import SQAUOWFactory
from user_v2.user_storage import CreateUserUsecase
from user_v2.query import SQAAUserStorage
from user_v2.models import UserName, User, Email

def insert_data() -> None:
    mapper_registry = registry()  # type: ignore

    metadata = MetaData()

    ## The implementation must OBEY the domain model interface
    # For example, the username column has a length of 20, obeying the domain model
    users_table = Table(
        "users",
        metadata,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("username", String(20), nullable=False, unique=True),
        Column("email", String(50), nullable=False, unique=True),
    )

    mapper_registry.map_imperatively(User, users_table)

def main() -> None:
    metadata = MetaData()
    # setup
    engine = create_engine("sqlite:///:memory:")
    metadata.create_all(engine)
    session_factory = sessionmaker(bind=engine)
    uow_factory = SQAUOWFactory(session_factory=session_factory)
    user_storage = SQAAUserStorage()
    # create instances of the domain logic and injecting dependencies
    usecase = CreateUserUsecase(user_storage=user_storage, uow_factory=uow_factory)

    # execute the usecase

    username = "Lusca"
    user_mail = "lusca@gg.com"
    user = User(username=UserName(username), email=Email(user_mail))
    usecase.execute(user)

    # check the result
    # check the result
    with uow_factory() as uow:
        user = user_storage.get_user(UserName(username))
        assert user.username == "Lusca"
        assert user.email == "lusca@gg.com"


if __name__ == "__main__":
    main()
