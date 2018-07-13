#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#Product Inventory Project - Create an application which manages
#an inventory of products. Create a product class which has a
#price, id, and quantity on hand. Then create an inventory class
#which keeps track of various products and can sum up the inventory
#value.

class Product:
	def __init__(self, name, price, id, quantity):
		"""
        Class constructor that needs a price, a name, a product id,
        and quantity.
        """
		self.name = name
		self.price = price
		self.id = id
		self.quantity = quantity

	def update_qty(self, quantity, method='add'):
		if method == 'add':
			self.quantity += quantity
		elif method == 'subtract':
			self.quantity = max(0, self.quantity - quantity)


class Inventory:
	def __init__(self):
		"""
        Initializes the class instance.
        """
		self.list_of_products = []
	def add_product(self, product):
		"""
        Add new products to the inventory list.
        """
		self.list_of_products.append(product)
	def print_inventory(self, inventory_list):
		"""
        Print the inventory list.
        """
		for product in self.list_of_products:
			print '%s\t%d\t%f each' %(product.name, product.quantity,product.price)

	def count_total_value(self, inventory_list):
		"""
        Count the total value of products.
        """
		value = 0
		for product in self.list_of_products:
			value += product.quantity*product.price
		print 'total value of all products in list  - ' + str(value)


if __name__ == '__main__':
	 prod1 = Product("colgate",2.20,5,1)
	 prod2 = Product("brush",5,6,3)
	 prod3 = Product("soap",10,7,1)
	 prod4 = Product("towel",20,8,4)

	 inventory_list_1 = Inventory()
	 inventory_list_1.add_product(prod1)
	 inventory_list_1.add_product(prod2)
	 prod2.update_qty(10, 'add')
	 prod4.update_qty(1, 'subtract')
	 inventory_list_1.add_product(prod3)
	 inventory_list_1.add_product(prod4)
	 inventory_list_1.print_inventory(inventory_list_1)
	 inventory_list_1.count_total_value(inventory_list_1)



