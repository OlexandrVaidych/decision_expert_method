from best_alternative import BestAlternative
from data import data
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from table import Table


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()

        table = Table(2, 2)

        best_alternative = BestAlternative(data)
        optimal_alternative = best_alternative.get_best_alternative()
        #print(optimal_alternative)

        layout.addWidget(table)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
