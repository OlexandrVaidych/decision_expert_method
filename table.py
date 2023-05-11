from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem
from data import data

class Table(QTableWidget):
    def __init__(self, rows, columns):
        super().__init__(rows, columns)

        self.initialize_table()

    def initialize_table(self):
        horizontal_header = ["Laptop1", "Laptop2"]
        
        for row in range(self.rowCount()):
            for col in range(self.columnCount()):
                item = QTableWidgetItem(data[row][col])
                self.setItem(row, col, item) 
        
        self.setHorizontalHeaderLabels(horizontal_header)
        self.setVerticalHeaderLabels(["Price", "Tech. Char."])