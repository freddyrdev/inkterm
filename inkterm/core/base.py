from ..utils.transformer import transform_formats

class InkTerm:
    def __init__(self):
        self.reset_color = True
        self.default_text_color = ""
        self.default_prefix = ""
        self.prefix = {}
        
        self.reset_ansi = "\033[0m"

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
        styles: list = None,
        payload: bool = False,
    ) -> str | None:
        styles_list = styles or []

        all_styles = self._use_formats(styles_list)
        convert_color = transform_formats(color)
        convert_bg = transform_formats(background, True)

        prefix_found = self._get_prefix(prefix)

        output = f"{prefix_found}{convert_color}{convert_bg}{all_styles}{self.default_text_color}{self.reset_ansi}"

        if payload: return output
        print(output)

    def _get_prefix(self, prefix: str) -> str:
        if prefix is not None:
            return self.prefix.get(prefix, "")
        
        if self.default_prefix:
            return self.prefix.get(self.default_prefix, "")

    def label(self, 
        text: str, 
        styles: list = [],
        color: str | tuple[int, int, int] = None,
        background: str | tuple[int, int, int] = None,
    ):
        styles_list = styles or []

        all_styles = self._use_formats(styles_list)
        convert_color = transform_formats(color)
        convert_bg = transform_formats(background, True)

        return f"{convert_color}{convert_bg}{all_styles}{text}\033[0m"

    def _use_formats(self, styles: list) -> str:
        return "".join(style.value for style in styles)

_instance = InkTerm()

write = _instance.write
label = _instance.label