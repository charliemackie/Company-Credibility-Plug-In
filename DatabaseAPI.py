import csv, sqlite3

class Database(object):
    def __init__(self, database):
        self.database_name = database
        self.conn = sqlite3.connect(self.database_name)
        self.c = self.conn.cursor()

    def create_table(self, table_name, headers):
        header_list = ", "
        header_list = header_list.join(headers)
        print(header_list)
        self.c.execute(f'''CREATE TABLE {table_name}
                        ({header_list})''')

    def import_csv(self, csv_name):
        if not '.csv' in csv_name:
            raise FileNotFoundError

        with open(csv_name, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                new_entry = ""
                count = 1
                row_list = row[0].split(",")
                for item in row_list:
                    print (item)
                    new_entry += "\'" + item + "\'" + ("," if count < len(row_list) else "")
                    count += 1
                print(new_entry)
                self.c.execute(f"INSERT INTO transactions VALUES ({new_entry})")
                self.conn.commit()

    def update_score(self, company_id, new_score):
        self.c.execute(f'''UPDATE scores
                        SET Score = \'{new_score}\'
                        WHERE ID = \'{company_id}\'''')
        self.conn.commit()

    def add_company(self, new_company, website, company_id, score):
        values = f"(\'{new_company}\',\'{website}\',\'{company_id}\',\'{score}\')"
        print(values)
        self.c.execute(f"INSERT INTO scores VALUES {values}")
        self.conn.commit()

    def get_company_data(self, company_id):
        self.c.execute(f"SELECT * FROM scores WHERE ID = \'{company_id}\'")
        return self.c.fetchall()

    def company_exists(self, company_id):
        string = f"SELECT * FROM scores WHERE ID = \'{company_id}\'"
        print(string)
        name = self.c.execute(string).fetchone()
        return len(name) != 0

    def get_data(self):
        data = {}
        self.c.execute("SELECT DISTINCT ID FROM transactions")
        unique_ids = self.c.fetchall()
        for company_id in unique_ids:
            returns = self.c.execute(f'SELECT * FROM transactions WHERE ID = \'{company_id[0]}\' AND Type = \'Return\'').fetchall()
            
            purchases = self.c.execute(f'SELECT * FROM transactions WHERE ID = \'{company_id[0]}\' AND Type = \'Purchase\'').fetchall()
            data[company_id[0]] = (purchases, returns)
        
        return data

    def close(self):
        self.conn.close()

