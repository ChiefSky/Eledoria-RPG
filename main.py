import random as rand 

hp = 0
damage = 0
coins = 0

def printParemeters():
    print("У тебя {0} здоровья, {1} атаки, {2} монет.".format(hp, damage, coins))

def initGame(initHp, initDamage, initCoins):
    global hp
    global damage
    global coins
    
    hp = initHp
    damage = initDamage
    coins = initCoins
    
    print("Вы отправились в путешествие!")
    printParemeters()
    
def gameLoop():
    situation = rand.randint(0, 3)
    if situation == 0:
        input("Вы встретили магазин")
    elif situation == 1:
        input("Вы встретили монстра")
    else:
        input("Блуждаем...")
        
        
initGame(3, 1, 5)

while True:
    gameLoop()
    
    if hp <= 0:
        if input("Сначала? (да/нет): ").lower() == "да":
            initGame(3, 1, 5)
        else:
            break