from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from math import *


#Processing data
class Algorithms:
    
    def __init__(self):
        pass
    
    
    def analyzePointPolygonPosition(self, q:QPointF, pol:QPolygonF):
        
        #Inicialize amount of intersections
        k = 0
        
        #Amount of vertices
        n = len(pol)
        
        #Process all segments
        for i in range(n):
            #Reduce coordinates
            xir = pol[i].x() - q.x()
            yir = pol[i].y() - q.y()
            
            xi1r = pol[(i+1)%n].x() - q.x()
            yi1r = pol[(i+1)%n].y() - q.y()
            
            #Suitable segment?
            if ((yi1r > 0) and (yir <= 0)) or ((yir > 0) and (yi1r <= 0)):
               
               #Compute intersection
               xm = (xi1r * yir - xir * yi1r)/(yi1r - yir)
               
               #Right half plane
               if xm > 0:       
                   k += 1  
                   
        #Point q inside polygon?
        if (k%2 == 1):
            return 1
        
        #Point q outside polygon
        return 0
     
    def get2LineAngle(self, p1:QPointF, p2:QPointF, p3:QPointF, p4:QPointF):
                
        #Get 2 line angle
        ux = p2.x() - p1.x()
        uy = p2.y() - p1.y() 
        
        vx = p4.x() - p3.x()
        vy = p4.y() - p3.y()         
        
        #Dot product
        dot = ux * vx + uy * vy  
        
        #Vector norms
        nu = (ux**2 + uy**2)**(1/2)
        nv = (vx**2 + vy**2)**(1/2)
        
        return acos(dot/(nu*nv))
  
                   
    def cHull(self, pol:QPolygonF):
        # CH construction using Jarvis scan algorithm
        ch = QPolygonF()
        
        #Find pivot 1
        q = min(pol, key = lambda k: k.y() )
        
        #Find pivot 2
        s = min(pol, key = lambda k: k.x() )
        
        #Initialize last 2 points of CH
        qj = q
        qj1 = QPointF(s.x(), q.y())
        
        #Add pivot to CH
        ch.append(q)
        
        #Find all points of CH
        while True:
            #Maximum and its index
            omega_max = 0
            index_max = -1
            
            #Process all point
            for i in range(len(pol)):
                
                #Compute angle
                omega = self.get2LineAngle(qj, qj1, qj, pol[i])
                
                #Update maximum
                if omega > omega_max:
                    omega_max = omega
                    index_max = i
                    
            #Append point to CH
            ch.append(pol[index_max])
            
            #We found pivot again
            if pol[index_max] == q:
                break        
                
            #Update last segment of CH
            qj1 = qj
            qj = pol[index_max]
            
        return ch    
            
    def mmb(self, pol:QPolygonF):
        
        #Compute points with extreme coordinates
        px_min = min(pol, key = lambda k: k.x() )
        px_max = max(pol, key = lambda k: k.x() )      
        py_min = min(pol, key = lambda k: k.y() )
        py_max = max(pol, key = lambda k: k.y() )          
        
        #Compute min-max box points
        v1 = QPointF(px_min.x(), py_min.y())
        v2 = QPointF(px_max.x(), py_min.y())
        v3 = QPointF(px_max.x(), py_max.y())
        v4 = QPointF(px_min.x(), py_max.y())
        
        #Create min max box
        box = QPolygonF([v1, v2, v3, v4])       
        
        return box
    
    
    def rotate(self, pol:QPolygonF, sig:float):
        #Rotate polygon by given angle
    
        pol_r = QPolygonF()
        
        #Process all points
        for p in pol:
            #Rotate point
            x_r = p.x() * cos(sig) - p.y() * sin(sig)
            y_r = p.x() * sin(sig) + p.y() * cos(sig)
    
            #Ceate rotated point
            p_r = QPointF(x_r, y_r)
            
            #Add to polygon
            pol_r.append(p_r)
            
        return pol_r
        
    
        