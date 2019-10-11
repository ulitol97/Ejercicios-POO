import unittest
import ticket_supermarket


class TestSupermarket(unittest.TestCase):
    """Parte del ejercicio 4 donde comprobamos el funcionamiento de una clase ticket"""

    def test_import(self):
        """Comprobar que el módulo con los tickets se llama ticket_supermarket"""
        self.assertTrue('ticket_supermarket' in globals().keys())

    def test_classes_exist(self):
        """Comprobar que el módulo de tickets tiene una clase Ticket y una clase Producto"""
        self.assertTrue(hasattr(ticket_supermarket, 'Ticket'))
        self.assertTrue(hasattr(ticket_supermarket, 'Product'))

    def test_documentation (self):
        """Comprobar que la clase ticket y product están mínimamente documentadas"""
        self.assertFalse(ticket_supermarket.Ticket.__doc__ is None)
        self.assertTrue(len(ticket_supermarket.Ticket.__doc__) > 20)

        self.assertFalse(ticket_supermarket.Product.__doc__ is None)
        self.assertTrue(len(ticket_supermarket.Product.__doc__) > 20)


    def test_init_ticket (self):
        """Comprobar que un ticket inicializado sin datos consta de una fecha de emisión y una lista vacía de productos"""
        ticket = ticket_supermarket.Ticket()
        self.assertTrue(hasattr(ticket, "date"))
        self.assertTrue(hasattr(ticket, "products"))
        self.assertIs(len (ticket.products), 0)

    def test_init_product (self):
        """Comprobar que un producto se inicializa con un precio y cantidad.
        Al ser inicializado sin datos cuenta con un precio de 1.00 y una cantidad de 1"""
        product = ticket_supermarket.Product()
        self.assertTrue(hasattr(product, "price"))
        self.assertTrue(hasattr(product, "amount"))
        self.assertIs(product.price, 1)
        self.assertIs(product.amount, 1)

    def test_init_ticket_2 (self):
        """Comprobar que un ticket inicializado con una lista los almacena en una lista de productos"""
        product1 = ticket_supermarket.Product(2, 2)
        product2 = ticket_supermarket.Product(5, 1)
        ticket = ticket_supermarket.Ticket([product1, product2])

        self.assertTrue(hasattr(ticket, "products"))
        self.assertIs(len(ticket.products), 2)
        self.assertIs(ticket.products[0].amount, 2)
        self.assertIs(ticket.products[1].price, 5)

    def test_compute_price_exists (self):
        """Comprobar que un ticket tiene un método llamado compute_price que calculará el total de los productos"""
        ticket = ticket_supermarket.Ticket()
        self.assertTrue('compute_price' in dir(ticket))
        self.assertTrue(hasattr(ticket.compute_price, '__call__'))

    def test_compute_price (self):
        """Comprobar que un ticket puede calcular su subtotal con el método compute_price"""
        product1 = ticket_supermarket.Product(2, 2)
        product2 = ticket_supermarket.Product(5, 1)
        ticket = ticket_supermarket.Ticket([product1, product2])
        self.assertIs(ticket.compute_price(), 9)
        ticket = ticket_supermarket.Ticket()
        self.assertIs(ticket.compute_price(), 0)


unittest.main()
