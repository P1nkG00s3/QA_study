import pytest

from src.candies.schemas import CandySchema
from src.candies.service import CandiesService
from src.db import Base, engine
from src.candies.models import Candies

from src.config import settings


@pytest.fixture(scope="session", autouse=True)
def setup_dp():
    print(f'{settings.DB_NAME=}')
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
