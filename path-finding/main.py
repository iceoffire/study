import pygame
from pygame import Surface
from pygame.font import Font
from pygame.locals import *
import pygame.gfxdraw
from path import Coordinate, Direction, Connection

def get_config():
    screen_size = (900, 500)
    screen_bord = (50, 50)
    max_x = 10
    max_y = 4
    city_a = Coordinate(get_related_pos(0, 1, screen_size, screen_bord, max_x, max_y), "City A")
    city_b = Coordinate(get_related_pos(1, 3, screen_size, screen_bord, max_x, max_y), "City B")
    city_c = Coordinate(get_related_pos(2, 2, screen_size, screen_bord, max_x, max_y), "City C")
    city_d = Coordinate(get_related_pos(3, 0, screen_size, screen_bord, max_x, max_y), "City D")
    city_e = Coordinate(get_related_pos(3, 4, screen_size, screen_bord, max_x, max_y), "City E")
    city_f = Coordinate(get_related_pos(4, 3, screen_size, screen_bord, max_x, max_y), "City F")
    city_g = Coordinate(get_related_pos(10,2, screen_size, screen_bord, max_x, max_y), "City G")

    coordinates = [
        city_a,
        city_b,
        city_c,
        city_d,
        city_e,
        city_f,
        city_g
    ]

    connections = [
        Connection(city_a, city_b, Direction.BOTH),
        Connection(city_b, city_c, Direction.BOTH),
        Connection(city_c, city_d, Direction.BOTH),
        Connection(city_c, city_e, Direction.BOTH),
        Connection(city_d, city_f, Direction.BOTH),
        Connection(city_e, city_f, Direction.BOTH),
        Connection(city_f, city_g, Direction.BOTH)
    ]

    

    return {
        'screen_size': screen_size,
        'screen': pygame.display.set_mode(screen_size),
        'coordinates': coordinates,
        'connections': connections,
        'coordinate_color': Color(151, 176, 104),
        'connection_color': Color(23, 189, 100),
        'is_running': True,
        'font': pygame.font.SysFont(pygame.font.get_fonts()[0], 18)
    }


def get_related_pos(x, y, screen_size, screen_bord, max_x, max_y):
    return (screen_bord[0]+((screen_size[0]-(2*screen_bord[0]))*(x/max_x)), screen_bord[1]+((screen_size[1]-(2*screen_bord[1]))*(y/max_y)))

def draw(screen: Surface, coordinates: list[Coordinate], connections: list[Connection], coordinate_color: Color, connection_color: Color, font: Font, **kwargs):
    screen.fill((0,0,0))

    for connection in connections:
        # draw lines
        pygame.draw.line(screen, connection_color, (connection.coord_a.x, connection.coord_a.y), (connection.coord_b.x, connection.coord_b.y))

        # draw distances in the middle
        text = "{} to {} {:.2f}m".format(connection.coord_a.city, connection.coord_b.city, connection.distance)
        font_created_surface = font.render(text, True, connection_color, (0,0,0))
        screen.blit(font_created_surface, (connection.coord_a.x + ((connection.coord_b.x-connection.coord_a.x)/2)-len(text)*2, connection.coord_a.y + ((connection.coord_b.y-connection.coord_a.y)/2)-18))
        # todo: draw arrow directions based on their Diretion

    for coordinate in coordinates:
        # draw coordinates points
        pygame.gfxdraw.filled_circle(screen, int(coordinate.x), int(coordinate.y), 4, coordinate_color)
        pygame.gfxdraw.aacircle(screen, int(coordinate.x), int(coordinate.y), 4, coordinate_color)

        # draw city names
        font_created_surface = font.render(coordinate.city, True, coordinate_color, (0,0,0))
        screen.blit(font_created_surface, (coordinate.x-len(coordinate.city)*2.2, coordinate.y-30))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

def update(config):
    for e in pygame.event.get():
        if e.type == QUIT or (e.type==KEYDOWN and e.key==K_ESCAPE):
            config['is_running'] = False
    return config

def main():
    pygame.init()
    pygame.font.init()
    configs = get_config()
    while configs['is_running']:
        configs = update(configs)
        draw(**configs)


if __name__=='__main__':
    main()