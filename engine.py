import tdl
from entity import Entity
from input_handlers import handle_keys
from render_functions import render_all, clear_all
from map_utils import make_map


def main():
    #sizes
    screen_width = 80
    screen_height = 50
    map_width = 80
    map_height = 45

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30
    
    # colors
    colors = {
        'dark_wall': (0, 0, 100),
        'darl_ground': (50, 50, 150)
    }
    
    #objects
    player = Entity(int(screen_width/2), int(screen_height/2), '@', (255, 255, 255))
    npc = Entity(int(screen_width/2 - 5), int(screen_height/2), '@', (255, 255, 0))
    entities = [player, npc]
    
    #consoles and game map
    tdl.set_font('arial10x10.png', greyscale=True, altLayout=True)
    root_console = tdl.init(screen_width, screen_height,
                            title="Ermak17")
    con = tdl.Console(screen_width, screen_height) # creating another console for drawing char on instd. of root

    game_map = tdl.map.Map(map_width, map_height) # creating game map obj
    make_map(game_map, max_rooms, room_min_size, room_max_size, map_width, map_height, player)


    while not tdl.event.is_window_closed():
        #draw and clear on console
        render_all(con, entities, game_map, root_console, screen_width, screen_height, colors)
        tdl.flush() # makes visible all the changes, update the screen
        clear_all(con, entities)

        for event in tdl.event.get():
            if event.type == 'KEYDOWN':
                user_input = event
                break
        else:
            user_input = None

        if not user_input:
            continue

        action = handle_keys(user_input)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move
            if game_map.walkable[player.x + dx, player.y + dy]:
                player.move(dx, dy)

        if exit:
            return True

        if fullscreen:
            tdl.set_fullscreen(not tdl.get_fullscreen())

if __name__ == "__main__":
    main()
