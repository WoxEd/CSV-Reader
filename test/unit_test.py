import unittest
import model.covid_model as model


class TestAdd(unittest.TestCase):
    """
    Test Cases for adding into the model
    """

    def setUp(self):
        """
        Setup
        """
        model.reset_db()

    def tearDown(self):
        """
        Teardown
        """
        model.reset_db()

    def test_add_empty(self):
        """
        Test Case for adding to empty list
        """
        self.assertEqual(0, model.get_size())
        model.add(1, 1, 1, 1, 1, 1)
        self.assertEqual(1, model.get_size())
        print("Unit Test: Add to empty list by Woxing Zhang")

    def test_add_not_empty(self):
        """
        Test Cases for adding into non empty list
        """
        self.assertEqual(0, model.get_size())
        model.add(0, 0, 0, 0, 0, 0)
        initial_size = model.get_size()
        self.assertNotEqual(0, initial_size)
        model.add(1, 1, 1, 1, 1, 1)
        self.assertEqual(initial_size + 1, model.get_size())
        print("Unit Test: Add to non empty list by Woxing Zhang")

    def test_delete_empty(self):
        """
        Test case confirming delete from empty list doesn't break things
        """
        self.assertEqual(0, model.get_size())
        delete_id = '1'
        model.delete(delete_id)
        self.assertEqual(0, model.get_size())
        print("Unit Test: Delete from empty database by Woxing Zhang")

    def test_delete_full(self):
        """
        Test case for deleting from a database with elements
        """
        self.assertEqual(0, model.get_size())
        model.add(1, 1, 1, 1, 1, 1)
        self.assertEqual(1, model.get_size())
        delete_id = '1'
        model.delete(delete_id)
        self.assertEqual(0, model.get_size())
        print("Unit Test: Delete from database with data by Woxing Zhang")

    def test_delete_full_non_existing(self):
        """
        Test case for deleting an element that doesn't exist from the database
        """
        self.assertEqual(0, model.get_size())
        model.add(1, 1, 1, 1, 1, 1)
        self.assertEqual(1, model.get_size())
        delete_id = '2'
        model.delete(delete_id)
        self.assertEqual(1, model.get_size())
        print("Unit Test: Delete non existing element from database with data by Woxing Zhang")


# runs the test cases
if __name__ == '__main__':
    unittest.main()
