player = {"name":input("Введите имя игрока: "), "health" : 100, "damage": 50,"armor": 1.2}
enemy = {"name":input("Введите имя противника: "), "health" : 50, "damage": 30,"armor": 1}

def get_damage(damage,armor):
    return damage / armor
def attack(unit, target):
    damage = get_damage(unit["damage"],target["armor"])
    target["health"] -= damage
attack(player, enemy)
print(player)
print(enemy)