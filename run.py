from app import create_app

app = create_app(
    config_class='app.config.DevelopmentConfig'
)

if __name__ == '__main__':
    app.run()