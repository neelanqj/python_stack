class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        self.logged = True
        print "Bikes price is " + str(self.price) + ", the bikes max_speed is " + str(self.max_speed) + ", and the bikes miles is " + str(self.miles)
        return self
    def ride(self):
        self.miles = self.miles + 10
        print "Riding"
        return self
    def reverse(self):
        self.miles = self.miles - 5
        print "Reversing"
        return self
		

bike1 = Bike(200, "25mph");
bike2 = Bike(200, "25mph");
bike3 = Bike(200, "25mph");

bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()