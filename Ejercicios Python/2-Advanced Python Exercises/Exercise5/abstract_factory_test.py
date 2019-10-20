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
        win_text.set_text('windows text')

        self.assertTrue(win_button.clicked)
        self.assertEqual(win_text.text, 'windows text')

        # Linux UI
        linux_button = abstract_factory.ui_components.LinuxButton()
        linux_text = abstract_factory.ui_components.LinuxText()

        self.assertFalse(linux_button.clicked)
        self.assertEqual(linux_text.text, '')

        linux_button.click()
        linux_text.set_text('linux text')

        self.assertTrue(linux_button.clicked)
        self.assertEqual(linux_text.text, 'linux text')

    def test_factory(self):
        """Init different factories and check they initiate objects correctly"""
        # Windows factory
        win_factory = abstract_factory.AbstractFactory.get_factory('Windows')

        win_button = win_factory.create_button()
        win_text = win_factory.create_text()

        self.assertTrue(isinstance(win_button, abstract_factory.ui_components.WindowsButton))
        self.assertTrue(isinstance(win_text, abstract_factory.ui_components.WindowsText))

        # Linux factory
        linux_factory = abstract_factory.AbstractFactory.get_factory('Linux')

        linux_button = linux_factory.create_button()
        linux_text = linux_factory.create_text()

        self.assertTrue(isinstance(linux_button, abstract_factory.ui_components.LinuxButton))
        self.assertTrue(isinstance(linux_text, abstract_factory.ui_components.LinuxText))


if __name__ == "__main__":
    unittest.main()
