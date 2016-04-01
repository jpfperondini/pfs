import csv, sqlite3

def execute():
    #Init the database
    conn = sqlite3.connect("pfs.db")
    c = conn.cursor()
    qry = open('schema.sql', 'r').read()
    c.execute(qry)
    conn.commit()

    #Loads the data
    data = []
    with open('extrato.csv', 'rb') as csvfile:
        rdr = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in rdr:
            c.execute('insert into financial_transaction values (?, ?, ?, ?)', [int(row[3]), row[0], row[2], row[4]])
    conn.commit()

    #Show data
    c.execute('select * from financial_transaction')
    print c.fetchone()

    #Close the DB
    c.close
    conn.close
