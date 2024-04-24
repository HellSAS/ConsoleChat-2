import rich
from rich.table import Table
from rich.console import Console

console = Console()

table = Table(title="Available Colors")
        
for i in range(0,6):
    table.add_column("Color")
    table.add_column("Color Code")



row1, row2, row3, row4, row5, row6 = [], [], [], [], [], []

for color in list(rich.color.ANSI_COLOR_NAMES)[:38]:
    row1.append((f"[{color}]{color}[/]", str(rich.color.ANSI_COLOR_NAMES[color])))
for color in list(rich.color.ANSI_COLOR_NAMES)[38:77]:
    row2.append((f"[{color}]{color}[/]", str(rich.color.ANSI_COLOR_NAMES[color])))
for color in list(rich.color.ANSI_COLOR_NAMES)[77:115]:
    row3.append((f"[{color}]{color}[/]", str(rich.color.ANSI_COLOR_NAMES[color])))
for color in list(rich.color.ANSI_COLOR_NAMES)[115:154]:
    row4.append((f"[{color}]{color}[/]", str(rich.color.ANSI_COLOR_NAMES[color])))
for color in list(rich.color.ANSI_COLOR_NAMES)[154:193]:
    row5.append((f"[{color}]{color}[/]", str(rich.color.ANSI_COLOR_NAMES[color])))
for color in list(rich.color.ANSI_COLOR_NAMES)[193:232]:
    row6.append((f"[{color}]{color}[/]", str(rich.color.ANSI_COLOR_NAMES[color])))

for i in range(0,38):
    table.add_row(*row1[i], *row2[i], *row3[i], *row4[i], *row5[i], *row6[i])


console.print(table)