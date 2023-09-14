from flask import Blueprint, render_template, request
from models.language_model import LanguageModel

# from deep_translator import GoogleTranslator

# from models.history_model import HistoryModel


translate_controller = Blueprint("translate_controller", __name__)


# Reqs. 4 e 5
@translate_controller.route("/", methods=["GET", "POST"])
def index():
    languages = LanguageModel.find()
    default_text = "O que deseja traduzir"
    default_translate_from = "en"
    default_translate_to = "pt"
    translated = "Tradução"

    if request.method == "POST":
        text_to_translate = request.form.get("text-to-translate", default_text)
        translate_from = request.form.get(
            "translate-from", default_translate_from
        )
        translate_to = request.form.get("translate-to", default_translate_to)
    else:
        text_to_translate = default_text
        translate_from = default_translate_from
        translate_to = default_translate_to

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated,
    )


# Req. 6
@translate_controller.route("/reverse", methods=["POST"])
def reverse():
    raise NotImplementedError
