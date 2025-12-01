from flask import Blueprint

def register_blueprints(app):
    from .home import home_bp
    from .race import race_bp
    from .lap import lap_bp
    from .telemetry import telemetry_bp
    from .comparison import comparison_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(race_bp)
    app.register_blueprint(lap_bp)
    app.register_blueprint(telemetry_bp)
    app.register_blueprint(comparison_bp)
