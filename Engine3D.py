from gl import Renderer, V3, _color
from obj import Texture
from shaders import *

import random

width = 960
height = 540

rend = Renderer(width, height)

rend.directional_light = V3(0,-1,-1)

rend.active_texture = Texture('models/model.bmp')
rend.normal_map = Texture('models/model_normal.bmp')

rend.background = Texture('models/wac.bmp')

rend.glClearBackground()

rend.active_shader = lava
rend.glLoadModel("models/papitas.obj",
                 translate = V3(-0.5, -1.7, -10),
                 scale = V3(4,4,4), rotate=V3(0,0,0))
rend.active_shader = tooned
rend.glLoadModel("models/hat.obj",
                 translate = V3(0.3, 0.1, -9),
                 scale = V3(5,5,5), rotate=V3(0,0,0))


rend.active_shader = ranrgb
rend.glLoadModel("models/cup.obj",
                 translate = V3(2.5, -1.7, -10),
                 scale = V3(3,8,3), rotate=V3(0,0,0))

rend.active_shader = tumbro
rend.glLoadModel("models/madara.obj",
                 translate = V3(1, -4, -10),
                 scale = V3(1,1,1), rotate=V3(0,0,0))
rend.active_shader = tuolf
rend.glLoadModel("models/burger.obj",
                 translate = V3(3.8, -3, -10),
                 scale = V3(5,5,5), rotate=V3(0,0,0))

rend.glFinish("output2.bmp")
