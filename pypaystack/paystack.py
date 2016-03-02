import requests
import json
import os

from .errors import InvalidAmountError, MissingAuthKeyError
 
class Transaction(object):

    """
    This class is used to represent all the activitivies that
    can be performed on behalf of a user, given the user's email and 
    their AUTH Code
    """

    _PAYSTACK_AUTHORIZATION_KEY = os.getenv('PAYSTACK_AUTHORIZATION_KEY', None)
    _CONTENT_TYPE = "application/json"

    #Endpoint URLs
    _CHARGING_URL = "https://api.paystack.co/transaction/charge_authorization"
    _VERIFICATION_URL = "https://api.paystack.co/transaction/verify/"

    def __init__(self, email, auth_code):
        self._email = email
        self._auth_code = auth_code
        if not self._PAYSTACK_AUTHORIZATION_KEY:
            raise MissingAuthKeyError("Set your authorization key as environment variable PAYSTACK_AUTHORIZATION_KEY")


    def _headers(self, authorization_key=None, content_type=None):
        if authorization_key is None:
            authorization_key = self._PAYSTACK_AUTHORIZATION_KEY
        if content_type is None:
            content_type = self._CONTENT_TYPE
        return {"Content-Type": content_type, "Authorization": "Bearer " + authorization_key}


    def _parse_json(self,json_string):
        """
        This function takes in every json response sent back by the
        server and trys to get out the important return variables
        """
        parsed_response = json.loads(json_string)

        status = parsed_response.get('status', None)
        message = parsed_response.get('message', None)
        data = parsed_response.get('data', None)

        return status, message, data


    def charge(self, amount):
        """
        Charges a customer and returns the response
        in a python tuple object
        
        status_code, status, message, data (dict of customer information)
        """
        if isinstance(amount, int) or isinstance(amount, float):
            if amount < 0:
                raise InvalidAmountError("Negative amount is not allowed")
        else:
            raise InvalidAmountError("Amount should be a number")

        payload = {"authorization_code":self._auth_code, "email":self._email, "amount": amount}
        r = requests.post(self._CHARGING_URL, headers=self._headers(), data=json.dumps(payload))

        status, message, data = self._parse_json(r.content)
        status_code = r.status_code

        return status_code, status, message, data 

     
    def verify(self, reference):
        """
        Verifies a transaction using the provided reference number
        and returns a python tuple object.
        
        status_code, status, message, data (dict of customer information)
        """
        reference = str(reference)
        r = requests.get(self._VERIFICATION_URL + reference, headers=self._headers())
        status, message, data = self._parse_json(r.content)
        status_code = r.status_code

        return status_code, status, message, data 

