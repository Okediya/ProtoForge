from typing import List, Dict
from pydantic import BaseModel

class TutorialStep(BaseModel):
    title: str
    explanation: str
    task: str
    quiz_question: str | None = None
    quiz_answer: str | None = None

class Tutorial(BaseModel):
    id: str
    title: str
    topic: str
    steps: List[TutorialStep]

TUTORIALS = [
    Tutorial(
        id="quadcopter-101",
        title="Building Your First Quadcopter",
        topic="drones",
        steps=[
            TutorialStep(
                title="Introduction to Frame Mechanics",
                explanation="The frame is the skeleton of your drone. It must be rigid yet lightweight.",
                task="Add a frame part to your project: `proto add part mechanical carbon-frame`",
                quiz_question="What is the most common material for racing drone frames?",
                quiz_answer="Carbon fiber"
            ),
            TutorialStep(
                title="Propulsion and Motors",
                explanation="Motors provide the thrust. KV ratings determine the RPM per volt.",
                task="Invent a motor: `proto invent 'brushless motor 2306 2400KV'`",
                quiz_question="What does KV stand for in motor specs?",
                quiz_answer="Velocity Constant"
            )
        ]
    )
]

def get_tutorial(topic: str) -> Tutorial | None:
    for t in TUTORIALS:
        if t.topic == topic or t.id == topic:
            return t
    return None
