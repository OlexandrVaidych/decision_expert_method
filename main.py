from attribute import Attribute
from data import data
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.table_widget = QTableWidget(self)
        self.setCentralWidget(self.table_widget)

        self.table_widget.setRowCount(2)
        self.table_widget.setColumnCount(2)

        self.table_widget.setHorizontalHeaderLabels(["Laptop1", "Laptop2",])
        self.table_widget.setVerticalHeaderLabels(["Price", "Tech. Char.",])

        self.add_data()

        attribute1 = Attribute(data, 0)
        attributes1 = attribute1.get_attributes()
        #print(attributes1)

        attribute2 = Attribute(data, 1)
        attributes2 = attribute2.get_attributes()
        #print(attributes2)
    
    def add_data(self):
        
        for row in range(self.table_widget.rowCount()):
            for col in range(self.table_widget.columnCount()):
                item = QTableWidgetItem(data[row][col])
                self.table_widget.setItem(row, col, item) 


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
