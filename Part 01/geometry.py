import rhino3dm as rg
import random as ra

def createSphere(o,r1, c):
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
    sph = rg.Sphere(o,r1)
    pts = []

    for i in range(c):
        u = ra.uniform(0,1)
        v = ra.uniform(0,1)
        pt = sph.PointAt(u,v)

        pts.append(pt)


    return pts
    
    
        
    #pts = sph2.Vertices
    '''sph3= []
    for i in range(len(pts)):
        smallRad = ra.uniform(r1/5,r2)
        smallSph = rg.Sphere(rg.Point3d[pts[i]], smallRad )
        smallSph = smallSph.ToNurbsSurface()
        sph3.append[sph3]'''


    '''vector1 = sph2.Normals.UnitizeNormals()
    pts= []
    for i in range(len(sph2.Vertices)):
        disp = ra.uniform(0,d)
        pts.append(rg.point3d[sph2.Vertices[i]].translation(vector1*disp))

    #pts =[rg.point3d[i].translation(vector1*disp) for i in sph2.Vertices]
    faces = sph2.Faces
    sph3 = rg.MeshNgon()
    sph3 = sph3.create(pts, faces)'''
    

    #return sph2
    #[rg.Point3d(pts[i]) for i in pts]