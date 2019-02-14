# kivypaystack

A port of pypaystack to support the kivy framework 

It uses the builtin UrlRequest class to make asynchronous requests on the web and get the result when the
request is completed, so no external module is needed

- Charge the customer
- Verify a transaction
- Create Plans
- Get a single or all transactions
- Get a single or all customers


##Installation
pip it away

 ```python
pip install -U kivypaystack
```

Register on the paystack website and get your Authorization key.  
you can store your authorization key in your environment variable as "PAYSTACK_AUTHORIZATION_KEY" or pass it into the  
any kivypaystack objects at initiatialization.

##Examples

```python
from kivypaystack import Transaction, Customer, Plan

"""
All objects at initialization, recieves an optional callback func
"""

def transaction_callback(action, result_type, request, result):
    ''' action: reponse action performed EG: transaction.charge("customer@domain.com", "CustomerAUTHcode", 10000)
                on callback action will be 'charge' 

        result_type:  can be 'success', 'failure', 'redirect', 'error'

        request: instance of kivy.urlrequest.UrlRequest

        result: a decode json dictionary
    '''
    if action == 'charge':  # if a charge transaction was passed
        print(result_type, result)

    if action == 'verify':
        print(result_type, result)


#Instantiate the transaction object to handle transactions.  
#Pass in your authorization key - if not set as environment variable PAYSTACK_AUTHORIZATION_KEY
# warning use public key not your secret key
transaction = Transaction(authorization_key="pk_myauthorizationkeyfromthepaystackguys", callback=transaction_callback)
response = transaction.charge("customer@domain.com", "CustomerAUTHcode", 10000) #Charge a customer N100.
response  = transaction.verify(refcode) #Verify a transaction given a reference code "refcode".


#Instantiate the customer class to manage customers

customer = Customer(authorization_key="pk_myauthorizationkeyfromthepaystackguys")
response = customer.create("customer2@gmail.com", "John", "Doe", phone="080123456789") #Add new customer
response = customer.getone(1234) #Get customer with id of 1234
response = customer.getall() #Get all customers


#Instantiate the plan class to manage plans

plan = Plan(authorization_key="pk_myauthorizationkeyfromthepaystackguys")
response = plan.create("Test Plan", 150000, 'Weekly') #Add new plan
response = plan.getone(240) #Get plan with id of 240
response = plan.getall() #Get all plans

```
#Todo
Write more tests

