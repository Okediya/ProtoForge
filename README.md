# ProtoForge
[![PyPI version](https://img.shields.io/pypi/v/protoforge.svg)](https://pypi.org/project/protoforge/)

**ProtoForge** is an elite CLI tool for learning and building virtual prototypes of ANY hardware (PC, car, airplane, drone, robot, IoT device, rocket, etc.). It integrates physics simulators, firmware emulation, and AI agents to provide an end-to-end prototyping experience.

## Key Features

- **AI Part Inventing**: Describe a part, and AI generates the parametric model (CadQuery) and physics parameters (Modelica).
- **Virtual Assembly**: Assemble complex systems in a virtual environment with ease.
- **Multi-Simulator Integration**: Connect to **Gazebo** for physics, **OpenModelica** for electronics/thermal, and **Renode** for firmware emulation.
- **Dynamic Plugin System**: "Bring your own simulator" with a plug-and-play architecture.
- **Interactive Learning**: Guided AI tutorials to help you master hardware engineering.
- **Export Ready**: Generates high-fidelity BOMs and step-by-step build instructions.

## Installation

```bash
pip install protoforge
```

Or install via Poetry (for development):
```bash
git clone https://github.com/Okediya/ProtoForge.git
cd ProtoForge
poetry install
```

## Quick Start (5-Minute Guide)

Follow these steps to build your first virtual prototype from scratch.

### 1. Configure Your AI
ProtoForge needs an AI "brain" to invent parts. We recommend **Groq** for speed or **Ollama** for local use.
```bash
# Example: Using Groq
proto config model --provider groq --model llama-3.3-70b-versatile --key YOUR_API_KEY
```

### 2. Initialize a Project
Create a fresh sandbox for your idea:
```bash
proto new quadcopter-project
cd quadcopter-project
```

### 3. Invent & Add Parts
Describe any part you need, and the AI will "invent" it and add it to your project library.
```bash
proto add mechanical "ultralight-carbon-fiber-frame" --ai-invent
```

### 4. Visualize & Simulate
See your design in 3D and run physics tests to ensure everything works as intended.
```bash
proto view        # Exports assembly to exports/assembly.stl
proto simulate    # Runs physics and firmware checks
```

### 5. Export for Reality
Get your Bill of Materials (BOM) and assembly guide for real-world manufacturing:
```bash
proto export      # Check the exports/ folder!
```

## License

Distributed under the MIT License. See `LICENSE` for more information.
