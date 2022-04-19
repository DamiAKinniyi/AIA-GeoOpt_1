import rhino3dm as rg
import random as ra

def createSphere(c,r,d):
    ''' 
    Generates a spiky sphere mesh geometry .
    --------------------------------------

    Parameters
    -----------
    o: sets the origin of the mesh
    r: sets the starting radius of the mesh
    d: sets the displacement for the mesh vertices
    
    Returns
    ----------
    A mesh geometry
    
    '''
    sph = rg.Sphere(c,r,d),
    sph = sph.ToNurbsSurface()
    sph2 = sph.mesh()
    vector1 = sph2.normals
    disp = r.uniform(0,d)
    pts = sph2.vertices.translation(vector1*disp)
    faces = sph2.Faces
    sph3 = rg.
    

    return sph2