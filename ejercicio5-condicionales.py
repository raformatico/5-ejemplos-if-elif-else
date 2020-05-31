# SEÑALES ENVIADAS POR EL CHAT
# > LAMADA DEL CHAT A LA CREACIÓN DEL CAMINO
def on_chat_crea_camino():
    agent.teleport(world(44, 4, 7), SOUTH)
    crea_camino()
player.on_chat("crea_camino", on_chat_crea_camino)
# > LAMADA DEL CHAT A LA CREACIÓN DEL CAMINO
def on_chat_recorre_camino():
    agent.teleport(world(44, 4, 7), SOUTH)
    recorre_camino()
player.on_chat("recorre_camino", on_chat_recorre_camino)


# FUNCIÓN PARA COLOCAR ORO
def poner_oro(num: number):
    for index5 in range(num):
        agent.destroy(DOWN)
        agent.set_item(GOLD_BLOCK, 1, 1)
        agent.place(DOWN)
        agent.move(FORWARD, 1)
        agent.collect_all()
agent.teleport(world(14, 4, 7), SOUTH)

# FUNCIÓN PARA CREAR EL CAMINO
def crea_camino():
    poner_oro(10)
    agent.turn(LEFT_TURN)
    poner_oro(3)
    agent.turn(RIGHT_TURN)
    poner_oro(10)
    agent.teleport(world(44, 4, 17), SOUTH)
    agent.turn(RIGHT_TURN)
    poner_oro(3)
    agent.turn(LEFT_TURN)
    poner_oro(10)

# FUNCIÓN PARA RECORRER EL CAMINO CORRECTO
# FUNCIÓN QUE IMPLEMENTA LA LÓGICA DE IF/ELIF/ELSE
def recorre_camino():
    agent.move(FORWARD, 10)
    if agent.inspect(AgentInspection.BLOCK, DOWN) == IRON_BLOCK:
        agent.turn_left()
        agent.move(FORWARD, 3)
        agent.turn_right()
        agent.move(FORWARD, 9)
        agent.move(UP, 5)
    elif agent.inspect(AgentInspection.BLOCK, DOWN) == REDSTONE_BLOCK:
        agent.turn_right()
        agent.move(FORWARD, 3)
        agent.turn_left()
        agent.move(FORWARD, 9)
        agent.move(UP, 5)
    else:
        agent.teleport_to_player()

