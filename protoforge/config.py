import os
from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class AIConfig(BaseSettings):
    provider: str = Field(default="ollama")
    model: str = Field(default="llama3.2")
    api_key: str | None = Field(default=None)
    base_url: str | None = Field(default=None)

class CloudSimConfig(BaseSettings):
    enabled: bool = Field(default=False)
    endpoint: str = Field(default="https://api.protoforge.com/sim")
    api_key: str | None = Field(default=None)

class GlobalConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="PROTOFORGE_", 
        env_file=str(Path.home() / ".protoforge" / ".env"),
        env_nested_delimiter="__"
    )
    
    ai: AIConfig = Field(default_factory=AIConfig)
    cloud_sim: CloudSimConfig = Field(default_factory=CloudSimConfig)
    data_dir: Path = Field(default=Path.home() / ".protoforge")
    parts_db: str = Field(default="parts.db")

    @property
    def db_path(self) -> Path:
        return self.data_dir / self.parts_db

def get_config() -> GlobalConfig:
    config = GlobalConfig()
    config.data_dir.mkdir(parents=True, exist_ok=True)
    return config

def save_config(config: GlobalConfig):
    """Save configuration to the data directory as an .env file."""
    config.data_dir.mkdir(parents=True, exist_ok=True)
    env_path = config.data_dir / ".env"
    with open(env_path, "w") as f:
        f.write(f"PROTOFORGE_AI__PROVIDER={config.ai.provider}\n")
        f.write(f"PROTOFORGE_AI__MODEL={config.ai.model}\n")
        if config.ai.api_key:
            f.write(f"PROTOFORGE_AI__API_KEY={config.ai.api_key}\n")
        if config.ai.base_url:
            f.write(f"PROTOFORGE_AI__BASE_URL={config.ai.base_url}\n")
        
        f.write(f"PROTOFORGE_CLOUD_SIM__ENABLED={str(config.cloud_sim.enabled).lower()}\n")
        f.write(f"PROTOFORGE_CLOUD_SIM__ENDPOINT={config.cloud_sim.endpoint}\n")
        if config.cloud_sim.api_key:
            f.write(f"PROTOFORGE_CLOUD_SIM__API_KEY={config.cloud_sim.api_key}\n")
