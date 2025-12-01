from flask import Blueprint, render_template, request
from services.fastf1_loader import load_session

lap_bp = Blueprint('lap', __name__, url_prefix="/lap")

@lap_bp.route("/", methods=["GET", "POST"])
def lap():
    laps = None
    error = None
    try:
        if request.method == "POST":
            year = int(request.form["year"])
            gp = request.form["gp"]
            driver = request.form["driver"]

            session = load_session(year, gp, "R")
            laps = session.laps.pick_driver(driver)
    except Exception as e:
        error = str(e)

    return render_template("lap.html", laps=laps, error=error)
