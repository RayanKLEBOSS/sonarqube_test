import random

from src.simulation import (
    Player,
    roll_dice,
    random_event,
    simulate,
    fight_goblin,
    buy_potion,
    describe_health,
    hash_password,
)


def test_roll_dice_always_in_range():
    random.seed(1)
    for _ in range(200):
        value = roll_dice(6)
        assert 1 <= value <= 6


def test_player_heal_is_capped_at_100():
    player = Player("Tester", health=90, inventory=[])
    assert player.heal(50) == 100


def test_player_is_alive():
    assert Player("Alive", health=10, inventory=[]).is_alive()
    assert not Player("Dead", health=0, inventory=[]).is_alive()


def test_fight_goblin_returns_valid_result():
    random.seed(7)
    player = Player("Fighter", inventory=[])
    assert fight_goblin(player) in ("won", "lost")


def test_random_event_returns_known_value():
    random.seed(3)
    player = Player("Explorer", inventory=[])
    assert random_event(player) in ("won", "lost", "treasure", "nothing")


def test_simulate_runs_with_seed():
    player, log = simulate(turns=5, seed=42)
    assert 1 <= len(log) <= 5
    assert isinstance(player, Player)


def test_buy_potion_with_enough_gold():
    player = Player("Buyer", gold=100, inventory=[])
    assert buy_potion(player, 30) is True
    assert player.gold == 70


def test_buy_potion_without_enough_gold():
    player = Player("Poor", gold=5, inventory=[])
    assert buy_potion(player, 30) is False


def test_describe_health():
    assert describe_health(Player("Healthy", health=80, inventory=[])) == "healthy"


def test_hash_password_is_deterministic():
    assert hash_password("abc") == hash_password("abc")
