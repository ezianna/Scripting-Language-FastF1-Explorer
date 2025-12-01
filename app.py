from flask import Flask
from routes.home import home_bp
from routes.race import race_bp
from routes.lap import lap_bp
from routes.telemetry import telemetry_bp
from routes.comparison import comparison_bp

def create_app():
    app = Flask(__name__)

    # Register routes
    app.register_blueprint(home_bp)
    app.register_blueprint(race_bp)
    app.register_blueprint(lap_bp)
    app.register_blueprint(telemetry_bp)
    app.register_blueprint(comparison_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
