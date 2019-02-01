class Product(object):
	def __init__(self, price, name, weight, brand):
        	self.price = price
        	self.name = name
		self.weight = weight
		self.brand = brand
		self.status = "for sale"

    	def sell(self):
        	self.status = "sold"
        	return self

    	def add_tax(self, tax):
        	return self.price * tax

	def return_prod(self, reason):
		if reason == "defective":
			self.status = "defective"
			self.price = 0
		elif reason =="in box":
			self.status = "for sale"
		elif reason == "openned":
			self.status = "used"
			self.price = self.price * 0.8
		return self
		
	def display_info(self):
		print "Price " + str(self.price)
		print "Item " + str(self.name)
		print "Weight " + str(self.weight)
		print "Brand " + str(self.brand)
		print "Status " + str(self.status)
		
		return self

prod = Product(10, "Stuff", 1, "Toyota")
prod.display_info()