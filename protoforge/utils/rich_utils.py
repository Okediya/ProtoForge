from rich.console import Console
from rich.theme import Theme
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn

# Custom ProtoForge Theme
PROTO_THEME = Theme({
    "info": "cyan",
    "warning": "yellow",
    "error": "bold red",
    "success": "bold green",
    "highlight": "bold magenta",
})

console = Console(theme=PROTO_THEME)

def print_banner():
    console.print(Panel.fit(
        "[bold cyan]PROTO[/bold cyan][bold white]FORGE[/bold white]",
        subtitle="[italic]AI-Powered Virtual Hardware Prototyping[/italic]",
        border_style="cyan"
    ))

def get_progress():
    return Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
    )

def draw_3d_preview_text(part_name: str):
    """Simple ASCII art representation for 3D preview."""
    art = f"""
    [bold green]3D PREVIEW: {part_name}[/bold green]
       ___________________
      /|                 /|
     / |                / |
    *--|---------------*  |
    |  |               |  |
    |  |               |  |
    |  *---------------|--*
    | /                | /
    |/_________________|/
    """
    console.print(Panel(art, border_style="green"))
