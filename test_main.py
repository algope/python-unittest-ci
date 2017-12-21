import os
import db as simple_db
import sqlite3
import unittest


class TestCensusDatabase(unittest.TestCase):
    """
    Test the census database
    """

    def setUp(self):
        """
        Setup a temporary database
        """
        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()

        # create a table
        cursor.execute("""CREATE TABLE census
                          (id TEXT, name TEXT, surname TEXT,
                           has_voted BOOLEAN)
                       """)

        # insert multiple voters
        voters = [('44444444Y', 'Alejandro', 'González', False),
                  ('43333333K', 'Carmen', 'Pérez', False),
                  ('05888888G', 'Antonio', 'González', False)]

        cursor.executemany("INSERT INTO census VALUES (?,?,?,?)", voters)
        conn.commit()

    def tearDown(self):
        """
        Delete the database
        """
        os.remove("mydatabase.db")

    def test_updating_voter(self):
        """
        Tests that we can successfully update an artist's name
        """
        simple_db.update_voter('43333333K', True)
        actual = simple_db.select_voter('43333333K')
        expected = ('43333333K', 'Carmen', 'Pérez', True)
        self.assertTupleEqual(expected, actual)


    def test_deleting_voters(self):
        """
        Tests that we can delete a voter that exists
        """

        simple_db.delete_voter('44444444Y')
        deleted = simple_db.select_voter('44444444Y')
        self.assertFalse(deleted)

    def test_artist_does_not_exist(self):
        """
        Test that an artist does not exist
        """
        simple_db.delete_voter('44444444Y')
        result = simple_db.select_voter('44444444Y')
        print(result)
        self.assertFalse(result)
