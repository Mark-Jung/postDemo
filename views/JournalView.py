import json

from flask import request
from flask.views import MethodView

from utils.parser import ReqParser

from controllers.JournalController import JournalController


class JournalView(): 

    @classmethod
    def new_journal(cls):

        data = json.loads(request.data.decode('utf-8'))
        req_params = ["title", "text", "longitude", "latitude"]
        if not ReqParser.check_body(data, req_params):
            return json.dumps({"error_message": "ill-formed request"}), 400

        err, status, response = JournalController.new_journal(data)        

        if err:
            return json.dumps({"error_message": err}), status

        return json.dumps({"response": "Success"}), 201


