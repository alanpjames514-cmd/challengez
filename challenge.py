import random

player_health = 100
enemy_health = 100

print("⚔️ Welcome to the Mini RPG Battle ⚔️")

while player_health > 0 and enemy_health > 0:
    print("\n-----------------------------")
    print(f"Player Health: {player_health}")
    print(f"Enemy Health: {enemy_health}")
    print("-----------------------------")

    action = input("Choose action (attack / defend / heal): ").lower()

    defended = False

    # PLAYER ACTION
    if action == "attack":
        damage = random.randint(10, 30)
        enemy_health -= damage
        print(f"You attack the enemy for {damage} damage!")

    elif action == "defend":
        defended = True
        print("You defend! Enemy attack damage will be reduced.")

    elif action == "heal":
        heal_amount = random.randint(10, 25)
        player_health += heal_amount
        if player_health > 100:
            player_health = 100
        print(f"You heal yourself for {heal_amount} health!")

    else:
        print("Invalid action! You lose your turn.")

    # CHECK IF ENEMY IS DEAD
    if enemy_health <= 0:
        print("\n🎉 You defeated the enemy! You win!")
        break

    # ENEMY ATTACK
    enemy_damage = random.randint(10, 35)

    if defended:
        enemy_damage = enemy_damage // 2

    player_health -= enemy_damage
    print(f"Enemy attacks you for {enemy_damage} damage!")

    # CHECK IF PLAYER IS DEAD
    if player_health <= 0:
        print("\n💀 You were defeated by the enemy. Game Over!")
        break
