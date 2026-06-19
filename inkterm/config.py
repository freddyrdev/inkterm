from .core import _instance

def config(
    reset_color: bool = True,
    default_text_color: str | tuple = None,
    prefix: dict = None
):
    _instance.setup(
        reset_color=reset_color,
        default_text_color=default_text_color,
        prefix=prefix or {}
    )