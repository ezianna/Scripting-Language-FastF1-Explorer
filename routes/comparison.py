from flask import Blueprint, render_template, request
from services.telemetry_utils import compare_telemetry
from services.plot_utils import plot_compare

comparison_bp = Blueprint('comparison', __name__, url_prefix="/compare")

@comparison_bp.route("/", methods=["GET", "POST"])
def compare():
    fig = None
    error = None
    try:
        if request.method == "POST":
            year = int(request.form["year"])
            gp = request.form["gp"]
            a = request.form["driver_a"]
            b = request.form["driver_b"]

            telA, telB = compare_telemetry(year, gp, a, b)
            fig = plot_compare(telA, telB, a, b)
    except Exception as e:
        error = str(e)

    return render_template("comparison.html", fig=fig, error=error)
