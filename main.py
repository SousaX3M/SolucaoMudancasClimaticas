import random

from flask import Flask, abort, redirect, render_template, request, url_for


app = Flask(__name__)

RANDOM_COUNTRIES = [
    "Brasil",
    "Canadá",
    "Estados Unidos",
    "México",
    "Argentina",
    "Colômbia",
    "Índia",
    "Indonésia",
    "Japão",
    "Quênia",
    "Austrália",
]
MAX_COUNTRY_NAME_LENGTH = 80


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analisar", methods=["POST"])
def analyze_country():
    country = request.form.get("country", "").strip()

    if not country:
        return render_template(
            "index.html",
            error="Informe o nome de um país para continuar.",
        ), 400

    if len(country) > MAX_COUNTRY_NAME_LENGTH:
        return render_template(
            "index.html",
            error="O nome do país deve ter no máximo 80 caracteres.",
        ), 400

    return redirect(url_for("country_result", country=country))


@app.route("/pais-aleatorio", methods=["POST"])
def random_country():
    country = random.choice(RANDOM_COUNTRIES)
    return redirect(url_for("country_result", country=country))


@app.route("/pais/<country>")
def country_result(country):
    country = country.strip()
    if not country or len(country) > MAX_COUNTRY_NAME_LENGTH:
        abort(404)

    return render_template("result.html", country=country)


if __name__ == "__main__":
    app.run(debug=True)
