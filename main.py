from app.io import FileReader
from app.controller import ModelBuilder, ModelSolver

path = r"C:\Users\hp\Documents\School\S3a\Recherche Opérationnelle\Projet\saves\test-1.pynet"

reader = FileReader(path)
net = reader.read_network()

matrix = net.get_network_matrix()

for router in net.routers:
    print(router)

for row in matrix:
    print(f"{row},")

builder = ModelBuilder(net, security_requirement=2, firewall_required=False)
builder.set_source(1)
builder.set_destination(3)
model = builder.build_model()

model.optimize()

solver = ModelSolver(builder)
path = solver.create_path()

if path is not None:
    print(path)
else:
    print("No path found.")