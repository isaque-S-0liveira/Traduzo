from flask import Blueprint, render_template, request
from models.language_model import LanguageModel
from deep_translator import GoogleTranslator

# from models.history_model import HistoryModel


translate_controller = Blueprint("translate_controller", __name__)


def translate_text(tr_to, tr_from, text):
    translated = GoogleTranslator(source=tr_from, target=tr_to).translate(text)
    return translated


# Reqs. 4 e 5
@translate_controller.route("/", methods=["GET", "POST"])
def index():
    languages = LanguageModel.list_dicts()
    default_text = ""
    default_translate_from = "en"
    default_translate_to = "pt"
    translated = "Tradução"

    if request.method == "POST":
        text_to_translate = request.form.get("text-to-translate", default_text)
        translate_from = request.form.get(
            "translate-from", default_translate_from
        )
        translate_to = request.form.get("translate-to", default_translate_to)
        translated = translate_text(
            translate_to, translate_from, text_to_translate
        )
        return render_template(
            "index.html",
            languages=languages,
            text_to_translate=text_to_translate,
            translate_from=translate_from,
            translate_to=translate_to,
            translated=translated,
        )

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
    languages = LanguageModel.list_dicts()

    if request.method == "POST":
        text_to_translate = request.form.get("text-to-translate")
        translate_to = request.form.get("translate-from")
        translate_from = request.form.get("translate-to")
        old_translate = translate_text(
            translate_to, translate_from, text_to_translate
        )
        translated = translate_text(
            translate_from, translate_to, text_to_translate
        )
        return render_template(
            "index.html",
            languages=languages,
            text_to_translate=translated,
            translate_from=translate_from,
            translate_to=translate_to,
            translated=old_translate,
        )
