from pathlib import Path
from protoforge.project import ProtoProject
from rich.table import Table
from rich.console import Console

def generate_bom_table(project: ProtoProject) -> Table:
    table = Table(title=f"Bill of Materials: {project.name}")
    table.add_column("Category", style="cyan")
    table.add_column("Part Name", style="magenta")
    table.add_column("Quantity", justify="right")
    
    for ref in project.parts:
        table.add_row(ref.category, ref.name, str(ref.quantity))
    
    return table

def export_build_instructions(project: ProtoProject, format: str = "markdown") -> str:
    if format == "markdown":
        lines = [f"# Build Instructions for {project.name}", ""]
        lines.append("## Bill of Materials")
        for ref in project.parts:
            lines.append(f"- {ref.name} ({ref.category}) x {ref.quantity}")
        
        lines.append("\n## Assembly Steps")
        lines.append("1. Gather all parts listed above.")
        lines.append("2. Calibrate simulators following `proto simulate` results.")
        lines.append("3. Flash firmware using Renode scripts generated in `.protoforge/sim/`.")
        
        return "\n".join(lines)
    
    return "Unsupported format"

def save_export(content: str, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        f.write(content)
