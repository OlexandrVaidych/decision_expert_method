class NumMark:
    def __init__(self, num_mark):
        self._num_mark = num_mark
    
    def get_num_mark(self):
        if self._num_mark == "unacc":
            res = 1
        elif self._num_mark == "acc":
            res = 2
        elif self._num_mark == "good":
            res = 3
        else:
            res = 4
        
        return res