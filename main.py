print("""
░█████╗░  ██████╗░███████╗██████╗░██████╗░░█████╗░  ██████╗░░█████╗░  ░██████╗███████╗██╗░░░░░░█████╗░
██╔══██╗  ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██╔══██╗  ██╔════╝██╔════╝██║░░░░░██╔══██╗
███████║  ██████╔╝█████╗░░██║░░██║██████╔╝███████║  ██║░░██║██║░░██║  ╚█████╗░█████╗░░██║░░░░░██║░░██║
██╔══██║  ██╔═══╝░██╔══╝░░██║░░██║██╔══██╗██╔══██║  ██║░░██║██║░░██║  ░╚═══██╗██╔══╝░░██║░░░░░██║░░██║
██║░░██║  ██║░░░░░███████╗██████╔╝██║░░██║██║░░██║  ██████╔╝╚█████╔╝  ██████╔╝███████╗███████╗╚█████╔╝
╚═╝░░╚═╝  ╚═╝░░░░░╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝  ╚═════╝░░╚════╝░  ╚═════╝░╚══════╝╚══════╝░╚════╝░""".center(120))



print("\n\nBEM-VINDO(A) AO JOGO: A PEDRA DO SELO")
print("""\nHá muito tempo, um poder antigo foi selado dentro de uma pedra mágica conhecida como:\nA PEDRA DO SELO\nEssa pedra não é uma arma comum, ela existe para impedir que um grande mal desperte.\nDurante séculos, ela permaneceu protegida no topo de uma torre sagrada, longe das mãos daqueles que buscavam poder. Mas a paz não durou para sempre.\nUm feiticeiro ambicioso chamado Malzor, o Conquistador, descobriu a existência da pedra… e o segredo por trás de seu poder.\nCom um exército sombrio ao seu comando, ele avançou pelo reino, derrotando todos que tentaram impedi-lo.\nOs guardiões caíram. A torre foi invadida, e agora a pedra está em suas mãos.\nSe Malzor conseguir corromper o poder da Pedra do Selo, nada poderá impedir a destruição do mundo.\nVocê é a última esperança.\nEnfrente os generais de Malzor, atravesse o caminho até a torre e recupere a pedra antes que seja tarde demais.\n\n""")

class Personagem:
    def __init__(self, vida, ataque, defesa, energia=0):
        self.nome = input("Digite um nome para o seu personagem: ")
        self.vida = vida
        self.vida_maxima = vida
        self.ataque = ataque
        self.defesa = defesa
        self.energia = energia
        self.defendendo = False

    def escolher_acao(self):
        print("\n1 - Atacar")
        print("2 - Habilidade")
        print("3 - Defender")
        if self.energia >= 100:
            print("4 - Especial")
        return int(input("Escolha sua ação: "))

    def ganhar_energia(self, quantidade):
        self.energia += quantidade
        if self.energia > 100:
            self.energia = 100

    def realizar_ataque(self, inimigo):
        dano = self.ataque
        if inimigo.defendendo:
            dano = int(dano * (1 - inimigo.defesa))
            print(f"{inimigo.nome} se defendeu! Dano reduzido para {dano}!")
        else:
            self.ganhar_energia(8)  
        inimigo.vida -= dano
        print(f"{self.nome} atacou causando {dano} de dano!")

    def defender(self):
        self.defendendo = True
        print(f"{self.nome} está se defendendo!")

    def usar_habilidade(self, inimigo):
        pass

    def usar_especial(self, inimigo):
        self.energia = 0

    def resetar(self):
        self.vida = self.vida_maxima
        self.energia = 0
        self.defendendo = False

    def combate(self, inimigo):
        print(f"\n==============================\nINIMIGO: {inimigo.nome}\nBATALHA INICIADA!\n==============================")

        while self.vida > 0 and inimigo.vida > 0:
            print("\n========================================\n")
            print(f"            {self.nome}                    ")
            print(f"Vida: {self.vida}\nEnergia: {self.energia}/100\n")
            print(f"            {inimigo.nome}")
            print(f"Vida: {inimigo.vida}\nEnergia: {inimigo.energia}/100")
            print("\n========================================\n")

            acao = self.escolher_acao()

            if acao == 1:
                self.realizar_ataque(inimigo)
            elif acao == 2:
                self.usar_habilidade(inimigo)
            elif acao == 3:
                self.defender()
            elif acao == 4 and self.energia >= 100:
                self.usar_especial(inimigo)

            if inimigo.vida > 0:
                inimigo.agir(self)

            self.defendendo = False
            inimigo.defendendo = False

        if self.vida <= 0:
            print(f"\n{self.nome} foi derrotado!")
        else:
            print(f"\n{inimigo.nome} foi derrotado!")

