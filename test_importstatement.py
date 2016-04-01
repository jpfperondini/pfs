import unittest, importstatement, db, logging

class TestStringMethods(unittest.TestCase):

  def test_execute(self):
      conn = db.init_memory()
      expected1 = (123456, "01/01/2016", "A", u'120,21')
      expected2 =  (654321, "02/01/2016","A","-54,31")
      importstatement.execute(conn, "tests/statement.csv")
      c = conn.cursor()
      c.execute("select * from financial_transaction")
      self.assertEqual(expected1,  c.fetchone())
      self.assertEqual(expected2,  c.fetchone())
      c.close
      conn.close

if __name__ == '__main__':
    unittest.main()
