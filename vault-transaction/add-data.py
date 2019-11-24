import firebase_admin
import names
import namegenerator
import random
from firebase_admin import firestore
from firebase_admin import credentials

# Using an OAuth 2.0 refresh token (service account)
cred = credentials.Certificate("/Users/jinhwanlew/Documents/vault-transaction/vault-transaction-firebase-adminsdk-vc6l7-161e5e8c3e.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Get transactions
def user_name():
  return (names.get_full_name())

def transaction_amount():
  return (random.randint(1, 10000))

def isReversed():
  return (bool(random.getrandbits(1)))

def company_name():
  return (namegenerator.gen())

# Adding data to Firebase
count = 0
while (count < 5000):
  name = user_name()
  amount = transaction_amount()
  reverse = isReversed()
  
  # Making company redundant
  repeat_company = random.randint(1, 10)
  if repeat_company == 1:
    company = 'SSENSE'
  else:
    company = company_name()

  doc_ref = db.collection(u'transactions').document(u'User name: ' + name)
  doc_ref.set({
      u'Company': company,
      u'Amount': amount,
      u'Reverse': reverse
  })

  count = count + 1