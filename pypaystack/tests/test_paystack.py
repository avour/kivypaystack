import os
from  unittest import TestCase
from pypaystack import Customer, Transaction, Plan


BASE_URL = "https://api.paystack.co"

class TestTransaction(TestCase):
   
    def setUp(self):
        super(TestPaystack, self).setUp()
        self.test_auth_key = os.getenv('PAYSTACK_AUTHORIZATION_KEY', None)
        self.transaction = Transaction()
        
 
    def test_charge(self):
        self.transaction
        (status_code, _ , _, _) = self.transaction.charge("AUTH_mwei8io4", "ahmedrazaq@cloud.com", 1000)
        self.assertEqual(status_code, 200)


    def test_verify(self):
       pass

# Todo: Finish this tests and actually test....:-(

