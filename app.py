from flask import Flask, jsonify
import os

from lib.whoami import Whoami

APP = Flask(__name__)
APP.config["JSONIFY_PRETTYPRINT_REGULAR"] = True

WHOAMI = Whoami()


@APP.route("/")
def _index():
    # Confirms the app is reachable
    return "Working"


@APP.route("/api/whoami")
def _get_whoami():
    # Maps the whoami output to /api/whoami
    return jsonify(WHOAMI.to_json())


if __name__ == "__main__":
    # For testing/debugging
    APP.run(host="0.0.0.0", port=os.environ.get("PORT") or 5000)
