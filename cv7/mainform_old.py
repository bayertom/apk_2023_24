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
        MainWindow.resize(646, 488)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Canvas = Draw(parent=self.centralwidget)
        self.Canvas.setObjectName("Canvas")
        self.horizontalLayout.addWidget(self.Canvas)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 646, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAnalysis = QtWidgets.QMenu(parent=self.menubar)
        self.menuAnalysis.setObjectName("menuAnalysis")
        self.menuView = QtWidgets.QMenu(parent=self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuClear = QtWidgets.QMenu(parent=self.menubar)
        self.menuClear.setObjectName("menuClear")
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
        self.actionCreate_DTM = QtGui.QAction(parent=MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/icons/triangles2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionCreate_DTM.setIcon(icon2)
        self.actionCreate_DTM.setObjectName("actionCreate_DTM")
        self.actionCreate_contour_lines = QtGui.QAction(parent=MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/icons/contours2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionCreate_contour_lines.setIcon(icon3)
        self.actionCreate_contour_lines.setObjectName("actionCreate_contour_lines")
        self.actionAnalyze_slope = QtGui.QAction(parent=MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/icons/slope2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionAnalyze_slope.setIcon(icon4)
        self.actionAnalyze_slope.setObjectName("actionAnalyze_slope")
        self.actionAnalyze_exposition = QtGui.QAction(parent=MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/icons/orientation2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionAnalyze_exposition.setIcon(icon5)
        self.actionAnalyze_exposition.setObjectName("actionAnalyze_exposition")
        self.actionDTM = QtGui.QAction(parent=MainWindow)
        self.actionDTM.setCheckable(True)
        self.actionDTM.setObjectName("actionDTM")
        self.actionCountour_lines = QtGui.QAction(parent=MainWindow)
        self.actionCountour_lines.setCheckable(True)
        self.actionCountour_lines.setObjectName("actionCountour_lines")
        self.actionSlope = QtGui.QAction(parent=MainWindow)
        self.actionSlope.setCheckable(True)
        self.actionSlope.setObjectName("actionSlope")
        self.actionExposition = QtGui.QAction(parent=MainWindow)
        self.actionExposition.setCheckable(True)
        self.actionExposition.setObjectName("actionExposition")
        self.actionResults = QtGui.QAction(parent=MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/icons/clear.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionResults.setIcon(icon6)
        self.actionResults.setObjectName("actionResults")
        self.actionClear_all = QtGui.QAction(parent=MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/icons/clear_all.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionClear_all.setIcon(icon7)
        self.actionClear_all.setObjectName("actionClear_all")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuAnalysis.addAction(self.actionCreate_DTM)
        self.menuAnalysis.addSeparator()
        self.menuAnalysis.addAction(self.actionCreate_contour_lines)
        self.menuAnalysis.addAction(self.actionAnalyze_slope)
        self.menuAnalysis.addAction(self.actionAnalyze_exposition)
        self.menuView.addAction(self.actionDTM)
        self.menuView.addAction(self.actionCountour_lines)
        self.menuView.addAction(self.actionSlope)
        self.menuView.addAction(self.actionExposition)
        self.menuClear.addAction(self.actionResults)
        self.menuClear.addAction(self.actionClear_all)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAnalysis.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuClear.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCreate_DTM)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCreate_contour_lines)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAnalyze_slope)
        self.toolBar.addAction(self.actionAnalyze_exposition)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionResults)
        self.toolBar.addAction(self.actionClear_all)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        
        #User functions
        self.actionOpen.triggered.connect(self.openClick) 
        self.actionCreate_DTM.triggered.connect(self.createDTClick)
        self.actionCreate_contour_lines.triggered.connect(self.createContourLinesClick)
        self.actionAnalyze_slope.triggered.connect(self.analyzeSlopeClick)
        self.actionAnalyze_exposition.triggered.connect(self.analyzeExpositionClick) 
        self.actionResults.triggered.connect(self.clearClick)
        self.actionClear_all.triggered.connect(self.clearAllClick) 
        
        self.actionDTM.triggered.connect(self.viewDTClick)
        self.actionCountour_lines.triggered.connect(self.viewContourLinesClick)
        self.actionSlope.triggered.connect(self.viewSlopeClick)
        self.actionExposition.triggered.connect(self.viewExpositionClick) 
        self.actionExit.triggered.connect(MainWindow.close)
        
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
        
        #Create contour lines
        contours = a.createContourLines(dt, 100, 1500, 10)
        
        #Set results
        self.Canvas.setContours(contours)
        
        #Repaint screen
        self.Canvas.repaint()
    
        
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
        
        
    def analyzeExpositionClick(self):
        pass
    

    def clearClick(self):
        pass        
    
    
    def clearAllClick(self):
        #Clear all data
        self.Canvas.clearAll()
        
        #Repaint screen
        self.Canvas.repaint()
    
    
    def viewDTClick(self):
        pass


    def viewContourLinesClick(self):
        pass
    
    
    def viewSlopeClick(self):
        pass


    def viewExpositionClick(self):
        pass
    
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DTM Analysis"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAnalysis.setTitle(_translate("MainWindow", "Analysis"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuClear.setTitle(_translate("MainWindow", "Clear"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionCreate_DTM.setText(_translate("MainWindow", "Create DTM"))
        self.actionCreate_contour_lines.setText(_translate("MainWindow", "Create contour lines"))
        self.actionAnalyze_slope.setText(_translate("MainWindow", "Analyze slope"))
        self.actionAnalyze_exposition.setText(_translate("MainWindow", "Analyze exposition"))
        self.actionDTM.setText(_translate("MainWindow", "DTM"))
        self.actionCountour_lines.setText(_translate("MainWindow", "Countour lines"))
        self.actionSlope.setText(_translate("MainWindow", "Slope"))
        self.actionExposition.setText(_translate("MainWindow", "Exposition"))
        self.actionResults.setText(_translate("MainWindow", "Clear results"))
        self.actionClear_all.setText(_translate("MainWindow", "Clear all"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
