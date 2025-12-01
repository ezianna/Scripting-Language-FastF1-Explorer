from flask import Blueprint, render_template, request, current_app
from services.fastf1_loader import load_session
import pandas as pd

race_bp = Blueprint('race', __name__, url_prefix="/race")


def _find_column(df, candidates):
    """Return the first matching column name in df from candidates (case-insensitive)."""
    cols = list(df.columns)
    lc = {c.lower(): c for c in cols}
    for cand in candidates:
        if cand.lower() in lc:
            return lc[cand.lower()]
    return None


@race_bp.route("/", methods=["GET", "POST"])
def race():
    data = None
    error = None
    try:
        if request.method == "POST":
            year = int(request.form["year"])
            gp = request.form["gp"]
            session = request.form["session"]

            ses = load_session(year, gp, session)
            res = ses.results

            # Log available columns to help debugging
            try:
                current_app.logger.info(f"race.results columns: {list(res.columns)}")
            except Exception:
                print("race.results columns:", list(res.columns))

            # Create a display DataFrame with normalized column names
            display = pd.DataFrame()

            # Position
            if 'Position' in res.columns:
                display['Position'] = res['Position']
            else:
                display['Position'] = range(1, len(res) + 1)

            # Driver name candidates
            driver_candidates = ['Driver', 'FullName', 'Fullname', 'Name', 'Abbreviation', 'Abbr', 'DriverName', 'Driver Name']
            drv_col = _find_column(res, driver_candidates)
            if drv_col:
                display['Driver'] = res[drv_col].astype(str)
            else:
                # Try to construct from 'GivenName'/'FamilyName' if present
                if 'GivenName' in res.columns and 'FamilyName' in res.columns:
                    display['Driver'] = res['GivenName'].astype(str) + ' ' + res['FamilyName'].astype(str)
                else:
                    display['Driver'] = 'N/A'

            # Team/Constructor candidates
            team_candidates = ['Team', 'Constructor', 'TeamName', 'Team Name', 'ConstructorName']
            team_col = _find_column(res, team_candidates)
            if team_col:
                display['Team'] = res[team_col].astype(str)
            else:
                # try 'Car' or 'CarNumber' fallback
                display['Team'] = 'N/A'

            # Points
            if 'Points' in res.columns:
                display['Points'] = res['Points']
            elif 'points' in res.columns:
                display['Points'] = res['points']
            else:
                display['Points'] = None

            data = display.reset_index(drop=True)
    except Exception as e:
        error = str(e)

    return render_template("race.html", race_data=data, error=error)
