from PySide6.QtWidgets import QApplication, QMainWindow
from main_ui import Ui_MainWindow
from openpyxl import load_workbook

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load_data()
        self.load_LMP_adress()
        self.load_transfer()
    
    def load_data(self):
        wb = load_workbook("data/template.xltx")
        ws = wb["titledTN"]
        self.ui.shipperLine.setPlainText(str(ws["B12"].value))
        self.ui.driverLine.setPlainText(str(ws["AD41"].value))
        self.ui.driverName.setText(str(ws["AC65"].value))
        self.ui.mppName.setText(str(ws["C65"].value))
        self.ui.vehicleName.setText(str(ws["B44"].value))
        self.ui.vehicleNumber.setText(str(ws["AD44"].value))
        self.ui.LmpChoise.setCurrentText(str(ws["B55"].value))
        self.ui.LmpChoise_2.setCurrentText(str(ws["B41"].value))
    def load_LMP_adress(self):
        wb = load_workbook("data/template.xltx")
        ws = wb["Данные"]

        self.ui.LmpChoise.clear()
        row = 2
        while True:
            value = ws[f"A{row}"].value
            if value is None:
                break
            self.ui.LmpChoise.addItem(str(value))
            row+=1
    
    def load_transfer(self):
        wb = load_workbook("data/template.xltx")
        ws = wb["Данные"]

        self.ui.LmpChoise_2.clear()
        row = 3
        while True:
            value = ws[f"C{row}"].value
            if value is None:
                break
            self.ui.LmpChoise_2.addItem(str(value))
            row+=1



app = QApplication([])
window = MainWindow()
window.show()
app.exec()
