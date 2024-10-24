import unittest
from unittest.mock import patch
from io import StringIO
import main

class TestMain(unittest.TestCase):
    # Tests for get_user_input
    @patch('sys.stdout', new_callable=StringIO)  # Suppress print output
    def test_get_user_input_rock(self, mock_stdout):
        self.assertEqual(main.get_user_input("1"), 1)

    @patch('sys.stdout', new_callable=StringIO)  # Suppress print output
    def test_get_user_input_paper(self, mock_stdout):
        self.assertEqual(main.get_user_input("2"), 2)

    @patch('sys.stdout', new_callable=StringIO)  # Suppress print output
    def test_get_user_input_scissors(self, mock_stdout):
        self.assertEqual(main.get_user_input("3"), 3)

    @patch('sys.stdout', new_callable=StringIO)  # Suppress print output
    def test_get_user_input_quit(self, mock_stdout):
        with self.assertRaises(SystemExit):
            main.get_user_input("0")

    @patch('sys.stdout', new_callable=StringIO)  # Suppress print output
    def test_get_user_input_out_of_range(self, mock_stdout):
        self.assertEqual(main.get_user_input("4"), None)

    @patch('sys.stdout', new_callable=StringIO)  # Suppress print output
    def test_get_user_input_non_integer(self, mock_stdout):
        self.assertEqual(main.get_user_input("a"), None)

    # Tests for play_round
    @patch('sys.stdout', new_callable=StringIO)  # Suppress print output
    def test_play_round_tie(self, mock_stdout):
        self.assertEqual(main.play_round(1, 1), "It's a tie!\n")

    @patch('sys.stdout', new_callable=StringIO)  # Suppress print output
    def test_play_round_user_wins(self, mock_stdout):
        self.assertEqual(main.play_round(1, 3), "You win!\n")

    @patch('sys.stdout', new_callable=StringIO)  # Suppress print output
    def test_play_round_user_loses(self, mock_stdout):
        self.assertEqual(main.play_round(1, 2), "You lose!\n")

if __name__ == '__main__':
    unittest.main()
