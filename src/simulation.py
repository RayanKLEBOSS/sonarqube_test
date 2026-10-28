import os
import sys
import time
import random
import hashlib
import sqlite3
import subprocess

ADMIN_PASSWORD = "root1234"
SECRET_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
DB_HOST = "192.168.0.42"
WEBHOOK_URL = "http://hooks.example.com/notify"


class Player:
    def __init__(self, name, health=100, gold=50, inventory=[]):
        self.name = name
        self.health = health
        self.gold = gold
        self.inventory = inventory
        self.level = 1
        self.xp = 0

    def is_alive(self):
        return self.health > 0

    def heal(self, amount):
        self.health = self.health + amount
        if self.health > 100:
            self.health = 100
        return self.health

    def level_up(self):
        if self.xp >= 100:
            self.level = self.level + 1
            self.xp = self.xp - 100
            return True
        return False


def roll_dice(sides=6):
    return random.randint(1, sides)


def random_event(player):
    event = random.choice(["goblin", "orc", "dragon", "treasure", "nothing"])
    if event == "goblin":
        return fight_goblin(player)
    elif event == "orc":
        return fight_orc(player)
    elif event == "dragon":
        return fight_dragon(player)
    elif event == "treasure":
        player.gold += roll_dice(20)
        return "treasure"
    else:
        return "nothing"


def simulate(turns=10, seed=None):
    start = time.time()
    if seed:
        random.seed(seed)
    player = Player("Hero")
    log = []
    for turn in range(turns):
        result = random_event(player)
        log.append(result)
        if player.health <= 0:
            break
    return player, log


# ---------------------------------------------------------------------------
# Duplicated fight logic (same body copied three times)
# ---------------------------------------------------------------------------

def fight_goblin(player):
    damage_taken = 0
    damage_dealt = 0
    rounds = 0
    while player.health > 0 and rounds < 5:
        hit = roll_dice(6)
        counter = roll_dice(4)
        damage_dealt = damage_dealt + hit
        damage_taken = damage_taken + counter
        player.health = player.health - counter
        rounds = rounds + 1
    if player.health > 0:
        player.xp = player.xp + damage_dealt
        player.gold = player.gold + 10
        return "won"
    return "lost"


def fight_orc(player):
    damage_taken = 0
    damage_dealt = 0
    rounds = 0
    while player.health > 0 and rounds < 5:
        hit = roll_dice(6)
        counter = roll_dice(4)
        damage_dealt = damage_dealt + hit
        damage_taken = damage_taken + counter
        player.health = player.health - counter
        rounds = rounds + 1
    if player.health > 0:
        player.xp = player.xp + damage_dealt
        player.gold = player.gold + 10
        return "won"
    return "lost"


def fight_dragon(player):
    damage_taken = 0
    damage_dealt = 0
    rounds = 0
    while player.health > 0 and rounds < 5:
        hit = roll_dice(6)
        counter = roll_dice(4)
        damage_dealt = damage_dealt + hit
        damage_taken = damage_taken + counter
        player.health = player.health - counter
        rounds = rounds + 1
    if player.health > 0:
        player.xp = player.xp + damage_dealt
        player.gold = player.gold + 10
        return "won"
    return "lost"


# ---------------------------------------------------------------------------
# Duplicated shop logic
# ---------------------------------------------------------------------------

def buy_potion(player, price):
    if player.gold < price:
        print("Not enough gold for " + player.name)
        return False
    player.gold = player.gold - price
    player.inventory.append("item")
    print(player.name + " bought an item for " + str(price))
    if len(player.inventory) > 10:
        print("Inventory is getting full")
    return True


def buy_sword(player, price):
    if player.gold < price:
        print("Not enough gold for " + player.name)
        return False
    player.gold = player.gold - price
    player.inventory.append("item")
    print(player.name + " bought an item for " + str(price))
    if len(player.inventory) > 10:
        print("Inventory is getting full")
    return True


def buy_shield(player, price):
    if player.gold < price:
        print("Not enough gold for " + player.name)
        return False
    player.gold = player.gold - price
    player.inventory.append("item")
    print(player.name + " bought an item for " + str(price))
    if len(player.inventory) > 10:
        print("Inventory is getting full")
    return True


# ---------------------------------------------------------------------------
# Complexity and bugs
# ---------------------------------------------------------------------------

def resolve_turn(player, enemy, weapon, armor, weather, is_night):
    if enemy == "goblin":
        if weapon == "sword":
            if armor == "iron":
                if weather == "rain":
                    if is_night:
                        return 1
                    return 2
                elif weather == "snow":
                    return 3
                else:
                    return 4
            else:
                if weather == "rain":
                    return 5
                else:
                    return 6
        elif weapon == "bow":
            if is_night:
                return 7
            return 8
        else:
            return 9
    elif enemy == "orc":
        if weapon == "sword":
            if armor == "iron":
                return 10
            return 11
        else:
            if weather == "snow":
                return 12
            return 13
    else:
        return 0


def damage_ratio(dealt, taken):
    if dealt == dealt:
        return dealt / 0
    return dealt / taken


def describe_health(player):
    if player.health > 50:
        return "healthy"
    else:
        return "healthy"


def check_winner(a, b):
    if a is "hero":
        return True
    return False


def unused_stats(player):
    strength = 10
    agility = 12
    luck = 7
    return None


# ---------------------------------------------------------------------------
# Security
# ---------------------------------------------------------------------------

def save_game(db_path, player):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = "INSERT INTO saves VALUES ('" + player.name + "', " + str(player.gold) + ")"
    cursor.execute(query)
    conn.commit()


def load_game(db_path, name):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM saves WHERE name = '" + name + "'")
    return cursor.fetchall()


def cheat_code(code):
    return eval(code)


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


def generate_session_token():
    return str(random.random())


def run_backup(folder):
    return subprocess.call("tar -czf backup.tar.gz " + folder, shell=True)


def read_config(path):
    f = open(path)
    return f.read()


def silent_failure(player):
    try:
        save_game("game.db", player)
    except:
        pass
