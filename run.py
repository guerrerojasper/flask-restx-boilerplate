from app import create_app

app = create_app(
    config_class='app.config.DevelopmentConfig'
)

if __name__ == '__main__':
    app.run()


"""
notes:
 - mongoengine 
   - pip install git+https://github.com/idoshr/flask-mongoengine.git@1.0.1
"""