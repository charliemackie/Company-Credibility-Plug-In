import csv, sqlite3

class Database(object):
    def Database(self, database):
        self.database_name = database
        self.conn = sqlite3.connect(self.database_name)
        self.c = self.conn.cursor()

    def import_csv(self, csv_name):
        if not '.csv' in csv_name:
            raise FileNotFoundError

        with open(csv_name, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                new_entry = f"({row.join(', ')})"
                self.c.execute(f"INSERT INTO transactions VALUES {new_entry}")

    def update_score(self, company_name, new_score):
        self.c.execute(f'''UPDATE scores
                        SET Score = {new_score}
                        WHERE CompanyName = {company_name}''')

    def add_company(self, new_company, website, company_id, segment, score):
        values = f"({new_company}, {website}, {company_id}, {segment}, {score})"
        c.execute(f"INSERT INTO scores VALUES {values}")

    def get_score(self, company):
        pass

    def company_exists(self, company):
        pass

    def close(self):
        self.conn.close()
    
    

