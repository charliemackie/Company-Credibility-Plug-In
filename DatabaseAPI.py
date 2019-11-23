import csv, sqlite3

class Database(object):
    def Database(self, database):
        self.database_name = database
        self.conn = sqlite3.connect(self.database_name)
        self.c = self.conn.cursor()

    def create_table(self, table_name, headers):
        header_list = headers.join(", ")
        self.c.execute(f'''CREATE TABLE {table_name}
                        ({header_list})''')

    def import_csv(self, csv_name):
        if not '.csv' in csv_name:
            raise FileNotFoundError

        with open(csv_name, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                new_entry = f"({row.join(', ')})"
                self.c.execute(f"INSERT INTO transactions VALUES {new_entry}")

    def update_score(self, company_id, new_score):
        self.c.execute(f'''UPDATE scores
                        SET Score = {new_score}
                        WHERE ID = {company_id}''')

    def add_company(self, new_company, website, company_id, segment, score):
        values = f"({new_company}, {website}, {company_id}, {segment}, {score})"
        self.c.execute(f"INSERT INTO scores VALUES {values}")

    def get_company_data(self, company_id):
        self.c.execute(f"SELECT * FROM scores WHERE ID = {company_id}")
        return self.c.fetchall()

    def company_exists(self, company):
        pass

    def get_data(self):
        data = {}
        self.c.execute("SELECT DISTINCT ID FROM transactions")
        unique_ids = self.c.fetchall()
        for company_id in unique_ids:
            returns = self.c.execute(f'''SELECT *
                                    FROM transactions
                                    WHERE ID = {company_id} AND Type = return''').fetchall()
            
            purchases = self.c.execute(f'''SELECT *
                                    FROM transactions
                                    WHERE ID = {company_id} AND Type = purchase''').fetchall()
            data[company_id] = (purchases, returns)
        
        return data
            

        


    def close(self):
        self.conn.close()
    

    
    