class Guerreiro(Personagem):
    def __init__(self):
        Personagem.__init__(self, vida=100, ataque=12, defesa=0.40)
        self.classe = "Guerreiro"

    def usar_habilidade(self, inimigo):
        if not inimigo.defendendo:
            self.ganhar_energia(15)  
        self.defendendo = True
        self.defesa = 0.70
        dano = 10
        inimigo.vida -= dano
        print(f"{self.nome} adotou Postura de Combate causando {dano} de dano e aumentando defesa para 70%!")

    def usar_especial(self, inimigo):
        Personagem.usar_especial(self, inimigo)
        dano = 25
        inimigo.vida -= dano
        print(f"{self.nome} usou Fúria de Batalha causando {dano} de dano!")

class Mago(Personagem):
    def __init__(self):
        Personagem.__init__(self, vida=100, ataque=10, defesa=0.20)
        self.classe = "Mago"

    def usar_habilidade(self, inimigo):
        if not inimigo.defendendo:
            self.ganhar_energia(15)
        dano = 20
        inimigo.vida -= dano
        self.defendendo = True
        print(f"{self.nome} lançou Bola de Fogo causando {dano} de dano e recuou se defendendo!")

    def usar_especial(self, inimigo):
        Personagem.usar_especial(self, inimigo)
        inimigo.vida -= 30
        print(f"{self.nome} usou Explosão Arcana causando 30 de dano!")


class Arqueiro(Personagem):
    def __init__(self):
        Personagem.__init__(self, vida=100, ataque=11, defesa=0.30)
        self.classe = "Arqueiro"

    def usar_habilidade(self, inimigo):
        if not inimigo.defendendo:
            self.ganhar_energia(15)
        dano = 20
        inimigo.vida -= dano
        self.defendendo = True
        print(f"{self.nome} usou Disparo Preciso causando {dano} de dano e recuou se defendendo!")

    def usar_especial(self, inimigo):
        Personagem.usar_especial(self, inimigo)
        inimigo.vida -= 28
        print(f"{self.nome} usou Chuva de Flechas causando 28 de dano (ignora defesa)!")


class Assassino(Personagem):
    def __init__(self):
        Personagem.__init__(self, vida=100, ataque=13, defesa=0.35)
        self.classe = "Assassino"

    def usar_habilidade(self, inimigo):
        if not inimigo.defendendo:
            self.ganhar_energia(15)
        dano = 20
        inimigo.vida -= dano
        self.defendendo = True
        print(f"{self.nome} usou Marca da Morte causando {dano} de dano e recuou se defendendo!")

    def usar_especial(self, inimigo):
        Personagem.usar_especial(self, inimigo)
        dano = 35 if inimigo.vida < 50 else 25
        inimigo.vida -= dano
        print(f"{self.nome} usou Golpe Fatal causando {dano} de dano!")


class Inimigo:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.defendendo = False
        self.energia = 0

    def ganhar_energia(self, quantidade):
        self.energia += quantidade
        if self.energia > 100:
            self.energia = 100

    def usar_especial(self, personagem):
        self.energia = 0

    def agir(self, personagem):
        pass

class Drakar(Inimigo):
    def __init__(self):
        Inimigo.__init__(self, "Drakar, o Brutal", vida=100, ataque=13, defesa=0.30)

    def agir(self, personagem):
        if self.energia >= 100:
            self.usar_especial(personagem)
        elif self.vida < 40:
            dano = 18
            if personagem.defendendo:
                dano = int(dano * (1 - personagem.defesa))
            else:
                self.ganhar_energia(15)
            personagem.vida -= dano
            print(f"{self.nome} usou Esmagamento causando {dano} de dano!")
        else:
            dano = self.ataque
            if personagem.defendendo:
                dano = int(dano * (1 - personagem.defesa))
            else:
                self.ganhar_energia(8)
            personagem.vida -= dano
            print(f"{self.nome} atacou causando {dano} de dano!")

    def usar_especial(self, personagem):
        Inimigo.usar_especial(self, personagem)
        dano = 25
        personagem.defendendo = False
        personagem.vida -= dano
        print(f"{self.nome} usou Terremoto causando {dano} de dano e quebrando sua defesa!")

