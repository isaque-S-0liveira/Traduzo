import json
from src.models.history_model import HistoryModel


# Req. 7
def test_request_history():
    history_json = HistoryModel.list_as_json()
    expected_data = [
        {
            "_id": "6503c230af44b9952872f0ad",
            "text_to_translate": "Hello, I like videogame",
            "translate_from": "en",
            "translate_to": "pt",
        },
        {
            "_id": "6503c230af44b9952872f0ae",
            "text_to_translate": "Do you love music?",
            "translate_from": "en",
            "translate_to": "pt",
        },
    ]
    history_data = json.loads(history_json)
    assert history_data == expected_data
