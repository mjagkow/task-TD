def middle(a, b, c):
    ab = 0.5 - (a - b > 0)
    bc = 0.5 - (b - c > 0)
    ca = 0.5 - (c - a > 0)

    if ab * bc > 0:
        return b
    if ca * ab > 0:
        return a
    return c
