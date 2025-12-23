class load_management: 
    def __init__(self, neighborhood):
        self.neighborhood = neighborhood
        self.location_area = []
        
    def total_load(self):
        return sum (self.neighborhood.values())
    
    def shed_load(self, limit= 500):
         for area, load in list(self.neighborhood.items()):
            if self.total_load() > limit:
                self.location_area.append(area)
                del self.neighborhood[area]
        
    def get_location_area(self):
        return self.location_area
                       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        