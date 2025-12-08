from PySide6.QtCore import QThread, Signal

from app.controller import ModelSolver

class PathFinderThread(QThread):
    finished = Signal(object, object)

    def __init__(self, builder):
        super().__init__()
        self.builder = builder

    def run(self):
        self.builder.build_model()
        solver = ModelSolver(self.builder)
        path = solver.create_path()
        self.finished.emit(solver, path)