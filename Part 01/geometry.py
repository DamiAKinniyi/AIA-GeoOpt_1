import rhino3dm as rg

def createSphere(c,r):
    sph = rg.Sphere(c,r)
    sph = sph.ToNurbsSurface()
    sph2 = sph.mesh()
    return sph2