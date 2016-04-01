import csv, sqlite3

def execute(filename):
    #Init the database
    conn = sqlite3.connect("pfs.db")
    c = conn.cursor()

    #Loads the data
    data = []
    with open(filename, 'rb') as csvfile:
        rdr = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in rdr:
            c.execute('insert into financial_transaction values (?, ?, ?, ?)', [int(row[3]), row[0], row[2], row[4]])
    conn.commit()

    #Close the DB
    c.close
    conn.close
