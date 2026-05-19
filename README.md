# A Pedra do Selo — Jogo de RPG em Python

## Sobre o projeto

**A Pedra do Selo** é um jogo de RPG por turnos desenvolvido inteiramente em Python puro, sem dependências externas. O jogador é apresentado à história do mundo, escolhe seu personagem e parte para uma jornada de batalhas contra inimigos cada vez mais poderosos.

Projeto desenvolvido como atividade acadêmica, com foco em orientação a objetos, lógica de combate e estruturação de código em Python.

---

## Como jogar

Ao iniciar o jogo, o jogador passa por três etapas:

1. **Narrativa introdutória** — a história do mundo é apresentada
2. **Escolha de personagem** — selecione uma das quatro classes disponíveis
3. **Nome do herói** — personalize seu personagem com um nome
4. **Batalha** — enfrente os inimigos em combate por turnos

### Ações disponíveis em combate

| Ação | Descrição |
|------|-----------|
| Atacar | Desfere um golpe básico no inimigo |
| Habilidade | Usa uma habilidade especial da sua classe |
| Defender | Reduz o dano recebido no próximo turno |
| Poder especial | Disponível ao encher a barra de energia |

---

## Classes de personagem

| Classe | Estilo de jogo |
|--------|----------------|
| **Guerreiro** | Grande resistência, ataques fortes e habilidades de contra-ataque |
| **Mago** | Magias destrutivas com efeitos contínuos, mas pouca defesa |
| **Arqueiro** | Especialista em ataques precisos à distância e golpes que ignoram defesa |
| **Assassino** | Combate veloz e letal, focado em dano crítico e execução |

---

## Inimigos

O jogo conta com **4 inimigos**, cada um com características, atributos e habilidades distintas. Os três primeiros aumentam progressivamente em dificuldade. O **quarto inimigo é o chefe final**, o mais poderoso da jornada.

---

## Como executar

### Pré-requisitos

- Python 3.12 ou superior
- Nenhuma biblioteca externa necessária

### Rodando o jogo

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/a-pedra-do-selo.git

# Acesse a pasta do projeto
cd a-pedra-do-selo

# Execute o jogo
python main.py
```

---

## Tecnologias utilizadas

- **Python 3.12+**
- Apenas bibliotecas padrão da linguagem (sem dependências externas)

---
