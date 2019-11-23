# Pull data from database
# Compute score for each ID
# Update database

from DatabaseAPI import Database

database = Database("transactions.db")
transactions = database.get_data()

def compute_score(transactions):
    purchases = 0
    returns = 0
    return_counter = 0
    for purchase in transactions[0]:
        purchases += purchase
    
    for return_item in transactions[1]:
        returns += return_item
        return_counter += 0
    
    return_frc = (returns / purchases) * return_counter
    score = 1 - return_frc
    return score

ids = list(transactions.keys())
for company_id in ids:
    database.update_score(company_id, compute_score(transactions[company_id]))

    