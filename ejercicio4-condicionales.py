# SEÑALES ENVIADAS POR EL CHAT
def on_chat_inicio():
    agent.teleport(world(14, 4, 7), SOUTH)
    colocarBloques()
player.on_chat("inicio", on_chat_inicio)

def on_chat_recoger(num1):
    agent.teleport(world(14, 4, 7), SOUTH)
    recogerBloques(num1)
player.on_chat("recoger", on_chat_recoger)

# FUNCIÓN PARA COLOCAR BLOQUES
def colocarBloques():
    agent.collect_all()
    for index in range(2):
        agent.set_item(GRASS, 1, 1)
        agent.destroy(DOWN)
        agent.place(DOWN)
        agent.collect_all()
        agent.move(FORWARD, 1)
    agent.set_item(REDSTONE_ORE, 1, 1)
    agent.destroy(DOWN)
    agent.place(DOWN)
    agent.collect_all()
    agent.move(FORWARD, 1)
    agent.set_item(GRASS, 1, 1)
    agent.destroy(DOWN)
    agent.place(DOWN)
    agent.collect_all()
    agent.move(FORWARD, 1)
    for index2 in range(2):
        agent.set_item(GOLD_BLOCK, 1, 1)
        agent.destroy(DOWN)
        agent.place(DOWN)
        agent.collect_all()
        agent.move(FORWARD, 1)
    for index3 in range(2):
        agent.set_item(GRASS, 1, 1)
        agent.destroy(DOWN)
        agent.place(DOWN)
        agent.collect_all()
        agent.move(FORWARD, 1)

# FUNCIÓN QUE IMPLEMENTA LA LÓGICA DE IF/ELIF/ELSE
def recogerBloques(núm: number):
    for index4 in range(núm):
        agent.collect_all()
        agent.move(FORWARD, 1)
        if agent.inspect(AgentInspection.BLOCK, DOWN) == REDSTONE_ORE:
            agent.set_item(GLASS, 1, 1)
            agent.destroy(DOWN)
            agent.place(DOWN)
        elif agent.inspect(AgentInspection.BLOCK, DOWN) == GOLD_BLOCK:
            agent.set_item(GRASS, 1, 1)
            agent.destroy(DOWN)
            agent.place(DOWN)
        else:
            player.say("Otras cosistas de poco interés...")