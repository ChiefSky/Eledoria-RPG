import random as rand 

hp = 0
damage = 0
coins = 0

def printParemeters():
    print("У тебя {0} здоровья, {1} атаки, {2} монет.".format(hp, damage, coins))
    
def printHp():
    print("У тебя", hp, "здоровья")
    
def printDamage():
    print("У тебя", damage, "урона")
    
def printCoins():
    print("У тебя", coins, "монет")
    
def meetShop():
    global hp
    global damage
    global coins
    
    def buy(cost):
        global coins
        if coins >= cost:
            coins -= cost
            printCoins()
            return True
        print("Мало денег!")
        return False
    
    weaponLvl = rand.randint(1, 5)
    weaponDamage = rand.randint(1,5) * weaponLvl
    weapons = ["Палка-копалка", "Молот Громовержца", "Лук Эльфа", "Посох мага", "Алмазный меч"]
    weaponRarities = ["Испорченный", "Обычный", "Редкий", "Эпический", "Легендарный"]
    weaponRarity = weaponRarities[weaponLvl - 1]
    weaponCost = rand.randint(3, 10) * weaponLvl
    weapon = rand.choice(weapons)
    
    oneHpCost = 5
    threeHpCost = 12
    
    print("Вам встретился магазин")
    printParemeters()
    
    while input("Что будешь делать? (зайти/уйти): ").lower() == "зайти":
        print ("1) Одна единица здоровья - ", oneHpCost, "монет")
        print ("2) Три единицы здоровья - ", threeHpCost, "монет")
        print ("3) {0}, {1}, {2} монет".format(weaponRarity, weapon, weaponCost))
    
        choice = input("Что хочешь приобрести?")
        if choice == "1":
            if buy(oneHpCost):
                hp+=1
                printHp()
        elif choice == "2":
            if buy(threeHpCost):
                hp+=3
                printHp()
        elif choice == "3":
            if buy(weaponCost):
                damage = weaponDamage
                printDamage()
        else:
            print("Я такое не продаю")
                

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
        meetShop()
    elif situation == 1:
        input("Вы встретили монстра")
    else:
        input("Блуждаем...")
        
        
initGame(3, 1, 999)

while True:
    gameLoop()
    
    if hp <= 0:
        if input("Сначала? (да/нет): ").lower() == "да":
            initGame(3, 1, 5)
        else:
            break