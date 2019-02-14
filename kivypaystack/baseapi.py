import os
# import requests
import json
from kivypaystack import version
 
from .errors import *

from kivy.network.urlrequest import UrlRequest
import urllib

class BaseAPI(object):

    """
    Base class for the kivypaystack python API wrapper for paystack
    Not to be instantiated directly.
    """

    _CONTENT_TYPE = "application/json"
    _BASE_END_POINT = "https://api.paystack.co"


    def __init__(self, authorization_key=None, callback=None):
        if authorization_key:
            self._PAYSTACK_AUTHORIZATION_KEY = authorization_key
        else:
            self._PAYSTACK_AUTHORIZATION_KEY = os.getenv('PAYSTACK_AUTHORIZATION_KEY', None)
        if not self._PAYSTACK_AUTHORIZATION_KEY:
            raise MissingAuthKeyError("Missing Authorization key argument or env variable")


    def _url(self, path):
        return self._BASE_END_POINT + path


    def _headers(self):
        return { 
                "Content-Type": self._CONTENT_TYPE, 
                "Authorization": "Bearer " + self._PAYSTACK_AUTHORIZATION_KEY,
                "user-agent": "pyPaystack-{}".format(version.__version__)
                }


    def _parse_json(self, response_obj):
        """
        This function takes in every json response sent back by the
        server and trys to get out the important return variables

        Returns a python tuple of status code, status(bool), message, data
        """
        parsed_response = response_obj.json()

        status = parsed_response.get('status', None)
        message = parsed_response.get('message', None)
        data = parsed_response.get('data', None)
        #if data:
        #    message = data.get('gateway_response', None) 
        return response_obj.status_code, status, message, data


    def _handle_request(self, action, method, url, data=None):

        """
        Generic function to handle all API url calls
        Returns a python tuple of status code, status(bool), message, data
        """
        method_map = ['GET', 'POST', 'PUT', 'DELETE',]
        if method not in method_map:
            raise InvalidMethodError("Request method not recognised or implemented")

        payload = urllib.urlencode(data)
        UrlRequest(url, req_headers==self._headers(),
                    req_body=payload,
                    method=method,
                    on_error=partial(self.callback, action, 'error'),
                    on_success=partial(self.callback, action, 'error'),
                    on_failure=partial(self.callback, action, 'error'),
                    on_redirect=partial(self.callback, action, 'error'),
        )


        # response = request(url, headers=self._headers(), data=payload, verify=True)
        # if response.status_code == 404:
        #     return response.status_code, False, "The object request cannot be found", None

        # if response.status_code in [200, 201]:
        #     return self._parse_json(response)
        # else:
        #     body = response.json()
        #     return response.status_code, body.get('status'), body.get('message'), body.get('errors') 


