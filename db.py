import sqlite3, logging, os

def init(force_recreate = False, filepath = 'pfs.db'):
    file_exists = os.path.isfile(filepath)

    if force_recreate and file_exists:
        os.remove(filepath)

    if not file_exists:
        conn = sqlite3.connect(filepath)
        c = conn.cursor()
        qry = open('schema.sql', 'r').read()
        c.execute(qry)
        conn.commit()
        c.close()
        conn.close()
        logging.info('Database created')

def init_memory():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    qry = open('schema.sql', 'r').read()
    c.execute(qry)
    conn.commit()
    c.close()
    logging.info('Database created')
    return conn;
