from flask import Blueprint, render_template, request
from services.telemetry_utils import get_driver_telemetry
from services.plot_utils import plot_telemetry

telemetry_bp = Blueprint('telemetry', __name__, url_prefix="/telemetry")

@telemetry_bp.route("/", methods=["GET", "POST"])
def telemetry():
    fig = None
    error = None
    try:
        if request.method == "POST":
            year = int(request.form["year"])
            gp = request.form["gp"]
            driver = request.form["driver"]

            tel = get_driver_telemetry(year, gp, driver)
            fig = plot_telemetry(tel)
    except Exception as e:
        error = str(e)

    return render_template("telemetry.html", fig=fig, error=error)
