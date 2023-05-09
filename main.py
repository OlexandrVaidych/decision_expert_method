from data import data
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        QMainWindow.table_widget = QTableWidget(self)
        self.setCentralWidget(self.table_widget)

        self.table_widget.setRowCount(2)
        self.table_widget.setColumnCount(2)

        self.table_widget.setHorizontalHeaderLabels(["Laptop1", "Laptop2",])
        self.table_widget.setVerticalHeaderLabels(["Price", "Tech. Char.",])

        self.add_data()
    
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
