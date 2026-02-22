from pathlib import Path
import yaml
from pydantic import BaseModel, Field
from typing import List, Dict, Any

class PartReference(BaseModel):
    category: str
    name: str
    quantity: int = 1
    params: Dict[str, Any] = Field(default_factory=dict)

class ProtoProject(BaseModel):
    name: str
    version: str = "0.1.0"
    description: str | None = None
    parts: List[PartReference] = Field(default_factory=list)
    sim_settings: Dict[str, Any] = Field(default_factory=dict)

    @classmethod
    def load(cls, path: Path) -> "ProtoProject":
        with open(path, "r") as f:
            data = yaml.safe_load(f)
        return cls(**data)

    def save(self, path: Path) -> None:
        with open(path, "w") as f:
            yaml.dump(self.model_dump(), f)

def find_project_root(start_path: Path = Path.cwd()) -> Path | None:
    current = start_path
    while current != current.parent:
        if (current / "protoforge.yaml").exists():
            return current
        current = current.parent
    return None
