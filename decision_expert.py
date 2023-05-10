class DecisionExpert:
    def __init__(self, attributes):
        self._attributes = attributes
    
    def determine_mark(self):
        res = "unacc"

        if self._attributes[0] == "high" and self._attributes[1] == "bad":
            res = "unacc"
        elif self._attributes[0] == "high" and self._attributes[1] == "acc":
            res = "unacc"
        elif self._attributes[0] == "high" and self._attributes[1] == "good":
            res = "unacc"
        elif self._attributes[0] == "high" and self._attributes[1] == "exc":
            res = "unacc"
        elif self._attributes[0] == "medium" and self._attributes[1] == "bad":
            res = "unacc"
        elif self._attributes[0] == "medium" and self._attributes[1] == "acc":
            res = "acc"
        elif self._attributes[0] == "medium" and self._attributes[1] == "good":
            res = "good"
        elif self._attributes[0] == "medium" and self._attributes[1] == "exc":
            res = "exc"
        elif self._attributes[0] == "low" and self._attributes[1] == "bad":
            res = "unacc"
        elif self._attributes[0] == "low" and self._attributes[1] == "acc":
            res = "good"
        elif self._attributes[0] == "low" and self._attributes[1] == "good":
            res = "exc"
        else:
            res = "exc"
        
        return res