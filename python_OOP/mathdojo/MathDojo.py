class MathDojo(object):
	def __init__(self, val):
        	self.val = val

    	def add(self, *args):
		for num in args:
			if isinstance(num, list):
				self.val += sum(num)
			else:
				self.val += num
        	return self

    	def subtract(self, *args):
		for num in args:
			if isinstance(num, list):
				self.val -= sum(num)
			else:
				self.val -= num
        	return self
		
	def result(self):
		return self.val

md = MathDojo(0)
print md.add(2).add(2,5).subtract(3,2).result()

md = MathDojo(0)
print md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()