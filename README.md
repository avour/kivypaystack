# paystack-client

A python wrapper for Paystack API


- Charge the customer
- Verifiy a transaction

Store your authorization key in your environment variable as "PAYSTACK_AUTHORIZATION_KEY"
 
```python
pip install pypaystack
from pypaystack import Transaction

transaction = Transaction("customer@domain.com", "CustomerAUTHcode")

####Charge this customer
status_code, status, message, data = transaction.charge(10000)

####Verify a transaction
status_code, status, message, data = transaction.verify(refcode)
```

