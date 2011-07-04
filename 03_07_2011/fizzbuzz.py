class fizzbuzz: 
    x = None 
   
    def __init__(self, x):
	self.x = x

    def fizzbuzz(self):
	    if self.x % 3 == 0 and self.x % 5 == 0:
		    return "fizzbuzz"
	    elif self.x % 3 == 0:
		    return "fizz"
  	    elif self.x % 5 == 0: 
		    return "buzz"
	    return self.x
