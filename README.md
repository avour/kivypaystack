# pypaystack

A python wrapper for Paystack API (WIP)


- Charge the customer
- Verify a transaction

##Installation

Register on the paystack website and get your Authorization key
Store your authorization key in your environment variable as "PAYSTACK_AUTHORIZATION_KEY"

 
```bash
pip install pypaystack
```

```python
from pypaystack import Transaction

transaction = Transaction("customer@domain.com", "CustomerAUTHcode")

###Charge this customer N100
status_code, status, message, data = transaction.charge(10000)

###Verify a transaction given a reference code "refcode"
status_code, status, message, data = transaction.verify(refcode)
```

More functionality to follow soon


