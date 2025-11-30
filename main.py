from app.model import Network

net = Network(1, "MyNet")

net.add_router("A", 9.9, 2.4, 4)
net.add_router("B", 9.9, 2.4, 4)
net.add_router("C", 9.9, 2.4, 4)
net.add_router("D", 9.9, 2.4, 4)
net.add_router("E", 9.9, 2.4, 4)

net.print_routers()

net.link(0, 1, 1.0)
net.link(0, 2, 5.0)
net.link(1, 3, 6.0)
net.link(2, 4, 8.0)

matrix = net.get_network_matrix()
for row in matrix:
    print(str(row) + ",")
    
path = net.create_path([0, 1, 3], 4)
if path is not None:
    print(path)
    print(path.path_cost())
    
    
path = net.create_path([3, 1, 0, 2, 4], 4)
if path is not None:
    print(path)
    print(path.path_cost())
    
print("----- Saving Network -----")
    
from app.io import FileWriter

writer = FileWriter(r"C:\Users\hp\Downloads" , "output")
writer.write_network(net)

from app.io import FileReader

reader = FileReader(r"C:\Users\hp\Downloads\output.pynet")
loaded_net = reader.read_network()
loaded_net.print_routers()

matrix = loaded_net.get_network_matrix()
for row in matrix:
    print(str(row) + ",")