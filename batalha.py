import json

class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, inimigo):
        inimigo.vida -= self.ataque
        print(f"{self.nome} Ataca {inimigo.nome} e Causa {self.ataque} de Dano!")

    def __str__(self):
        return f"{self.nome} {self.vida}"

class Guerreiro(Personagem):
    def __init__(self, nome, vida, ataque):
        super().__init__(nome, vida, ataque)
        
    def especial(self, inimigo):
        inimigo.vida -= self.ataque + 15
        print(f"{self.nome} Usa Golpe Poderoso em {inimigo.nome} e Causa {self.ataque + 15} de Dano!")

class Mago(Personagem):
    def __init__(self, nome, vida, ataque):
        super().__init__(nome, vida, ataque)
    
    def especial(self):
        self.vida += 25
        print(f"{self.nome} usa Cura e Ganha 25 Pontos de Vida!")    

class Arqueiro(Personagem):
    def __init__(self, nome, vida, ataque):
        super().__init__(nome, vida, ataque)
    
    def especial(self, inimigos):
        if (inimigos[0] != self):
            inimigos[0].vida -= 15
        if (inimigos[1] != self):
            inimigos[1].vida -= 15
        print(f"{self.nome} usa Chuva de Flechas e Causa 15 de Dano a Todos os Inimigos!")
        
def importar_personagens(path):
    characters = []
    count = 0
    with open(path, 'r') as file:
        to_character = json.load(file)
        for dic in to_character:
            name = dic["nome"]
            life = dic["vida"]
            attack = dic["ataque"]
            class_ = dic["classe"]
            if (class_ == "Guerreiro"):
                characters.append(Guerreiro(name, life, attack))
            elif (class_ == "Mago"):
                characters.append(Mago(name, life, attack))
            elif (class_ == "Arqueiro"):
                characters.append(Arqueiro(name, life, attack))
            count += 1
    file.close()
    return characters, count        

def ordenar_personagens_por_vida(personagens):
    sorted_personagens = sorted(personagens, key=lambda personagem: personagem.vida)
    return sorted_personagens

personagens, num_personagens = importar_personagens('personagens.json')
print(f"{num_personagens} Personagens Entram em Batalha!")

personagens = ordenar_personagens_por_vida(personagens)

print(personagens[0])
print(personagens[1])
print(personagens[2])

personagens[0].atacar(personagens[1])
print(personagens[1])

personagens[1].atacar(personagens[2])
print(personagens[2])

personagens[2].atacar(personagens[0])
print(personagens[0])

personagens[0].especial()
print(personagens[0])

personagens[1].especial([personagens[0], personagens[1]])
print(personagens[0])
print(personagens[1])

personagens[2].especial(personagens[1])
print(personagens[1])