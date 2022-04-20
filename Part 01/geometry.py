import rhino3dm as rg
import random as ra
import math

def createSphere(o,r1):
    ''' 
    Generates a sphere geometry .
    --------------------------------------

    Parameters
    -----------
    o: sets the origin of the mesh
    r: sets the starting radius of the sphere
        
    Returns
    ----------
    A NURBS sphere
    
    '''
    sph = rg.Sphere(o,r1)
    sph = sph.ToNurbsSurface()
    return sph    