import unittest
import abstract_factory


class TestUM(unittest.TestCase):
    """Unit tests of advanced exercise 5, abstract factory"""

    def setUp(self):
        print("Executing test of advanced exercise 5: abstract factory")

    def test_ui_set_up(self):
        """Init different UI components and check they are modified correctly"""
        # Windows UI
        win_button = abstract_factory.ui_components.WindowsButton()
        win_text = abstract_factory.ui_components.WindowsText()

        self.assertFalse(win_button.clicked)
        self.assertEqual(win_text.text, '')

        win_button.click()

        # Linux UI
        linux_button = abstract_factory.ui_components.LinuxButton()
        linux_text = abstract_factory.ui_components.LinuxText()

        self.assertFalse(linux_button.clicked)
        self.assertEqual(linux_text.text, '')

        linux_button.click()


if __name__ == "__main__":
    unittest.main()
