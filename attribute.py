class Attribute:
    def __init__(self, data, index):
         self._data = data
         self._index = index

    def get_attributes(self):
            attributes = []
            
            for i in range(self._index, len(self._data)):
                for j in range(len(self._data[0])):
                    attributes.append(self._data[j][i])
                break
                    
            return attributes