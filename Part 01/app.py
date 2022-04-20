from flask import Flask
import ghhops_server as hs
import geometry as geo

app = Flask(__name__)
hops = hs.Hops(app)

@hops.component (
    "/createSpikyMesh",
    name = "Spiky_Mesh", 
    inputs = [
        hs.HopsPoint('Origin', 'O', 'Set centre point of the sphere'),
        hs.HopsNumber("Radius", "R", "Set sphere radius", default=2),
        
    ],
    outputs = [
        hs.HopsSurface('Sphere', 'S', "Sphere Geometry", hs.HopsParamAccess.ITEM)
    ]
)

def create(o, r):
    return geo.createSphere(o, r)


if __name__== "__main__":
    app.run(debug=True)