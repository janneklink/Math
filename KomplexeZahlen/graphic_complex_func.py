from PIL import Image
from math import cos, sin, pi


def complex_func(x: float) -> complex:
    real = 2*(1+cos(x))* cos(x)
    imag = 2*(1+cos(x)) * sin(x)
    return complex(real, imag)


def render_function(c1: complex, c2: complex, width: int, height: int, delta_x: float, x_min: float, x_max: float,
                    name: str):
    size = (width, height)
    img = Image.new('HSV', size,color=int(0xff00ff))
    x = x_min
    x_relative = width / (c1.real - c2.real)
    y_relative = height / (c1.imag - c2.imag)
    while x < x_max:
        f_of_x = -1*complex_func(x)
        xy = (int(x_relative * (f_of_x.real - c1.real)), int(y_relative * (f_of_x.imag - c1.imag)))
        img.putpixel(xy, (255, 255, 255))
        x += delta_x
    img.putpixel((500-125//2,500),(255, 255, 255))
    img.convert('RGB').save(name, quality=95)


render_function(-5 - 5j, 5 + 5j, 1000, 1000, 0.001, 0, 2 * pi, "B.jpg")

