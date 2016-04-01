import sqlite3, logging, os

def init(force_recreate = False):
    if force_recreate:
        os.remove('pfs.db')

    if not os.path.isfile('pfs.db'):
        conn = sqlite3.connect('pfs.db')
        c = conn.cursor()
        qry = open('schema.sql', 'r').read()
        c.execute(qry)
        conn.commit()
        c.close()
        conn.close()
        logging.info('Database created')
