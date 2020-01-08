from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget
from PyQt5 import uic
from main_ui import Ui_MainWindow
from add_edit_ui import Ui_Form
import sqlite3
import sys


class CoffeeShow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connection = sqlite3.connect("data/coffee.sqlite")

        self.load_button.clicked.connect(self.load)
        self.create_button.clicked.connect(self.create_or_edit)

        self.coffee_table_widget.setColumnCount(7)
        self.coffee_table_widget.setHorizontalHeaderLabels(
            ["id", "variety", "degree_of_roasting",
             "ground", "taste_description", "price", "volume"]
        )
        self.coffee_table_widget.resizeColumnsToContents()

    def load(self):
        cur = self.connection.cursor()
        data = cur.execute("""SELECT * FROM coffee""").fetchall()
        self.coffee_table_widget.setRowCount(0)
        for i, part in enumerate(data):
            self.coffee_table_widget.setRowCount(self.coffee_table_widget.rowCount() + 1)
            for j, item in enumerate(part):
                self.coffee_table_widget.setItem(i, j, QTableWidgetItem(str(item)))
        self.coffee_table_widget.resizeColumnsToContents()

    def create_or_edit(self):
        if self.coffee_table_widget.selectedIndexes() == []:
            self.add_edit_coffee = AddEditCoffee(self, None)
            self.add_edit_coffee.show()
        else:
            row = self.coffee_table_widget.selectedIndexes()[0].row()
            self.add_edit_coffee = AddEditCoffee(self, row)
            self.add_edit_coffee.show()


class AddEditCoffee(QWidget, Ui_Form):
    def __init__(self, main_form, row):
        super().__init__()
        self.main_form = main_form
        self.row = row
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_click)

    def on_click(self):
        variety = self.variety_lineedit.text()
        degree_of_roasting = self.degree_of_roasting_spinbox.value()
        ground = int(self.ground_checkbox.isChecked())
        taste_description = self.taste_sescription_lineedit.text()
        price = self.price_spinbox.value()
        volume = self.volum_spinbox.value()
        cursor = self.main_form.connection.cursor()
        if self.row is not None:
            cursor.execute(f"""DELETE FROM coffee WHERE id=={self.row + 1}""")
        cursor.execute(f"""
            INSERT INTO coffee 
            (variety, degree_of_roasting, ground, 
            taste_description, price, volume) 
            VALUES ("{variety}", {degree_of_roasting}, {ground},
            "{taste_description}", {price}, {volume})"""
                        )
        self.main_form.connection.commit()
        self.main_form.load()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    coffee_show = CoffeeShow()
    coffee_show.show()
    sys.exit(app.exec())
