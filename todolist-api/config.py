import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:postgres@localhost:5432/tododb"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
     # Flask-Smorest / OpenAPI
    API_TITLE = "Todo API"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.3"

    OPENAPI_URL_PREFIX = "/"
    OPENAPI_SWAGGER_UI_PATH = "/docs"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"