class Alternative:
    def __init__(self, laptops):
        self._laptops = laptops
    
    def calc_best_alternative(self):
        max_num_mark = max(self._laptops.values())

        for key, value in self._laptops.items():
            if value == max_num_mark:
                alternative = key
                break
        
        return f"The best alternative is {alternative}" 