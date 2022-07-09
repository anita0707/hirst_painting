# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg',10)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print (rgb_colors)
from turtle import Screen
import turtle as T
import random

color_list = [(240, 228, 204), (216, 160, 87), (242, 222, 234), (228, 243, 233), (224, 231, 243), (192, 167, 26), (230, 207, 105), (57, 114, 161), (179, 69, 43), (203, 156, 179)]


def draw_colorline():
    for _ in range(10):

        tim.dot(20, random.choice(color_list))
        tim.fd(50)


tim = T.Turtle()
T.colormode(255)
tim.up()
tim.hideturtle()
y = -250
tim.goto(-250, y)
for _ in range(10):
    draw_colorline()
    y += 50
    tim.goto(-250, y)
screen = Screen()
screen.exitonclick()


