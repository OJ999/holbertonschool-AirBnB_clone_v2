#!/usr/bin/python3
import unittest
import MySQLdb

# Import your modules and classes here

class TestMySQLStorage(unittest.TestCase):
    def setUp(self):
        # Set up MySQL connection and create a specific database for testing
        self.db = MySQLdb.connect(host="localhost", user="hbnb_test", passwd="hbnb_test_pwd", db="hbnb_test_db")
        self.cursor = self.db.cursor()

        # Additional setup steps if necessary

    def tearDown(self):
        # Clean up resources after each test
        self.cursor.close()
        self.db.close()

        # Additional teardown steps if necessary

    def test_create_state(self):
        # Get the initial number of records in the states table
        initial_count = self.get_state_count()

        # Execute the console command to create a state
        # This may involve interacting with your module or class
        # e.g., create_state("California")

        # Get the number of records in the states table after the action
        final_count = self.get_state_count()

        # Validate the action changed the state of the database
        self.assertEqual(final_count, initial_count + 1)

    def get_state_count(self):
        # Query the database to get the number of records in the states table
        self.cursor.execute("SELECT COUNT(*) FROM states")
        count = self.cursor.fetchone()[0]
        return count

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
