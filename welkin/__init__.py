from welkin.api_resources import *  # noqa
from welkin.auth import Auth

# Welkin Python bindings
# API docs at http://
# Authors:


# Configuration variables
client_id = None
client_secret = None
scope = 'all'
api_base = "https://api.welkinhealth.com"
api_version = "v1"
authorization = "https://api.welkinhealth.com/v1/token"


# Set to either 'debug' or 'info', controls console logging
log = None


# Sets some basic information about the running application that's sent along
# with API requests. Useful for plugin authors to identify their plugin when
# communicating with Stripe.
#
# Takes a name and optional version and plugin URL.

def set_app_info(name, partner_id=None, url=None, version=None):
    global app_info
    app_info = {
        "name": name,
        "partner_id": partner_id,
        "url": url,
        "version": version,
    }
