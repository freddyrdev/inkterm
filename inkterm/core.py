from .utils import transform_formats

class InkTerm:
    def __init__(self):
        self.reset_color = True
        self.default_text_color = ""
        self.prefix = {}
        
        self.reset_ansi = ""
        self.prefix_found = ""

    def setup(self, 
        reset_color: bool = None, 
        default_text_color: str | tuple = None,
        prefix: dict = None
    ):
        if reset_color is not None: self.reset_color = reset_color
        if default_text_color is not None: self.default_text_color = transform_formats(default_text_color)
        if prefix is not None: self.prefix = prefix

        self.reset_ansi = "\033[0m" if self.reset_color else ""
    
    def write(
        self,
        text: str, 
        prefix: str = None,
        color: str | tuple[int, int, int] = None, 
        background: str | tuple[int, int, int] = None,
        payload: bool = False,
    ) -> str | None:
        prefix_found = self._get_prefix(prefix)
        convert_color = transform_formats(color)
        convert_bg = transform_formats(background, True)

        output = prefix_found + convert_color + convert_bg + text + self.reset_ansi

        if payload: return output
        print(output)

    def _get_prefix(self, prefix: str) -> str:
        for key, value in self.prefix.items():
            if key == prefix:
                return value
        return ""

_instance = InkTerm()

write = _instance.write