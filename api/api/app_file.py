import connexion


def get_app():
    """Get an API instance of the Todo APP"""
    app = connexion.FlaskApp(__name__, specification_dir='openapi/')
    app.add_api('api.yaml')

    return app
