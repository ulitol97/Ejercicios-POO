import unittest
import tree_set


class TestUM(unittest.TestCase):
    """Unit tests of advanced exercise 2, duck typing with a tree set"""

    def setUp(self):
        print("Executing test of advanced exercise 2: duck typing with a tree set")

    def test_person_set_up(self):
        """Init a person and check the attribute names have been stored correctly"""
        p1 = tree_set.Person('Edu', 'Ulibarri')
        p2 = tree_set.Person('Guillermo', 'Ulibarri', 23, '123456789X')
        # Default values
        self.assertEqual(p1.name, 'Edu')
        self.assertEqual(p1.surname, 'Ulibarri')
        self.assertIs(p1.age, 18)
        self.assertEqual(p1.dni, '1234567V')

        # Specific values
        self.assertEqual(p2.name, 'Guillermo')
        self.assertEqual(p2.surname, 'Ulibarri')
        self.assertIs(p2.age, 23)
        self.assertEqual(p2.dni, '123456789X')

    def test_comapare_surname_name(self):
        """Test the default comparison system by surname and name"""
        p1 = tree_set.Person('Edu', 'Ulibarri')
        p2 = tree_set.Person('Guillermo', 'Ulibarri')
        p3 = tree_set.Person('Alejandro', 'Alvarez')
        p4 = tree_set.Person('Zimon', 'Zabalza')
        p5 = tree_set.Person('Tintin', 'Milu')

        # 'Edu' comes before 'Guillermo' when the surnames are the same
        self.assertIs(p1.compare_to (p2), -1)
        # 'Guillermo' comes after 'Edu' when the surnames are the same
        self.assertIs(p2.compare_to (p1), 1)
        # 'Zabalza' comes after 'Alvarez'
        self.assertIs(p4.compare_to(p1), 1)
        # 'Zabalza' comes after 'Ulibarri'
        self.assertIs(p4.compare_to(p2), 1)
        # 'Alvarez' comes before 'Milu'
        self.assertIs(p3.compare_to(p5), -1)

    def test_tree_set_by_dni(self):
        """Test the default comparison system by surname and name"""
        tree_set_dni = tree_set.TreeSet(tree_set.ComparatorDNI())  # Tree set comparing by DNI
        p1 = tree_set.Person("Edu", "A", 70, "3456")
        p2 = tree_set.Person("Alex", "B", 28, "4567")
        p3 = tree_set.Person("Marcial", "C", 15, "7891")

        tree_set_dni.add(p1)
        tree_set_dni.add(p2)
        tree_set_dni.add(p3)

        # Check the order of the elements in the set
        # 'Edu' has the lowest DNI
        self.assertEqual(tree_set_dni.contents[0], p1)
        # 'Alex' has the next bigger DNI
        self.assertEqual(tree_set_dni.contents[1], p2)
        # 'Marcial' has the biggest DNI
        self.assertEqual(tree_set_dni.contents[2], p3)

    def test_tree_set_by_age(self):
        """Test the default comparison system by surname and name"""
        tree_set_age = tree_set.TreeSet(tree_set.ComparatorAge())  # Tree set comparing by Age
        p1 = tree_set.Person("Edu", "A", 70, "3456")
        p2 = tree_set.Person("Alex", "B", 28, "4567")
        p3 = tree_set.Person("Marcial", "C", 15, "7891")

        tree_set_age.add(p1)
        tree_set_age.add(p2)
        tree_set_age.add(p3)

        # Check the order of the elements in the set
        # 'Marcial' has the lowest age
        self.assertEqual(tree_set_age.contents[0], p3)
        # 'Alex' has the next bigger age
        self.assertEqual(tree_set_age.contents[1], p2)
        # 'Edu' has the biggest age
        self.assertEqual(tree_set_age.contents[2], p1)



if __name__ == "__main__":
    unittest.main()
