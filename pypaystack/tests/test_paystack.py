import os
from  unittest import TestCase
from pypaystack import Customer, Transaction, Plan


BASE_URL = "https://api.paystack.co"

class TestTransaction(TestCase):
   
    def setUp(self):
        super(TestTransaction, self).setUp()
        self.test_auth_key = os.getenv('PAYSTACK_AUTHORIZATION_KEY', None)
        self.transaction = Transaction()
        
 
    def test_charge(self):
        (status_code, _ , _, _) = self.transaction.charge("AUTH_invalidcode", "customer@cloud.com", 1000)
        self.assertEqual(status_code, 400)


    def test_verify(self):
       pass

# Todo: Finish this tests and actually test....:-(

