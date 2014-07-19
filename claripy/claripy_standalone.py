from .claripy import Claripy
from .solvers import BranchingSolver
from .backends import BackendZ3, BackendConcrete
from .datalayer import DataLayer

class ClaripyStandalone(Claripy):
    def __init__(self, expression_backends=None, solver_backend=None, results_backend=None):
        expression_backends = [ BackendConcrete(self), BackendZ3(self) ] if expression_backends is None else expression_backends

        solver_backend = BackendZ3(self) if solver_backend is None else solver_backend
        results_backend = BackendConcrete(self) if results_backend is None else results_backend
        Claripy.__init__(self, expression_backends, solver_backend, results_backend)
        self.dl = DataLayer()

    def solver(self):
        return BranchingSolver(self)
