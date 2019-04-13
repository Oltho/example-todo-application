from api.app_file import get_app


def run_app():
    app = get_app()
    app.run(port=8000)

if __name__ == '__main__':
    run_app()
