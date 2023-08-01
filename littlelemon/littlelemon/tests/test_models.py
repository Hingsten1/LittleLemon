from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item.title, "IceCream")
        
        
        
        

class MenuViewTest(TestCase):
    def test_setUp(self):
        item1 = Menu.objects.create(title="Dick", price=80, inventory=10)
        item2 = Menu.objects.create(title="Ass", price=69, inventory=1)
        
        
    #def test_getall(self):
        
        self.assertEqual(item1.title, "Dick")
        self.assertEqual(item2.title, "Ass")
        
        