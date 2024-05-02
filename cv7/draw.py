from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from qpoint3df import *
from edge import *


class Draw(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.points = []
        self.dt = []


    def mousePressEvent(self, e:QMouseEvent):
        #Get cursor position
        x = e.position().x()
        y = e.position().y()
        
        #Create new point
        p = QPointF(x,y)

        #Add point to the point cloud
        self.points.append(p)

        #Repaint screen
        self.repaint()
        

    def paintEvent(self,  e:QPaintEvent):
        #Draw situation
        
        #Create new object
        qp = QPainter(self)

        #Start drawing
        qp.begin(self)
            
        #Set graphic attributes
        qp.setPen(Qt.GlobalColor.green)
        qp.setBrush(Qt.GlobalColor.transparent)
        
        #Draw triangulation
        for e in self.dt:
            qp.drawLine(int(e.getStart().x()), int(e.getStart().y()), int(e.getEnd().x()), int(e.getEnd().y()))
                
       
        #Set graphic attributes
        qp.setPen(Qt.GlobalColor.black)
        qp.setBrush(Qt.GlobalColor.yellow)

        #Draw points
        r = 10
        for p in self.points:
            qp.drawEllipse(int(p.x()-r), int(p.y()-r), 2*r, 2*r)
       
        #Draw contour lines        
        
        #Draw slope
        
        #Draw aspect

        #End drawing
        qp.end()
        
    
    def getPoints(self):
        # Return points
        return self.points
    
    
    def clearAll(self):
        #Clear points
        self.points.clear()
        
        #Clear DT
        self.dt.clear()
        
        #Repaint screen
        self.repaint()
        
    
    def setDT(self, dt: list[Edge]):
        self.dt = dt
        
    