class Selena(Inimigo):
    def __init__(self):
        Inimigo.__init__(self, "Selena, a Sombria", vida=100, ataque=10, defesa=0.30)

    def agir(self, personagem):
        if self.energia >= 100:
            self.usar_especial(personagem)
        elif self.vida < 40:
            self.defendendo = True
            print(f"{self.nome} se defendeu!")
        else:
            dano = self.ataque
            if personagem.defendendo:
                dano = int(dano * (1 - personagem.defesa))
            else:
                self.ganhar_energia(8)
            personagem.vida -= dano
            print(f"{self.nome} atacou causando {dano} de dano!")

    def usar_especial(self, personagem):
        Inimigo.usar_especial(self, personagem)
        dano = 22
        personagem.vida -= dano
        personagem.defendendo = False
        print(f"{self.nome} usou Selo Sombrio causando {dano} de dano e bloqueando sua defesa!")

class Vorn(Inimigo):
    def __init__(self):
        Inimigo.__init__(self, "Vorn, o Veloz", vida=100, ataque=9, defesa=0.50)

    def agir(self, personagem):
        if self.energia >= 100:
            self.usar_especial(personagem)
        else:
            dano = self.ataque
            if personagem.defendendo:
                dano = int(dano * (1 - personagem.defesa))
            else:
                self.ganhar_energia(8)
            personagem.vida -= dano
            print(f"{self.nome} atacou causando {dano} de dano!")

    def usar_especial(self, personagem):
        Inimigo.usar_especial(self, personagem)
        dano = self.ataque * 2
        personagem.vida -= dano
        print(f"{self.nome} usou Ataque Relâmpago atacando duas vezes causando {dano} de dano!")

class Malzor(Inimigo):
    def __init__(self):
        Inimigo.__init__(self, "Malzor, o Conquistador", vida=100, ataque=12, defesa=0.25)

    def agir(self, personagem):
        if self.energia >= 100:
            self.usar_especial(personagem)
        elif self.vida < 40:
            self.vida += 10
            self.ganhar_energia(15)
            print(f"{self.nome} usou Cura e recuperou 10 de vida! Vida atual: {self.vida}")
        else:
            dano = self.ataque
            if personagem.defendendo:
                dano = int(dano * (1 - personagem.defesa))
            else:
                self.ganhar_energia(8)
            personagem.vida -= dano
            print(f"{self.nome} atacou causando {dano} de dano!")

    def usar_especial(self, personagem):
        Inimigo.usar_especial(self, personagem)
        dano = 25
        personagem.vida -= dano
        print(f"{self.nome} usou Domínio Absoluto causando {dano} de dano!")

def escolher_personagem():
    print("ESCOLHA SEU PERSONAGEM")
    print("1 - Guerreiro")
    print("2 - Mago")
    print("3 - Arqueiro")
    print("4 - Assassino")

    escolha = int(input("Digite o número: "))

    if escolha == 1:
        return Guerreiro()
    elif escolha == 2:
        return Mago()
    elif escolha == 3:
        return Arqueiro()
    elif escolha == 4:
        return Assassino()

personagem = escolher_personagem()

drakar = Drakar()
personagem.combate(drakar)

if personagem.vida > 0:
    personagem.resetar()
    selena = Selena()
    personagem.combate(selena)

if personagem.vida > 0:
    personagem.resetar()
    vorn = Vorn()
    personagem.combate(vorn)

if personagem.vida > 0:
    personagem.resetar()
    malzor = Malzor()
    personagem.combate(malzor)

if personagem.vida > 0:
    print(f"\nPARABÉNS {personagem.nome.upper()} VOCÊ VENCEU TOODOS OS INIMIGOS E SALVOU O REINO!")