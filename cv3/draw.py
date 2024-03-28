from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtGui import QMouseEvent, QPaintEvent
from PyQt6.QtWidgets import *


class Draw(QWidget):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.building = QPolygonF()
        self.mbr = QPolygonF()


    def mousePressEvent(self, e: QMouseEvent):
        
        #Get coordinates of q
        x = e.position().x()
        y = e.position().y()
        
        #Add new vertex
        p = QPointF(x, y)
            
        #Add p to polygon
        self.building.append(p)
            
        #Repaint screen
        self.repaint()
        
        
    def paintEvent(self, e: QPaintEvent):
        #Draw situation
        
        #Create new graphic object
        qp = QPainter(self)
        
        #Start drawing
        qp.begin(self)
        
        #Set graphical attributes
        qp.setPen(Qt.GlobalColor.black)
        qp.setBrush(Qt.GlobalColor.yellow)
        
        #Draw building
        qp.drawPolygon(self.building)
        
        #Set graphical attributes MBR
        qp.setPen(Qt.GlobalColor.red)
        qp.setBrush(Qt.GlobalColor.transparent)
        
        #Draw MBR
        qp.drawPolygon(self.mbr)
    
        #End drawing
        qp.end()
        
         
    def getBuilding(self):
        # Return building
        return self.building
    
    
    def setMBR(self, mbr):
        # set mbr to input
        self.mbr = mbr  
        
    
    def clearData(self):
        #Clear building
        self.building.clear()
        
        #Clear CH
        self.ch.clear()
        
        #Clear MBR
        self.mbr.clear()
                
        #Repaint screen
        self.repaint()
        
        