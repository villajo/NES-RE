import json

areaArray = []


class AreaClass:
    def __init__(self, u_boundary, d_boundary, l_boundary, r_boundary):
        self.u_boundary = u_boundary
        self.d_boundary = d_boundary
        self.l_boundary = l_boundary
        self.r_boundary = r_boundary


def load_area_data(room, area):
    objects = []
    file_data = open("data/mansion.json", "r")
    json_data = file_data.read()
    game_data = json.loads(json_data)
    up = eval(game_data[str(room)]["BOUNDS"]["UP"])
    down = eval(game_data[str(room)]["BOUNDS"]["DOWN"])
    left = eval(game_data[str(room)]["BOUNDS"]["LEFT"])
    right = eval(game_data[str(room)]["BOUNDS"]["RIGHT"])
    img = game_data[str(room)]["BACKGROUND"]

    return up, down, left, right, img
