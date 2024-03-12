from rich.console import Console
from rich.table import Table

console = Console()

table = Table(show_header=True, header_style="bold magenta")
table.add_column("Date")
table.add_row("12.03.2024")
console.print(table)

