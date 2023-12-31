import pytest
from pathlib import Path
from tempfile import TemporaryDirectory
import cards


@pytest.fixture()
def some_data():
    """Return answer to ultimate question."""
    return 42

def test_some_data(some_data):
    """Use fixture return value in a test."""
    assert some_data == 42

# -- this code was tranfered to conftest.py file and use a session scope
# @pytest.fixture(scope="module")
# def cards_db():
#     with TemporaryDirectory() as db_dir:
#         db_path = Path(db_dir)
#         db = cards.CardsDB(db_path)
#         yield db
#         db.close()

def test_empty(cards_db):
    assert cards_db.count() == 0

def test_two(cards_db):
    cards_db.add_card(cards.Card("first"))
    cards_db.add_card(cards.Card("second"))
    assert cards_db.count() == 2
