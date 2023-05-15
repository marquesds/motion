from motion import create_app

application = create_app()


application.run(port=9000, debug=True)
