from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from qpoint3df import *
from edge import *
from random import *
from triangle import *
from math import *


class Draw(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.points = []
        self.dt = []
        self.contours = []
        self.dtm_slope = []
        self.dtm_aspect = []
        self.drawDT = True
        self.drawContourLines = True
        self.drawSlope = True
        self.drawAspect = True
        


    def mousePressEvent(self, e:QMouseEvent):
        #Get cursor position
        x = e.position().x()
        y = e.position().y()
        
        #Generate random height
        zmin = 150
        zmax = 400
        z = random() * (zmax - zmin) + zmin
        
        #Create new point
        p = QPoint3DF(x, y, z)

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
        qp.setPen(Qt.GlobalColor.gray)
      
        #Draw slope
        for t in self.dtm_slope:
            #Get slope
            slope = t.getSlope()
            
            #Convert slope to color
            mju = 2*255/pi
            col = int(255 - mju*slope)
            color = QColor(col, col, col)
            qp.setBrush(color)
            
            #Draw triangle
            qp.drawPolygon(t.getVertices())
            
        
        #DRAW DT
        if self.drawDT:     
            #Set graphic attributes
            qp.setPen(Qt.GlobalColor.green)
            qp.setBrush(Qt.GlobalColor.transparent)
            
            #Draw triangulation
            for e in self.dt:
                qp.drawLine(int(e.getStart().x()), int(e.getStart().y()), int(e.getEnd().x()), int(e.getEnd().y()))

        #Set graphic attributes
        qp.setPen(Qt.GlobalColor.gray)
        qp.setBrush(Qt.GlobalColor.yellow)
        
        #Draw contour lines
        for e in self.contours:
            qp.drawLine(int(e.getStart().x()), int(e.getStart().y()), int(e.getEnd().x()), int(e.getEnd().y()))
                
        #Set graphic attributes
        qp.setPen(Qt.GlobalColor.black)
        qp.setBrush(Qt.GlobalColor.yellow)

        #Draw points
        r = 10
        for p in self.points:
            qp.drawEllipse(int(p.x()-r), int(p.y()-r), 2*r, 2*r)
       
    

        #End drawing
        qp.end()
        
    
    def getPoints(self):
        # Return points
        return self.points
    
    def getDT(self):
        #Return DT
        return self.dt
    
    def clearAll(self):
        #Clear points
        self.points.clear()
        
        #Clear DT
        self.dt.clear()
        
        #Repaint screen
        self.repaint()
        
    
    def setDT(self, dt: list[Edge]):
        self.dt = dt
        
        
    def setContours(self, contours: list[Edge]):
        self.contours = contours


    def setDTMAspect(self, dtm_aspect: list[Triangle]):
        self.dtm_aspect = dtm_aspect    
        
    
    def setDTMSlope(self, dtm_slope: list[Triangle]):
        self.dtm_slope = dtm_slope
    