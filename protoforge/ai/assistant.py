import litellm
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from protoforge.config import AIConfig

class AIResponse(BaseModel):
    content: str
    raw: Any

class ProtoAssistant:
    def __init__(self, config: AIConfig):
        self.config = config
        
    def chat(self, messages: List[Dict[str, str]], json_mode: bool = False) -> AIResponse:
        response = litellm.completion(
            model=f"{self.config.provider}/{self.config.model}",
            messages=messages,
            api_key=self.config.api_key,
            base_url=self.config.base_url,
            response_format={"type": "json_object"} if json_mode else None
        )
        return AIResponse(
            content=response.choices[0].message.content,
            raw=response
        )

    def invent_part_prompt(self, description: str) -> str:
        return f"""
        You are an elite hardware engineer. Invent a virtual part based on this description: {description}
        Return a JSON object with:
        - name: A slugified name (e.g. brushless-motor-5in)
        - category: One of [electronics, mechanical, thermal, fluid]
        - description: A brief technical summary
        - parametric_code: Valid Python/CadQuery code to generate the 3D model.
        - physics_params: A JSON object string containing Modelica parameters.
        - datasheet_summary: A markdown stub of a datasheet (links, specs, pinouts).
        """
