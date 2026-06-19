def transform_formats(format_to_ansi: str | tuple[int, int, int] | None, bg: bool = False) -> str:
    if not format_to_ansi:
        return ""
    
    ansi_type = '48' if bg else '38'

    if isinstance(format_to_ansi, str):
        hex_str = format_to_ansi.lower().strip().lstrip('#')

        if len(hex_str) > 6:
            raise ValueError(f"The format '{format_to_ansi}' is invalid.")

        try:
            r = int(hex_str[0:2], 16)
            g = int(hex_str[2:4], 16)
            b = int(hex_str[4:6], 16)
        except ValueError:
            raise ValueError(f"This string '{format_to_ansi}' does not contain invalid hexadecimal characters.")
            
        return f"\x1b[{ansi_type};2;{r};{g};{b}m"
    
    if isinstance(format_to_ansi, tuple):
        if len(format_to_ansi) != 3:
            raise ValueError('The RGB color tuple must have exactly 3 elements: (R, G, B)')
        
        r, g, b = format_to_ansi
        
        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            raise ValueError('The color values must be between 0 and 255.')
        return f"\x1b[{ansi_type};2;{r};{g};{b}m"
    
    raise TypeError(f'The color type is not allowed: {type(format_to_ansi)}')