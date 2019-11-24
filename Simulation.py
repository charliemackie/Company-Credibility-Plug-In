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

websites = open('websites.csv', 'r')
lines = websites.readlines()
for company_id in ids:
    for line in lines:
        line = line.split(',')
        if company_id == line[0]:
            if not database.company_exists(company_id):
                database.add_company(line[1], line[2].strip(), company_id, round(compute_score(transactions, company_id) * 100, 1))
            else:
                print('here')
                database.update_score(company_id, round(compute_score(transactions, company_id) * 100, 1))
