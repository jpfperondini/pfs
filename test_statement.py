import unittest, statement, db, logging

class TestStatement(unittest.TestCase):

    def _test_check_value_for_invalid_input(self, value):
        conn = db.init_memory()
        self.assertRaises(ValueError, statement._check_value, value)
        conn.close

    def test_import_file(self):
        conn = db.init_memory()
        expected1 = (123456, "01/01/2016", "A", 12021)
        expected2 =  (654321, "02/01/2016","A", -5431)
        statement.importfile(conn, "tests/statement.csv")
        c = conn.cursor()
        c.execute("select * from financial_transaction")
        self.assertEqual(expected1,  c.fetchone())
        self.assertEqual(expected2,  c.fetchone())
        c.close
        conn.close

    def test_check_value(self):
        conn = db.init_memory()
        value = '123,12'
        self.assertEqual(value, statement._check_value(value))
        conn.close

    def test_check_value_for_scale_1(self):
        self._test_check_value_for_invalid_input('123,1')

    def test_check_value_for_scale_0(self):
        self._test_check_value_for_invalid_input('123,')

    def test_check_value_for_scale(self):
        self._test_check_value_for_invalid_input('123')

    def test_get(self):
        conn = db.init_memory()
        c = conn.cursor()
        db1 = (123456, "01/01/2016", "A", 12021)
        db2 = (654321, "02/01/2016","A", -5431)
        c.execute("insert into financial_transaction values (?, ?, ?, ?)", db1)
        c.execute("insert into financial_transaction values (?, ?, ?, ?)", db2)
        c.close()
        conn.commit()

        expected1 = (123456, "01/01/2016", "A", 120.21)
        expected2 =  (654321, "02/01/2016","A", -54.31)

        data = statement.get(conn)

        self.assertEqual(expected1,  data[0])
        self.assertEqual(expected2,  data[1])
        conn.close()

if __name__ == '__main__':
    unittest.main()
