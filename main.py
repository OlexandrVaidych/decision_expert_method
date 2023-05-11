from alternative import Alternative
from attribute import Attribute
from data import data
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout,QLabel, QWidget
from decision_expert import DecisionExpert
from num_mark import NumMark
from table import Table


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()

        table = Table(2, 2)

        """
        attribute1 = Attribute(data, 0)
        attributes1 = attribute1.get_attributes()
        #print(attributes1)

        attribute2 = Attribute(data, 1)
        attributes2 = attribute2.get_attributes()
        #print(attributes2)

        mark1 = DecisionExpert(attributes1)
        laptop1_mark = mark1.determine_mark()
        #print(laptop1_mark)

        mark2 = DecisionExpert(attributes2)
        laptop2_mark = mark2.determine_mark()
        #print(laptop2_mark)

        num1 = NumMark(laptop1_mark)
        num_mark1 = num1.get_num_mark()
        #print(num_mark1)

        num2 = NumMark(laptop2_mark)
        num_mark2 = num2.get_num_mark()
        #print(num_mark2)

        laptops = {horizontal_header[0]: num_mark1, horizontal_header[1]: num_mark2}
        
        alternative = Alternative(laptops)
        best_alternative = alternative.get_best_alternative()
        #print(best_alternative)
        """

        layout.addWidget(table)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
