from alternative import Alternative
from attribute import Attribute
from decision_expert import DecisionExpert
from num_mark import NumMark


class BestAlternative:
    def __init__(self, data):
        self._data = data
    
        attribute1 = Attribute(self._data, 0)
        attributes1 = attribute1.get_attributes()

        attribute2 = Attribute(self._data, 1)
        attributes2 = attribute2.get_attributes()

        mark1 = DecisionExpert(attributes1)
        laptop1_mark = mark1.determine_mark()

        mark2 = DecisionExpert(attributes2)
        laptop2_mark = mark2.determine_mark()

        num1 = NumMark(laptop1_mark)
        self.num_mark1 = num1.get_num_mark()

        num2 = NumMark(laptop2_mark)
        self.num_mark2 = num2.get_num_mark()


    def get_best_alternative(self):
        laptops = {"Laptop1": self.num_mark1, "Laptop2": self.num_mark2}

        alternative = Alternative(laptops)
        best_alternative = alternative.calc_best_alternative()
        
        return best_alternative