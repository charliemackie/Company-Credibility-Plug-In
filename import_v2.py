import csv, random

names = {
    "Electronics": [["APPLE","BELL","EB_GAMES","THE_SOURCE","BEST_BUY"], 50, 500],
    "Clothing": [["ALDO","FOSSIL","GUESS","FOREVER21","HUDSONS_BAY"], 10, 200],
    "Footwear": [["ROOTS","SKETCHERS","BROWNS","BOATHOUSE","SOFTMOC"], 10, 200],
    "Health": [["BATH_BODY_WORKS","KIEHLS","MARSHALLS","MAC","GNC"], 10, 500],
    "Jewellery": [["MICHAEL_HILL","PANDORA","SWAROVSKI","CHARM_DIAMOND","PEOPLES"], 50, 1000]
}


def getTransaction():
    sectors = list(names.keys())
    new_index = random.randint(0, len(sectors) - 1)
    sector = names[sectors[new_index]]
    new_name = random.randint(0, len(sector[0]) - 1)
    vendor = sector[0][new_name]
    amount = random.randint(sector[1], sector[2])

    transaction_type = TransactionType()# 1 is purchase, 0 is return
    return vendor, amount, transaction_type


def TransactionType():
    x = random.randint(0,10)
    if(x<=8):
        return "Purchase"
    else:
        return "Return"

def createStatement(num_transactions):
    statement = []
    for _ in range(num_transactions):
        statement.append(getTransaction())
    return statement
    

def createCSV(numofstatements,k):
    for a in range(numofstatements):
        with open("csvfilled"+str(a)+".csv", 'w', newline='') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',')
            filewriter.writerows(createStatement(k))
            csvfile.close()
        

createCSV(20,50)

