import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect

# import redis
# from flask_session import Session

# -- ---------------------------------------------------------------------------------
# -- Script Name : Ldap Authentication with FLask
# -- Author      : *******
# -- Date        : *******
# -- ---------------------------------------------------------------------------------
# -- Description : Authenticate users with Flask
# -- ---------------------------------------------------------------------------------
# -- Version History
# -- ===============
# --
# -- Who      		    version     Date      Description. 3
# -- ===       		    =======     ======    ======================
# -- XXXXXXXX             1.0       Jan 21    Initial Version.
# -- ---------------------------------------------------------------------------------


current_path = os.environ['PATH']
print(current_path)

# -- ---------------------------------------------------------------------------------
# -- Function    : Initiate the App C:\Users\p784138\AWS\Non-Prod\
# -- ---------------------------------------------------------------------------------
app = Flask(__name__,
            template_folder="C:\\Users\\sasan\\PycharmProjects\\Flask-Ldap\\templates",
            root_path="C:\\Users\\sasan\\PycharmProjects\\Flask-Ldap\\Flask-Ldap"
            )


bootstrap = Bootstrap(app)
app.config.from_object('settings')
app.secret_key = os.urandom(24)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

csrf = CSRFProtect(app)

print('Inside __init__py')

from main import app
