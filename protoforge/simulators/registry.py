from typing import Dict, Type
from protoforge.simulators.base import BaseSimulator

class SimulatorRegistry:
    def __init__(self):
        self._simulators: Dict[str, BaseSimulator] = {}

    def register(self, simulator: BaseSimulator):
        self._simulators[simulator.name.lower()] = simulator

    def get(self, name: str) -> BaseSimulator | None:
        return self._simulators.get(name.lower())

    def list_all(self) -> Dict[str, BaseSimulator]:
        return self._simulators

    def load_plugins(self):
        """Load external simulators from entry points."""
        import importlib.metadata
        eps = importlib.metadata.entry_points(group='protoforge.simulators')
        for ep in eps:
            try:
                sim_cls = ep.load()
                sim = sim_cls()
                self.register(sim)
            except Exception as e:
                # In a real app we'd log this gracefully
                pass

registry = SimulatorRegistry()
registry.load_plugins()
