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
# Recommended: Install via Poetry
git clone https://github.com/Okediya/ProtoForge.git
cd ProtoForge
poetry install
```

## Quick Start

1. **Initialize a Project**:
   ```bash
   proto new quadcopter-project
   cd quadcopter-project
   ```

2. **Configure Your AI**:
   ```bash
   # Supports Groq, OpenAI, Ollama, etc.
   proto config model --provider groq --model llama-3.3-70b-versatile --key YOUR_API_KEY
   ```

3. **Invent Parts**:
   ```bash
   proto add mechanical "sturdy-carbon-frame" --ai-invent
   ```

4. **Visualize & Simulate**:
   ```bash
   proto view        # See it in 3D (STL export)
   proto simulate    # Run physics and firmware tests
   ```

5. **Export to Real World**:
   ```bash
   proto export      # Get your shopping list and assembly guide
   ```

## License

Distributed under the MIT License. See `LICENSE` for more information.
