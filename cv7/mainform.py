# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from draw import Draw
from algorithms import *
from Settings import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1111, 1015)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Canvas = Draw(parent=self.centralwidget)
        self.Canvas.setObjectName("Canvas")
        self.horizontalLayout.addWidget(self.Canvas)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1111, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAnalysis = QtWidgets.QMenu(parent=self.menubar)
        self.menuAnalysis.setObjectName("menuAnalysis")
        self.menuView = QtWidgets.QMenu(parent=self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuClear = QtWidgets.QMenu(parent=self.menubar)
        self.menuClear.setObjectName("menuClear")
        self.menuSettings = QtWidgets.QMenu(parent=self.menubar)
        self.menuSettings.setObjectName("menuSettings")
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
        self.actionCreate_DT = QtGui.QAction(parent=MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/icons/triangles2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionCreate_DT.setIcon(icon2)
        self.actionCreate_DT.setObjectName("actionCreate_DT")
        self.actionCreateContouLines = QtGui.QAction(parent=MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/icons/contours2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionCreateContouLines.setIcon(icon3)
        self.actionCreateContouLines.setObjectName("actionCreateContouLines")
        self.actionAnalyzeSlope = QtGui.QAction(parent=MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/icons/slope2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionAnalyzeSlope.setIcon(icon4)
        self.actionAnalyzeSlope.setObjectName("actionAnalyzeSlope")
        self.actionAnalyzeExposition = QtGui.QAction(parent=MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/icons/orientation2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionAnalyzeExposition.setIcon(icon5)
        self.actionAnalyzeExposition.setObjectName("actionAnalyzeExposition")
        self.actionDT = QtGui.QAction(parent=MainWindow)
        self.actionDT.setCheckable(True)
        self.actionDT.setObjectName("actionDT")
        self.actionContour_lines_2 = QtGui.QAction(parent=MainWindow)
        self.actionContour_lines_2.setCheckable(True)
        self.actionContour_lines_2.setObjectName("actionContour_lines_2")
        self.actionSlope = QtGui.QAction(parent=MainWindow)
        self.actionSlope.setCheckable(True)
        self.actionSlope.setObjectName("actionSlope")
        self.actionExposition = QtGui.QAction(parent=MainWindow)
        self.actionExposition.setCheckable(True)
        self.actionExposition.setObjectName("actionExposition")
        self.actionClear_results = QtGui.QAction(parent=MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/icons/clear.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionClear_results.setIcon(icon6)
        self.actionClear_results.setObjectName("actionClear_results")
        self.actionClear_all = QtGui.QAction(parent=MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/icons/clear_all.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionClear_all.setIcon(icon7)
        self.actionClear_all.setObjectName("actionClear_all")
        self.actionParameters = QtGui.QAction(parent=MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("images/icons/settings.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionParameters.setIcon(icon8)
        self.actionParameters.setObjectName("actionParameters")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuAnalysis.addAction(self.actionCreate_DT)
        self.menuAnalysis.addSeparator()
        self.menuAnalysis.addAction(self.actionCreateContouLines)
        self.menuAnalysis.addAction(self.actionAnalyzeSlope)
        self.menuAnalysis.addAction(self.actionAnalyzeExposition)
        self.menuView.addAction(self.actionDT)
        self.menuView.addAction(self.actionContour_lines_2)
        self.menuView.addAction(self.actionSlope)
        self.menuView.addAction(self.actionExposition)
        self.menuClear.addAction(self.actionClear_results)
        self.menuClear.addSeparator()
        self.menuClear.addAction(self.actionClear_all)
        self.menuSettings.addAction(self.actionParameters)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAnalysis.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuClear.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCreate_DT)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCreateContouLines)
        self.toolBar.addAction(self.actionAnalyzeSlope)
        self.toolBar.addAction(self.actionAnalyzeExposition)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionClear_results)
        self.toolBar.addAction(self.actionClear_all)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionParameters)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)
        
        #Settings
        self.settings = QtWidgets.QDialog()
        self.ui = Ui_Settings()
        self.ui.setupUi(self.settings)

        self.retranslateUi(MainWindow)
        
        #User functions
        self.actionOpen.triggered.connect(self.openClick) 
        self.actionCreate_DT.triggered.connect(self.createDTClick)
        self.actionCreateContouLines.triggered.connect(self.createContourLinesClick)
        self.actionAnalyzeSlope.triggered.connect(self.analyzeSlopeClick)
        self.actionAnalyzeExposition.triggered.connect(self.analyzeExpositionClick) 
        self.actionClear_results.triggered.connect(self.clearClick)
        self.actionClear_all.triggered.connect(self.clearAllClick) 
        
        self.actionDT.triggered.connect(self.viewDTClick)
        self.actionContour_lines_2.triggered.connect(self.viewContourLinesClick)
        self.actionSlope.triggered.connect(self.viewSlopeClick)
        self.actionExposition.triggered.connect(self.viewExpositionClick)
        
        self.actionExit.triggered.connect(MainWindow.close)

        self.actionParameters.triggered.connect(self.setParameters)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def openClick(self):
        pass 
    
    
    def createDTClick(self):
        #Get points
        points = self.Canvas.getPoints()
        
        #Create triangulation
        a = Algorithms()
        dt = a.createDT(points)
        
        #Update DT
        self.Canvas.setDT(dt)
        
        #Repaint screen
        self.Canvas.repaint()
        
        #Check menu item
        self.actionDT.setChecked(True)
        
        
    def createContourLinesClick(self):
        #Get Delaunay triangulation
        a = Algorithms()
        
        #Do we have a triangulation
        dt = self.Canvas.getDT()
        
        #No triangulation constructed
        if not dt:     
            
            #Get points
            points =  self.Canvas.getPoints() 
            
            #Create DT   
            dt = a.createDT(points)
            
            #Set results
            self.Canvas.setDT(dt)
        
        #Do we have a triangulation
        dt = self.Canvas.getDT()
        
        #Get contour line parameters
        zmin = float(self.ui.lineEdit.text())
        zmax = float(self.ui.lineEdit_2.text())
        dz = float(self.ui.lineEdit_3.text())
        
        #Create contour lines
        contours = a.createContourLines(dt, zmin, zmax, dz)
        
        #Set results
        self.Canvas.setContours(contours)
        
        #Repaint screen
        self.Canvas.repaint()
        
        #Check menu item
        self.actionContour_lines_2.setChecked(True)
    
        
    def analyzeSlopeClick(self):
    
        #Get Delaunay triangulation
        a = Algorithms()
        
        #Do we have a triangulation
        dt = self.Canvas.getDT()
        
        #No triangulation constructed
        if not dt:     
            
            #Get points
            points =  self.Canvas.getPoints() 
            
            #Create DT   
            dt = a.createDT(points)
            
            #Set results
            self.Canvas.setDT(dt)
        
        #Do we have a triangulation
        dt = self.Canvas.getDT()
        
        #Analyze dtm slope
        dtm_slope = a.analyzeDTMSlope(dt)
        
        #Set results
        self.Canvas.setDTMSlope(dtm_slope)
        
        #Repaint screen
        self.Canvas.repaint()  
        
        #Check menu item
        self.actionSlope.setChecked(True)  
        
        
    def analyzeExpositionClick(self):
        pass
    

    def clearClick(self):
        #Clear results
        self.Canvas.clearResults()
        
        #Repaint screen
        self.Canvas.repaint()    
    
    
    def clearAllClick(self):
        #Clear all data
        self.Canvas.clearAll()
        
        #Repaint screen
        self.Canvas.repaint()
    
    
    def viewDTClick(self):
        #Enable/disable drawing
        self.Canvas.setViewDT(self.actionDT.isChecked())
        
        #Update
        self.Canvas.update()


    def viewContourLinesClick(self):
        #Enable/disable drawing
        self.Canvas.setViewContourLines(self.actionContour_lines_2.isChecked())
        
        #Update
        self.Canvas.update()
    
    
    def viewSlopeClick(self):
        #Enable/disable drawing
        self.Canvas.setViewSlope(self.actionSlope.isChecked())
        
        #Update
        self.Canvas.update()


    def viewExpositionClick(self):
        #Enable/disable drawing
        self.Canvas.setViewAspect(self.actionExposition.isChecked())
        
        #Update
        self.Canvas.update()
    
    
    def setParameters(self):
        self.settings.show()
    
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DTM Analysis"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAnalysis.setTitle(_translate("MainWindow", "Analysis"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuClear.setTitle(_translate("MainWindow", "Clear"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setToolTip(_translate("MainWindow", "Open file"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setToolTip(_translate("MainWindow", "Exit application"))
        self.actionExit.setShortcut(_translate("MainWindow", "Backspace"))
        self.actionCreate_DT.setText(_translate("MainWindow", "Create DT"))
        self.actionCreate_DT.setToolTip(_translate("MainWindow", "Create Delaunay triangulation"))
        self.actionCreateContouLines.setText(_translate("MainWindow", "Create contour lines"))
        self.actionAnalyzeSlope.setText(_translate("MainWindow", "Analyze slope"))
        self.actionAnalyzeSlope.setToolTip(_translate("MainWindow", "Analyze DTM slope"))
        self.actionAnalyzeExposition.setText(_translate("MainWindow", "Analyze exposition"))
        self.actionAnalyzeExposition.setToolTip(_translate("MainWindow", "Analyze DTM exposition"))
        self.actionDT.setText(_translate("MainWindow", "DT"))
        self.actionContour_lines_2.setText(_translate("MainWindow", "Contour lines"))
        self.actionSlope.setText(_translate("MainWindow", "Slope"))
        self.actionExposition.setText(_translate("MainWindow", "Exposition"))
        self.actionClear_results.setText(_translate("MainWindow", "Clear results"))
        self.actionClear_all.setText(_translate("MainWindow", "Clear all"))
        self.actionParameters.setText(_translate("MainWindow", "Parameters"))
        self.actionParameters.setToolTip(_translate("MainWindow", "Parameter settings"))
from draw import Draw


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
