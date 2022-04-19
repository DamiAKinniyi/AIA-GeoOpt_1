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
        hs.HopsNumber("Radius", "R", "Set sphere radius"),
        hs.HopsNumber("Displacement", "D", "Set displacement")
    ],
    outputs = [
        hs.HopsMesh('Sphere', 'S', "Sphere Geometry")
    ]
)

def create(o, r, d):
    return geo.createSphere(o, r, d)


if __name__== "__main__":
    app.run(debug=True)