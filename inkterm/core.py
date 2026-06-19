from .utils import transform_formats

class InkTerm:
    def __init__(self):
        self.reset_color = True
        self.default_text_color = ""
        self.default_prefix = ""
        self.prefix = {}
        
        self.reset_ansi = ""

    def setup(self, 
        reset_color: bool = None, 
        default_text_color: str | tuple = None,
        default_prefix: str = None,
        prefix: dict = None
    ):
        if reset_color is not None: self.reset_color = reset_color
        if default_text_color is not None: self.default_text_color = transform_formats(default_text_color)
        if prefix is not None: self.prefix = prefix
        if default_prefix is not None: self.default_prefix = default_prefix

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
            
        if self.default_prefix: 
            return self.prefix[self.default_prefix]
        
        raise ValueError(f"The prefix '{prefix}' does not exist.")

    def label(self, 
        text: str, 
        color: str | tuple[int, int, int] = None,
        background: str | tuple[int, int, int] = None,
    ):
        convert_color = transform_formats(color)
        convert_bg = transform_formats(background)

        return convert_color + convert_bg + text

_instance = InkTerm()

write = _instance.write
label = _instance.label