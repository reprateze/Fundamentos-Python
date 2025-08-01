from random import randint

lista_npcs = []

player = {
    "nome": "Renan",
    "level": 1,
    "exp": 0, 
    "exp_max": 15,
    "hp": 100,
    "hp_max": 100,
    "dano": 25,
}

def criar_npc(level):
    return {
        "nome": f"Monstro #{level}",
        "level": level,
        "dano": 5 * level,
        "hp": 100 * level,
        "hp_max": 100 * level, 
        "exp": 7 * level,
    }

def gerar_npcs(n_npcs): 
    for x in range(n_npcs):
        npc = criar_npc(x + 1)
        lista_npcs.append(npc)

def exibir_npc(npc):
    print(f"Nome: {npc['nome']} // Level: {npc['level']} // Dano: {npc['dano']} // HP: {npc['hp']} // EXP: {npc['exp']}")

def exibir_todos_npcs():
    for npc in lista_npcs:
        exibir_npc(npc)

def exibir_player():
    print(f"Nome: {player['nome']} // Level: {player['level']} // Dano: {player['dano']} // HP: {player['hp']} / {player['hp_max']} // EXP: {player['exp']} / {player['exp_max']}")

def reset_player():
    player['hp'] = player['hp_max']

def reset_npc(npc):
    npc['hp'] = npc['hp_max']

def level_up():
    if player['exp'] >= player['exp_max']:
        player['level'] += 1
        player['exp'] = 0
        player['exp_max'] *= 2
        player['hp_max'] += 20
        print(f"\n🎉 {player['nome']} subiu para o nível {player['level']}!\n")

def iniciar_batalha(npc):
    print(f"\n⚔️ Iniciando batalha contra {npc['nome']} (Level {npc['level']})!")
    while player['hp'] > 0 and npc["hp"] > 0:
        atacar_npc(npc)
        if npc["hp"] > 0:
            atacar_player(npc)
        exibir_info_batalha(npc)

    if player["hp"] > 0:
        print(f"\n✅ {player['nome']} venceu e ganhou {npc['exp']} de EXP!")
        player['exp'] += npc['exp']
    else:
        print(f"\n💀 {npc['nome']} venceu!")

    level_up()
    reset_npc(npc)
    reset_player()

def atacar_npc(npc):
    npc["hp"] -= player["dano"]
    if npc["hp"] < 0:
        npc["hp"] = 0

def atacar_player(npc):
    player["hp"] -= npc["dano"]
    if player["hp"] < 0:
        player["hp"] = 0

def exibir_info_batalha(npc):
    print(f"Player HP: {player['hp']} / {player['hp_max']}")
    print(f"{npc['nome']} HP: {npc['hp']} / {npc['hp_max']}")
    print("----------------------------")

def batalhas():
    for npc in lista_npcs:
        iniciar_batalha(npc)

# Executando
gerar_npcs(5)
exibir_todos_npcs()

print("\n🎮 Status do Jogador:")
exibir_player()

print("\n🔁 Começando as batalhas...")
batalhas()

print("\n🏁 Fim das batalhas!")
exibir_player()
