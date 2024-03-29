# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from draw import Draw
from algorithms import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1095, 708)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Canvas = Draw(parent=self.centralwidget)
        self.Canvas.setObjectName("Canvas")
        self.horizontalLayout.addWidget(self.Canvas)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1095, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuInput = QtWidgets.QMenu(parent=self.menubar)
        self.menuInput.setObjectName("menuInput")
        self.menuAnalyze = QtWidgets.QMenu(parent=self.menubar)
        self.menuAnalyze.setObjectName("menuAnalyze")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(parent=MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionOpen = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icons/open_file.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtGui.QAction(parent=MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/icons/exit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionExit.setIcon(icon1)
        self.actionExit.setObjectName("actionExit")
        self.actionPoint_Polygon = QtGui.QAction(parent=MainWindow)
        self.actionPoint_Polygon.setCheckable(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/icons/pointpol.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionPoint_Polygon.setIcon(icon2)
        self.actionPoint_Polygon.setObjectName("actionPoint_Polygon")
        self.actionClear = QtGui.QAction(parent=MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/icons/clear_all.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionClear.setIcon(icon3)
        self.actionClear.setObjectName("actionClear")
        self.actionRay_Crossing_Algorithm = QtGui.QAction(parent=MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/icons/ray.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionRay_Crossing_Algorithm.setIcon(icon4)
        self.actionRay_Crossing_Algorithm.setObjectName("actionRay_Crossing_Algorithm")
        self.actionWinding_Number_Algorithm = QtGui.QAction(parent=MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/icons/winding.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionWinding_Number_Algorithm.setIcon(icon5)
        self.actionWinding_Number_Algorithm.setObjectName("actionWinding_Number_Algorithm")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuInput.addAction(self.actionPoint_Polygon)
        self.menuInput.addSeparator()
        self.menuInput.addAction(self.actionClear)
        self.menuAnalyze.addAction(self.actionRay_Crossing_Algorithm)
        self.menuAnalyze.addAction(self.actionWinding_Number_Algorithm)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuInput.menuAction())
        self.menubar.addAction(self.menuAnalyze.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPoint_Polygon)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRay_Crossing_Algorithm)
        self.toolBar.addAction(self.actionWinding_Number_Algorithm)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionClear)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        
        self.actionOpen.triggered.connect(self.openClick) # type: ignore
        self.actionPoint_Polygon.triggered.connect(self.pointPolygonClick) # type: ignore
        self.actionClear.triggered.connect(self.clearClick) # type: ignore
        self.actionRay_Crossing_Algorithm.triggered.connect(self.rayCrossingClick) # type: ignore
        self.actionWinding_Number_Algorithm.triggered.connect(self.windingNumberClick) # type: ignore
        self.actionExit.triggered.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
    def openClick(self):
        pass
        
        
    def pointPolygonClick(self):
        #Draw point or add vertex to polygon
        self.Canvas.switchDrawing()
     
        
    def clearClick(self):
        # Clear data
        self.Canvas.clearData()
        
        
    def rayCrossingClick(self):
        
        #Get data
        q = self.Canvas.getQ()
        pol = self.Canvas.getPol()
        
        #Run analysis
        a = Algorithms()
        result = a.analyzePointPolygonPosition(q, pol)
        
        #Show results
        mb = QtWidgets.QMessageBox()
        mb.setWindowTitle('Analyze point and polygon position')
        
        #Point inside
        if result:
            mb.setText("Point inside polygon.")
  
        #Point outside
        else:
            mb.setText("Point outside polygon.")
            
        #Show window
        mb.exec()
        
        
        
    def windingNumberClick(self):
        pass
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Point and polygon position"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuInput.setTitle(_translate("MainWindow", "Input"))
        self.menuAnalyze.setTitle(_translate("MainWindow", "Analyze"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setToolTip(_translate("MainWindow", "Open file"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setToolTip(_translate("MainWindow", "Close application"))
        self.actionPoint_Polygon.setText(_translate("MainWindow", "Point/Polygon"))
        self.actionPoint_Polygon.setToolTip(_translate("MainWindow", "Input point/polygon vertex"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
        self.actionClear.setToolTip(_translate("MainWindow", "Clear data"))
        self.actionRay_Crossing_Algorithm.setText(_translate("MainWindow", "Ray Crossing Algorithm"))
        self.actionWinding_Number_Algorithm.setText(_translate("MainWindow", "Winding Number Algorithm"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
