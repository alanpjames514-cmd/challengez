import random

player_health = 100
enemy_health = 100

print("Welcome to the Mini RPG Battle")

while player_health > 0 and enemy_health > 0:

    print("\n-----------------------------")
    print("Player Health:", player_health)
    print("Enemy Health:", enemy_health)
    print("-----------------------------")

    action = input("Choose action (attack / defend / heal): ").lower()

    defended = False

    if action == "attack":
        damage = random.randint(10, 30)
        enemy_health -= damage
        print("You attack the enemy for", damage, "damage")

    elif action == "defend":
        defended = True
        print("You defend this turn")

    elif action == "heal":
        heal_amount = random.randint(10, 25)
        player_health += heal_amount
        if player_health > 100:
            player_health = 100
        print("You heal yourself for", heal_amount)

    else:
        print("Invalid action")

    if enemy_health <= 0:
        print("\nYou defeated the enemy")
        break

    enemy_damage = random.randint(10, 35)

    if defended:
        enemy_damage = enemy_damage // 2

    player_health -= enemy_damage
    print("Enemy attacks you for", enemy_damage, "damage")

    if player_health <= 0:
        print("\nYou were defeated by the enemy")
        break
