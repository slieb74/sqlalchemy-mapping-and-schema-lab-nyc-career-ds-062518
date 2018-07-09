import unittest, sqlite3

connection = sqlite3.connect('./musicians.db')
cursor = connection.cursor()

class TestSchema(unittest.TestCase):
    table_info = cursor.execute("PRAGMA table_info('musicians')").fetchall()

    def test_table_name(self):
        self.assertEqual(cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchone()[0], 'musicians')

    def test_id_column(self):
        name = self.table_info[0][1]
        datatype = self.table_info[0][2]
        self.assertEqual(name, 'id')
        self.assertEqual(datatype, 'INTEGER')

    def test_fullname_column(self):
        name = self.table_info[1][1]
        datatype = self.table_info[1][2]
        self.assertEqual(name, 'fullname')
        self.assertEqual(datatype, 'VARCHAR')

    def test_instrument_column(self):
        name = self.table_info[2][1]
        datatype = self.table_info[2][2]
        self.assertEqual(name, 'instrument')
        self.assertEqual(datatype, 'VARCHAR')

    def test_dob_column(self):
        name = self.table_info[3][1]
        datatype = self.table_info[3][2]
        self.assertEqual(name, 'dob')
        self.assertEqual(datatype, 'DATETIME')

    def test_alive_column(self):
        name = self.table_info[4][1]
        datatype = self.table_info[4][2]
        self.assertEqual(name, 'alive')
        self.assertEqual(datatype, 'BOOLEAN')
