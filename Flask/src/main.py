from flask_jwt_extended import jwt_required, get_jwt_identity, verify_jwt_in_request
from dotenv import load_dotenv
from WebServer import *
import os

# CONFIGS
load_dotenv()

# API CLASS (CONFIG AND ROUTES)
class API(object):

    @staticmethod
    def run():

        # CONFIGURE WEB SERVER
        web = WebServer(login=API.login, jwt_expire=os.getenv('JWT_EXPIRE'))

        # ADD YOUR ROUTES HERE
        web.add({ "url": "/public", "callback": API.api_public, "methods": ['GET'] })
        web.add({ "url": "/secure", "callback": API.api_secure, "methods": ['GET'] })

        # RUN APP
        web.run(port=os.getenv('PORT') or 8080, debug=(os.getenv('MODE') != 'production'))

    # LOGIN CALLBACK [REQUIRED]

    @staticmethod
    # VERIFY USER AND RETURN ID
    def login(username, password):

        return 1 if username == 'root' and password == '1234' else 0

    # ROUTES

    @staticmethod
    @jwt_required(optional=False) # JWT PROTECTED ROUTE
    def api_secure(req):

        try: return { "user": get_jwt_identity() }
        except Exception as e: return { "error": str(e) }

    @staticmethod # PUBLIC ROUTE
    def api_public(req):

        try: return { "message": "Welcome!" }
        except Exception as e: return { "error": str(e) }

if __name__ == '__main__':

    # RUN WEB APP
    api = API()
    api.run()
