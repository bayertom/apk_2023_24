from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from math import *
from numpy import *
from scipy.linalg import *
from qpoint3df import *

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
        
        #Correct interval
        arg = dot/(nu*nv)
        
        return acos(max(min(arg, 1), -1))
        
                   
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
                if qj != pol[i]:
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
         
            
    def createMMB(self, pol:QPolygonF):
        
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
    
        
    def getArea(self, pol : QPolygonF):
        #Return polygon area
        area = 0
        n = len(pol)  
          
        #Proccesing of vertexes
        for i in range(n):
            area = area + pol[i].x() * (pol[(i+1)%n].y() - pol[(i-1+n)%n].y())
            
        return abs(area)/2
    
    
    def resizeRectangle(self, rect: QPolygonF, build: QPolygonF):
        #Resize rectangle to fit area of the building
        
        #Compute areas
        Ab = self.getArea(build)
        A = self.getArea(rect)
        
        #Compute ratio
        k = Ab/A
        
        #Center of mass
        tx = (rect[0].x() + rect[1].x() + rect[2].x() + rect[3].x()) / 4
        ty = (rect[0].y() + rect[1].y() + rect[2].y() + rect[3].y()) / 4
        
        #Vectors 
        u1x = rect[0].x() - tx
        u1y = rect[0].y() - ty
        u2x = rect[1].x() - tx
        u2y = rect[1].y() - ty
        u3x = rect[2].x() - tx
        u3y = rect[2].y() - ty
        u4x = rect[3].x() - tx
        u4y = rect[3].y() - ty
        
        #New vertices
        v1x = tx + sqrt(k) * u1x
        v1y = ty + sqrt(k) * u1y
        v2x = tx + sqrt(k) * u2x
        v2y = ty + sqrt(k) * u2y
        v3x = tx + sqrt(k) * u3x
        v3y = ty + sqrt(k) * u3y
        v4x = tx + sqrt(k) * u4x
        v4y = ty + sqrt(k) * u4y
        
        v1 = QPointF(v1x, v1y)
        v2 = QPointF(v2x, v2y)
        v3 = QPointF(v3x, v3y)
        v4 = QPointF(v4x, v4y)
        
        #Add vertices to polygon
        rectR = QPolygonF([v1, v2, v3, v4])
        
        return rectR
    
    
    def createMBR(self, pol : QPolygonF):
        #Create minimum bounding rectangle        
    
        #Compute convex hull
        ch = self.cHull(pol)
        
        #Initialization
        mmb_min = self.createMMB(ch)
        area_min = self.getArea(mmb_min)
        sigma_min = 0
        
        #Process all segments of CH
        n = len(ch)
        for i in range(n):
            #Coordinate differences
            dx = ch[(i+1)%n].x() - ch[i].x()
            dy = ch[(i+1)%n].y() - ch[i].y()
            
            #Direction
            sigma = atan2(dy, dx)
            
            #Rotate convex hull by -sigma
            ch_rot = self.rotate(ch, -sigma)
            
            #Find mmb and its area
            mmb_rot = self.createMMB(ch_rot)
            area_rot = self.getArea(mmb_rot)
            
            #Is it a better approximation?
            if area_rot < area_min:
                mmb_min = mmb_rot
                area_min = area_rot
                sigma_min = sigma
        
        #Back rotation
        mmb_unrot = self.rotate(mmb_min, sigma_min)
        
        #Resize rectangle
        mmb_res = self.resizeRectangle(mmb_unrot, pol) 
        
        return mmb_res   
    
    
    def createERPCA(self, pol:QPolygonF):
        #Create enclosing rectangle using PCA
        x = []
        y = []
        
        #Add coordinates to lists
        for p in pol:
            x.append(p.x())
            y.append(p.y())
            
        #Create array
        P = array([x, y])
        
        #Compute covariation matrix
        C = cov(P)
        
        #Singular value decomposition
        [U, S, V] = svd(C)
        
        #Compute sigma
        sigma = atan2(V[0][1], V[0][0])
        
        #Rotate polygon by minus sigma
        pol_unrot = self.rotate(pol, -sigma)
        
        #Find min-max box
        mmb = self.createMMB(pol_unrot)
        
        #Rotate min-max box (create enclosing rectangle)
        er = self.rotate(mmb, sigma)
        
        #Resize enclosing rectangle
        er_r = self.resizeRectangle(er, pol)
        
        return er_r
   
   
    def getPointAndLinePosition(self, p: QPoint3DF, p1: QPoint3DF, p2: QPoint3DF): 
        # Analyze point and line position
        ux = p2.x() - p1.x()
        uy = p2.y() - p1.y()
        
        vx = p.x() - p1.x()
        vy = p.y() - p1.y()
        
        #Compute test
        t = ux*vy - uy*vx
        
        #Point in the left half plane
        if t > 0:
            return 1
        
        #Point in the right half plane
        if t < 0:
            return 0
        
        #Point on the line
        return -1
    
        
    def getNearestPoint(self, q:QPoint3DF, points:list[QPoint3DF]):
        #Find point nearest to q
        p_nearest = None
        dist_nearest = inf
        
        #Process all points
        for p in points:
            #Point p differente from q
            if p!=q:
                #Compute distance
                dx = p.x() - q.x()
                dy = p.y() - q.y()
                
                dist = sqrt(dx**2 + dy**2)
                
                #Update nearest point
                if dist < dist_nearest:
                    p_nearest = p
                    dist_nearest = dist
        
        return p_nearest
        
                
    def getDelaunayPoint(self, start:QPoint3DF,end:QPoint3DF, points:list[QPoint3DF]):
        #Find Delaunay point to an edge
        p_dt = None
        angle_max = 0   
             
        #Process all points
        for p in points:
            
            #Point p differente from q
            if start != p and end != p:
                
                #Point in the left halfplane
                if self.getPointAndLinePosition(p, start, end) == 1:
                    
                    #Compute angle
                    angle = self.get2LineAngle(p, start, p, end)
                
                    # Update maximum
                    if angle > angle_max:
                        angle_max = angle
                        p_dt = p
                
        return p_dt