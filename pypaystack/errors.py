class PyPaystackError(Exception):
    """
    Python Paystack Error
    """
    pass

class InvalidAmountError(PyPaystackError):
    """
    Invalid amount error"
    """
    pass

class MissingAuthKeyError(PyPaystackError):
    pass

