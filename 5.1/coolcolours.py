def colour(r, g, b):
    if r <= 24 and g <= 255 and b <= 24:
        return ("green")
    if r <= 24 and g <= 24 and b <= 255:
        return("blue")
    if r <= 255 and g <= 24 and b <= 24:
        return("red")