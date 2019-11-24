# Pull data from database
# Compute score for each ID
# Update database

from DatabaseAPI import Database

database = Database("transactions.db")
transactions = database.get_data()

def compute_score(transactions, company_id):
    
    purchases = 0
    returns = 0
    return_counter = 0
    for purchase in transactions[company_id][0]:
        purchases += int(purchase[1])
    
    for return_item in transactions[company_id][1]:
        returns += int(return_item[1])
        return_counter += 1
    
    return_frc = (returns / purchases)
    score = 1 - return_frc
    return score

ids = list(transactions.keys())
for company_id in ids:
    print(company_id, compute_score(transactions, company_id))
    