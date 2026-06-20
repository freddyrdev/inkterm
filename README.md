# Inkterm

A lightweight, fluent, and modern tool for decorating terminal text. Essential for building clean Command Line Interfaces (CLI) and console applications without cluttering your code with raw ANSI escape sequences.

## Installation

Install `inkterm` via pip:

```bash
pip install inkterm
```

### Key Features
1. **Flexible Color Formats:** Full support for HEX strings, RGB tuples, and built-in ANSI constants.
2. **Global Configuration:** Clean, centralized setup to define your project's default visual hierarchy once and reuse it everywhere.
3. **Smart Prefixes:** Manage consistent log levels (info, error, success) seamlessly.

### Quick Start
Instead of using Python's native `print()` and manually concatenating colors, use the `write()` function for instant, clean styling:
```python
from inkterm import write

write("Hello world!", color="#7c7c7c")
```

### The `write()` Function Reference
| Argument | Default | Type | Description |
| :--- | :--- | :--- | :--- |
| text | Required | str | The message to be printed. |
| color | None | str / tuple / Color | Foreground color (HEX string, RGB tuple, or Color Enum). |
| background | None | str / tuple / Color | Background color (HEX string, RGB tuple, or Color Enum). |
| styles | None | list | A list of text formats (e.g., `[Style.BOLD]`). |
| prefix | None | str | Name of a predefined prefix from your global config. |
| payload | False | bool | If True, returns the formatted ANSI string instead of printing it. |

### Centralized Global Settings
To maximize code readability, configure your visual styles at your application's entry point (e.g., `main.py`).

#### The `config()` Reference

| Argument | Default | Type | Description |
| :--- | :--- | :--- | :--- |
| reset_color | True` | bool | Automatically appends an ANSI reset sequence at the end of every line. |
| default_text_color | None | str / tuple / Color | Fallback foreground color for all standard text. |
| default_prefix | None | str | The prefix name used by default when `write()` specifies none. |
| prefix | None | dict | A dictionary mapping names to pre-styled components via `label()`. |

### Advanced Configuration Example
```python
# main.py

from inkterm import config, write, label, Style, Color

config(
    # Set default text color using an Enum constant
    default_text_color=Color.WHITE,

    # Build and register custom prefixes
    prefix={
        "info": label("[INFO]", color="#57bf4b", styles=[Style.BOLD]),
        "error": label("[ERROR]", color=Color.RED, styles=[Style.BOLD, Style.UNDERLINE]),
    },

    # Automatically use the 'info' prefix if none is passed to write()
    default_prefix="info"
)

# Standard print using the default "info" prefix
write("System is running smoothly.")  # Output: [INFO] System is running smoothly.

# Overriding the prefix for specific logs
write("Database connection failed!", prefix="error")  # Output: [ERROR] Database connection failed!
```

### Built-in Constants
For fast, standard terminal coloring, you can import and use the `Color` and `Style` Enums directly:

#### Available Styles (`Style.*`)
* `Style.BOLD`
* `Style.DIM`
* `Style.ITALIC`
* `Style.UNDERLINE`
* `Style.BLINK`
* `Style.REVERSE`
* `Style.STRIKETHROUGH`

### Available Colors (`Colors.*`)
* `Color.BLACK`
* `Color.RED`
* `Color.GREEN`
* `Color.YELLOW`
* `Color.BLUE`
* `Color.MAGENTA`
* `Color.CYAN`
* `Color.WHITE`

---
For fast, standard terminal coloring, you can import and use the Color and Style Enums directly: