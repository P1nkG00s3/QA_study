import pytest

from src.candies.schemas import CandySchema
from src.candies.service import CandiesService
from src.db import Base, engine
from src.candies.models import Candies

from src.config import settings


@pytest.fixture
def candies():
    candies = [
        CandySchema(title="candy1", owner="John"),
        CandySchema(title="candy2", owner="Boris"),
    ]
    return candies


@pytest.fixture
def delete_candies():
    CandiesService.delete_all()


@pytest.mark.usefixtures("delete_candies")
class TestCandies:
    def test_count(self, candies):
        for candy in candies:
            CandiesService.add(candy)
        assert CandiesService.count() == 2

    def test_list(self, candies):
        for candy in candies:
            CandiesService.add(candy)

        list_test = CandiesService.list()

        for list_elem in list_test:
            assert list_elem in candies

    def test_add(self, candies):
        CandiesService.add(CandySchema(title="candy3", owner="Vasya"))
        assert CandiesService.count() == 1

    def test_delete(self, candies):
        for candy in candies:
            CandiesService.add(candy)
        CandiesService.delete(6)
        assert CandiesService.count() == 1

    def test_get(self, candies):
        for candy in candies:
            CandiesService.add(candy)
        CandiesService.get(8)
