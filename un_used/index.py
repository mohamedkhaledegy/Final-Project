#### Import Packages
import sys
import numpy as np

#### GUI Desktop library Pyside2/Pyqt5 
from PySide2 import QtUiTools
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2 import QtWidgets as qtw
from PySide2.QtUiTools import loadUiType

## import Py version of Ui design
#from main_window import Ui_MainWindow

#### Matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

ui_main,_ = loadUiType('main_window2.ui')
ui_main5,_ = loadUiType('main_window5.ui')

ui_login,_ot = loadUiType('second_window.ui')

class MiApp(QMainWindow,ui_main5):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.grafica = Canvas_grafica()
        self.grafica1 = Canvas_grafica2()
        self.grafica2 = Canvas_grafica3()
        self.grafica3 = Canvas_grafica4()

        #self.ui.grafica_uno = self.findChild(qtw.QVBoxLayout,"grafica_uno")

        #self.grafica_uno = self.findChild(qtw.QVBoxLayout,"self.ui.grafica_uno")
        self.grafica_uno.addWidget(self.grafica)
        self.grafica_dos.addWidget(self.grafica1)
        self.grafica_tres.addWidget(self.grafica2)
        self.grafica_cuatro.addWidget(self.grafica3)

    def log_in_system(self):
        self.window2 = Main()
        self.close()
        self.window2.show()

class Main(QMainWindow,ui_main):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)


class Canvas_grafica(FigureCanvas):
    def __init__(self, parent=None):
        self.fig , self.ax = plt.subplots(1, dpi=100, figsize=(5, 5),
            sharey=True, facecolor='white')
        super().__init__(self.fig)
        nombres = ['15', '25', '30', '35','40']
        colores = ['red','red','red','red', 'red']
        tamaño = [10, 15, 20, 25, 30]

        self.ax.bar(nombres, tamaño, color = colores)
        self.fig.suptitle('Grafica de Barras',size=9)

class Canvas_grafica2(FigureCanvas):
    def __init__(self, parent=None):
        self.fig , self.ax = plt.subplots(1,dpi=100, figsize=(5, 5),
            sharey=True, facecolor='white')
        super().__init__(self.fig)

        nombres = ['Fresa', 'Piña', 'Lima', 'Uva']
        colores = ['blue','yellow','aqua','fuchsia']
        tamaño = [20, 26, 30, 24]
        explotar = [0.05, 0.05, 0.05, 0.05]

        plt.title("Cantidad de Frutas Disponibles",
            color='black',size=9, family="Arial")

        self.ax.pie(tamaño, explode = explotar, labels = nombres, 
            colors = colores,
                autopct = '%1.0f%%', pctdistance = 0.6,
                shadow=True, startangle=90, radius = 0.8, 
                labeldistance=1.1)  
        self.ax.axis('equal')


class Canvas_grafica3(FigureCanvas):
    def __init__(self, parent=None):     
        self.fig , self.ax = plt.subplots(1, dpi=100, figsize=(5, 5), 
            sharey=True, facecolor='white')
        super().__init__(self.fig) 

        self.fig.suptitle('Grafica de Datos',size=9)
        np.random.seed(20)
        y = np.random.randn(150).cumsum()

        self.ax = plt.axes()
        plt.plot(y, color='magenta')


class Canvas_grafica4(FigureCanvas):
    def __init__(self, parent=None):     
        self.fig , self.ax = plt.subplots(1, dpi=100, figsize=(5, 5), 
            sharey=True, facecolor='white')
        super().__init__(self.fig) 

        x = [1, 2, 3, 4, 5,6,7]
        y1 = [1, 0, 1, 3, 2,4,3]
        y2 = [0, 2, 2, 3, 4,6,5]
        y3 = [3, 1, 3, 4, 2,7,6]

        y = np.vstack([y1, y2, y3])

        labels = ["Y1 ", "Y2", "Y3"]
        color = ["orange","blue","green"]

        self.ax.stackplot(x, y1, y2, y3, labels=labels,colors=color)
        self.ax.legend(loc='upper left')
        self.ax.stackplot(x, y)
        self.fig.suptitle('Grafica Stackplot',size=9)

def create_app():
    #widget_meters = AnalogGaugeWidget()
    window = MiApp()
    #window = Login()
    window.show()
    app.exec_()

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    app.setStyle('Fusion')
    #engine = QQmlApplicationEngine()
    #engine.load(os.path.join(os.path.dirname(__file__), "qml/main.qml"))
    # with open("front/style.qss", "r") as f:
    #     _style = f.read()
    #     app.setStyleSheet(_style)
    create_app()