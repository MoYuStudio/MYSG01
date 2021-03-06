
import pygame
from pygame.locals import *

window =\
{
    # window
    'size'         : [1280,720],
    'set_size'     : [320,180],
    'size_level'   : 0.5,
    'fps'          : 60,
    'title'        : 'Mineland',
    'surface_level': 1,
    'tilemap_level': 1,

    # move
    'move':[8,20],
    'move_speed':2,
    'move_switch':
    {
        'up'   : False,
        'down' : False,
        'left' : False,
        'right': False,
    },
    'zoom_switch':
    {
        'in' : False,
        'out': False,
    },

    # window ppt
    'page_switch' :
    {
        'switch':False,
        'menu_main_page' : True,
        'game_main_page' : False,
    }
    
}

tilemap =\
{
    # tilemap
    'tilemap': [],
    'boarder': 64,
    'seed'   : 0,
    'octaves': 2,
    'freq'   : 12,

    # tile
    'tile_size'       : 16,
    'pretile_type'    : 0,
    'tile_type'       : 0,
    'build'           : False,
    'reward'          : False,
    'tile_choose'     : False,
    'tile_choose_info': [0,0,0],
    'tile_choose_info': [0,0,0,0,0,0],
    
    # tile time
    'time_speed': 1000,
}

assets = {}

gui =\
{
    'button_preclick': False,
    'button_num'     : 0,
}

transition =\
{
    'fade_black' : False,
}

screen = pygame.display.set_mode(window['size'],pygame.RESIZABLE)

player_rect = pygame.Rect((window['set_size'][0]/2-8,window['set_size'][1]/2-8,16,16),width=0)
hitable_map = []