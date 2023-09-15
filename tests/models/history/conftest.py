from src.database.db import db
from src.models.history_model import HistoryModel

import pytest


@pytest.fixture(autouse=True)
def prepare_base():
    db.get_collection("history").drop()
    HistoryModel(
        {
            '_id': '6503c230af44b9952872f0ad',
            "text_to_translate": "Hello, I like videogame",
            "translate_from": "en",
            "translate_to": "pt",
        }
    ).save()

    HistoryModel(
        {
            '_id': '6503c230af44b9952872f0ae',
            "text_to_translate": "Do you love music?",
            "translate_from": "en",
            "translate_to": "pt",
        }
    ).save()
