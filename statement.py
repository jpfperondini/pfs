import csv

def importfile(conn, path):
    c = conn.cursor()
    data = []
    with open(path, 'rb') as csvfile:
        rdr = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in rdr:
            value = _check_value(row[4]).replace(',', '')
            c.execute('insert into financial_transaction values (?, ?, ?, ?)', [int(row[3]), row[0], row[2], int(value)])
    conn.commit()
    c.close()

def _check_value(value):
    comma_idx = value.find(',')
    if comma_idx == -1:
        raise ValueError("Invalid input " + value)

    if len(value) - comma_idx < 3:
        raise ValueError("Invalid input " + value)
    return value;

def get(conn):
    c = conn.cursor()
    c.execute("select doc, date, desc, value from financial_transaction")
    data = []
    for item in c.fetchall():
        data.append((item[0], item[1], item[2], float(item[3]) / 100.0))
    c.close()
    return data
