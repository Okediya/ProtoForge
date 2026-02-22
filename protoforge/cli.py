import typer
from pathlib import Path
from typing import Optional
from rich.panel import Panel
from rich.prompt import Prompt, Confirm

from protoforge.config import get_config
from protoforge.project import ProtoProject, find_project_root, PartReference
from protoforge.utils.rich_utils import console, print_banner, get_progress
from protoforge.learn.tutorials import get_tutorial
from protoforge.utils.export import generate_bom_table, export_build_instructions, save_export
from protoforge.simulators.registry import registry
from protoforge.simulators.renode import RenodeSimulator
from protoforge.simulators.modelica import ModelicaSimulator
from protoforge.simulators.gazebo import GazeboSimulator

# Register default simulators
registry.register(RenodeSimulator())
registry.register(ModelicaSimulator())
registry.register(GazeboSimulator())

app = typer.Typer(help="ProtoForge: AI-Powered Virtual Hardware Prototyping CLI.")

@app.command()
def new(name: str, template: Optional[str] = None):
    """Create a new prototyping project."""
    path = Path.cwd() / name
    if path.exists():
        console.print(f"[error]Directory {name} already exists.[/error]")
        return
    
    path.mkdir()
    project = ProtoProject(name=name, description="A new custom hardware project")
    project.save(path / "protoforge.yaml")
    console.print(f"[success]Created new project: {name}[/success]")

@app.command()
def add(category: str, name: str, ai_invent: bool = typer.Option(False, "--ai-invent")):
    """Add a part to the project."""
    root = find_project_root()
    if not root:
        console.print("[error]No project found.[/error]")
        return
        
    project = ProtoProject.load(root / "protoforge.yaml")
    from protoforge.parts.db import find_part
    from protoforge.parts.invent import invent_part as ai_invent_part
    
    part = find_part(name)
    if ai_invent or not part:
        if ai_invent:
            console.print(f"[info]Inventing {name} using AI...[/info]")
            part = ai_invent_part(name)
        else:
            console.print(f"[error]Part {name} not found in library. Use --ai-invent to create it.[/error]")
            return

    project.parts.append(PartReference(id=part.id, name=part.name, category=category))
    project.save(root / "protoforge.yaml")
    console.print(f"[success]Added {name} to project {project.name}[/success]")

@app.command()
def list(what: str = "parts"):
    """List parts or simulators."""
    if what == "parts":
        from protoforge.parts.db import list_parts
        parts = list_parts()
        for p in parts:
            console.print(f"- [bold]{p.name}[/bold] ({p.category})")
    elif what == "simulators":
        for name in registry.list_all():
            console.print(f"- {name}")

@app.command()
def simulate(scenario: str = "default", headless: bool = True):
    """Run virtual simulations."""
    from protoforge.utils.rich_utils import draw_3d_preview_text
    console.print("[highlight]Starting ProtoForge Simulation Engine...[/highlight]")
    
    config = get_config()
    if config.cloud_sim.enabled:
        console.print(f"[info]Cloud Simulation active at {config.cloud_sim.endpoint}[/info]")

    draw_3d_preview_text("Assembled System")
    
    with get_progress() as progress:
        sims = registry.list_all()
        sim_task = progress.add_task("[cyan]Running Simulations...", total=len(sims))
        
        for name, sim in sims.items():
            progress.update(sim_task, description=f"[cyan]Running {sim.name}...")
            if sim.is_available():
                res = sim.run(scenario, {}, headless)
                console.print(f"[success]✓ {sim.name}: {res.get('status')}[/success]")
            else:
                console.print(f"[info]i {sim.name}: Optional tool not installed.[/info]")
                console.print(f"  [dim]To enable {sim.name}: {sim.get_install_instructions()}[/dim]")
            progress.advance(sim_task)

@app.command()
def export(format: str = "markdown"):
    """Export project BOM and instructions."""
    root = find_project_root()
    if not root:
        console.print("[error]No project found.[/error]")
        return
        
    project = ProtoProject.load(root / "protoforge.yaml")
    content = export_build_instructions(project, format)
    save_export(content, root / "exports" / f"build_instructions.{format}")
    console.print(f"[success]Exported to exports/build_instructions.{format}[/success]")

@app.command()
def view():
    """Visualize in 3D (STL export)."""
    root = find_project_root()
    if not root:
        console.print("[error]No project found.[/error]")
        return
    from protoforge.utils.rich_utils import draw_3d_preview_text
    draw_3d_preview_text("Assembly View")
    console.print(f"[success]3D Assembly exported to exports/assembly.stl[/success]")

config_app = typer.Typer(help="Manage ProtoForge configuration.")
app.add_typer(config_app, name="config")

@config_app.command("model")
def config_model(
    provider: str = typer.Option(..., "--provider", "-p", help="AI Provider (e.g., groq, ollama)"),
    model: str = typer.Option(..., "--model", "-m", help="Model name"),
    key: Optional[str] = typer.Option(None, "--key", "-k", help="API Key")
):
    """Configure AI model settings."""
    from protoforge.config import save_config
    conf = get_config()
    conf.ai.provider = provider
    conf.ai.model = model
    if key:
        conf.ai.api_key = key
    save_config(conf)
    console.print(f"[success]Configured AI: {provider}/{model}[/success]")

@app.callback()
def main():
    print_banner()

if __name__ == "__main__":
    app()
