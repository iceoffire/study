import pygame
from pygame import Surface
from pygame.font import Font
from pygame.locals import *
import pygame.gfxdraw
from path import Vertice, Connection, AdjacencyList
from dijkstra import Dijkstra

def get_config():
    screen_size = (900, 500)
    screen_bord = (50, 50)
    max_x = 10
    max_y = 4
    city_a = Vertice(get_related_pos(0, 1, screen_size, screen_bord, max_x, max_y), "City A")
    city_b = Vertice(get_related_pos(1, 3, screen_size, screen_bord, max_x, max_y), "City B")
    city_c = Vertice(get_related_pos(2, 2, screen_size, screen_bord, max_x, max_y), "City C")
    city_d = Vertice(get_related_pos(3, 0, screen_size, screen_bord, max_x, max_y), "City D")
    city_e = Vertice(get_related_pos(3, 4, screen_size, screen_bord, max_x, max_y), "City E")
    city_f = Vertice(get_related_pos(4, 3, screen_size, screen_bord, max_x, max_y), "City F")
    city_g = Vertice(get_related_pos(10,2, screen_size, screen_bord, max_x, max_y), "City G")

    adjacencyList = AdjacencyList()
    adjacencyList.add_vertex(city_a)
    adjacencyList.add_vertex(city_b)
    adjacencyList.add_vertex(city_c)
    adjacencyList.add_vertex(city_d)
    adjacencyList.add_vertex(city_e)
    adjacencyList.add_vertex(city_f)
    adjacencyList.add_vertex(city_g)

    adjacencyList.connect(0, 1)
    adjacencyList.connect(1, 2)
    adjacencyList.connect(2, 3)
    adjacencyList.connect(2, 4)
    adjacencyList.connect(3, 5)
    adjacencyList.connect(4, 5)
    adjacencyList.connect(5, 6)

    dijkstra = Dijkstra()
    print(dijkstra.calculate(adjacencyList, 0, 6))

    return {
        'screen_size': screen_size,
        'screen': pygame.display.set_mode(screen_size),
        'adjacencyList': adjacencyList,
        'coordinate_color': Color(151, 176, 104),
        'connection_color': Color(23, 189, 100),
        'is_running': True,
        'font': pygame.font.SysFont(pygame.font.get_fonts()[0], 18)
    }


def get_related_pos(x, y, screen_size, screen_bord, max_x, max_y):
    return (screen_bord[0]+((screen_size[0]-(2*screen_bord[0]))*(x/max_x)), screen_bord[1]+((screen_size[1]-(2*screen_bord[1]))*(y/max_y)))

def draw(screen: Surface, adjacencyList: AdjacencyList, coordinate_color: Color, connection_color: Color, font: Font, **kwargs):
    screen.fill((0,0,0))
    
    for coordinate in adjacencyList.vertices:
        for key in coordinate.edges:
            connection = coordinate.edges[key]
            target = adjacencyList.vertices[key]
            # draw lines
            pygame.draw.line(screen, connection_color, (coordinate.x, coordinate.y), (target.x, target.y))

            # draw distances in the middle
            text = "{} to {} {:.2f}m".format(coordinate.city, target.city, connection.distance)
            font_created_surface = font.render(text, True, connection_color, (0,0,0))
            screen.blit(font_created_surface, (coordinate.x + ((target.x-coordinate.x)/2)-len(text)*2, coordinate.y + ((target.y-coordinate.y)/2)-18))
            # todo: draw arrow directions based on their Diretion

    #for coordinate in adjacencyList.vertices:
    #    for edge in coordinate.edges:
    #        # draw coordinates points
    #        pygame.gfxdraw.filled_circle(screen, int(coordinate.x), int(coordinate.y), 4, coordinate_color)
    #        pygame.gfxdraw.aacircle(screen, int(coordinate.x), int(coordinate.y), 4, coordinate_color)
#
    #        # draw city names
    #        font_created_surface = font.render(coordinate.city, True, coordinate_color, (0,0,0))
    #        screen.blit(font_created_surface, (coordinate.x-len(coordinate.city)*2.2, coordinate.y-30))

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