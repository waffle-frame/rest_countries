# Importing the necessary modules and libraries
import os
from dotenv import load_dotenv
from flask import Flask
from routes.blueprint import blueprint

load_dotenv()

def create_app():
    app = Flask(__name__)  # flask app object
    
    # app.config.from_prefixed_env(".env")
    app.config.update(**os.environ)
    # app.config = os.environ
    return app


# Creating the app
app = create_app()
# redis = Redis(
#     host=app.config.get("REDIS_HOST"),  # type: ignore
#     port=app.config.get("REDIS_PORT"),  # tyrepe: ignore
#     db=app.config.get("REDIS_DATABASE")  # type: ignore
# )

app.register_blueprint(blueprint, url_prefix='/api')


# Running the app
if __name__ == '__main__':
    app.run(
        host=app.config.get("SERVER_HOST"),
        port=app.config.get("SERVER_PORT"),
        debug=app.config.get("SERVER_DEBUG_MODE"),
    )
