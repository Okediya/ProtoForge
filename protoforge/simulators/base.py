from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseSimulator(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def is_available(self) -> bool:
        """Check if the external simulator tool is installed."""
        pass

    @abstractmethod
    def run(self, scenario: str, params: Dict[str, Any], headless: bool = True) -> Dict[str, Any]:
        """Execute a simulation scenario."""
        pass

    @abstractmethod
    def get_install_instructions(self) -> str:
        """Provide instructions on how to install this simulator."""
        pass
