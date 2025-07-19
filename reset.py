from main import lista_cactus
def reset_game():
    global punti, collisione_rilevata, incremento_vel_terreno, lista_cactus
    global vel_terreno, indice_livello_attuale, random_inizio, random_fine
    global posizione_sprite_y, velocità_salto, sta_salando

    punti = 0
    collisione_rilevata = False
    incremento_vel_terreno = 6
    vel_terreno = 0
    indice_livello_attuale = 0
    random_inizio = 100
    random_fine = 250
    lista_cactus.clear()
    posizione_sprite_y = 422
    velocità_salto = 0
    sta_salando = False