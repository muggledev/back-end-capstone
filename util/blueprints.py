import routes

def register_blueprints(app):
    app.register_blueprint(routes.artifacts)
    app.register_blueprint(routes.auth_tokens)
    app.register_blueprint(routes.caretakers)
    app.register_blueprint(routes.dark_creatures)
    app.register_blueprint(routes.light_creatures)
    app.register_blueprint(routes.magical_preserves)
    app.register_blueprint(routes.preserve_artifacts_xref)
    app.register_blueprint(routes.users)
