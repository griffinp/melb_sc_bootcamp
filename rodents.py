# defining a new class of object, called 'Rodent'
class Rodent:
    def __init__(self, tag_id): #this is a 'constructor'
        self.tag_id = tag_id #a variable starting with 'self.' will be stored as part of the object
        self.weights = []
    
    def plot(self):
        return self.tag_id[0]
    
    def add_weight(self, weight):
        self.weights.append(weight)
    


