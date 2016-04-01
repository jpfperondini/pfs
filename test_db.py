import unittest, importstatement, db, logging, os, sqlite3

class TestDB(unittest.TestCase):

  def test_init(self):
      path = 'db.test_init.db'
      db.init(True, path)
      conn = sqlite3.connect(path)
      c = conn.cursor()
      c.execute("select * from sqlite_master where name = 'financial_transaction' and type = 'table'")
      self.assertEquals("financial_transaction", c.fetchone()[1])
      c.close()
      conn.close()
      os.remove(path)


  def test_init_memory(self):
      conn = db.init_memory()
      c = conn.cursor()
      c.execute("select * from sqlite_master where name = 'financial_transaction' and type = 'table'")
      self.assertEquals("financial_transaction", c.fetchone()[1])
      c.close()
      conn.close()

if __name__ == '__main__':
    unittest.main()
