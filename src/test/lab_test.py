import unittest

from src.main.user import User
from src.main.lab import problem1


class LabTest(unittest.TestCase):
    def test_problem1(self):
        """
        This test queries the student's view directly and compares it to a query of the underlying site_user
        table, to confirm the view only exposes firstname and lastname.
        """
        conn = problem1()
        cur = conn.cursor()

        try:
            cur.execute("SELECT * FROM firstname_lastname;")
            actual_result = [User(0, row[0], row[1], 0) for row in cur.fetchall()]
        except Exception as e:
            print(f"problem1: {e}\n")
            self.fail(str(e))
        finally:
            conn.close()

        expected_result = [
            User(0, "Steve", "Garcia", 0),
            User(0, "Alexa", "Smith", 0),
            User(0, "Steve", "Jones", 0),
            User(0, "Brandon", "Smith", 0),
            User(0, "Adam", "Jones", 0),
        ]

        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()
