def render_all(con, entities, root_console, screen_width, screen_height):
	#Draw all entitites in th list
	for entity in entitites:
		draw_entitiy(con, entity)

	root_console.blit(com, 0, 0, screen_width, screen_height, 0, 0)

def clear_all(con, entitites):
	for entity in entitites:
		clear_entity(con, entity)

def draw_entitiy(con, entity):
	con.draw_char(entity.x, entity.y, entity.char, entity.color, bg=None)

def clear_entity(con, entity):
	#erase char that represents this object
	con.draw_char(entity.x, entity.y, ' ', entity.color, bg=None)