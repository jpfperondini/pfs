import csv, sqlite3

def execute(conn, filename):
    c = conn.cursor()
    data = []
    with open(filename, 'rb') as csvfile:
        rdr = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in rdr:
            c.execute('insert into financial_transaction values (?, ?, ?, ?)', [int(row[3]), row[0], row[2], row[4]])
    conn.commit()
    c.close()
