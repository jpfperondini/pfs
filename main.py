import csv, sqlite3

def importStatement():
    #Init the database
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    qry = open('schema.sql', 'r').read()
    c.execute(qry)
    conn.commit()

    #Loads the data
    data = []
    with open('extrato.csv', 'rb') as csvfile:
        rdr = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in rdr:
            c.execute('insert into transaciton values (?, ?, ?, ?)', [int(row[3]), row[0], row[2], row[4]])
    conn.commit()

    #Show data
    c.execute('select * from transaciton')
    print c.fetchone()

    #Close the DB
    c.close
    conn.close

importStatement()
