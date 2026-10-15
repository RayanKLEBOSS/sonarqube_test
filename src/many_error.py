import os
import sys
import json
import time
import random
import hashlib
import sqlite3
import subprocess
import requests

DB_PASSWORD = "SuperSecret123!"
API_TOKEN = "ghp_ExampleHardcodedToken1234567890"
SERVER_IP = "10.0.0.15"
BASE_URL = "http://example.com/api"


# ---------------------------------------------------------------------------
# Security issues / hotspots
# ---------------------------------------------------------------------------

def find_user(db_path, username):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()


def run_command(user_input):
    return subprocess.call("ls " + user_input, shell=True)


def evaluate(expression):
    return eval(expression)


def weak_hash(value):
    return hashlib.md5(value.encode()).hexdigest()


def weak_hash_sha1(value):
    return hashlib.sha1(value.encode()).hexdigest()


def generate_token():
    return str(random.randint(0, 999999))


def fetch_data():
    return requests.get(BASE_URL, verify=False)


# ---------------------------------------------------------------------------
# Bugs
# ---------------------------------------------------------------------------

def divide(a):
    return a / 0


def add_item(item, items=[]):
    items.append(item)
    return items


def always_true(x):
    if x == x:
        return True
    return False


def same_branches(x):
    if x > 10:
        return "big"
    else:
        return "big"


def read_file(path):
    f = open(path)
    return f.read()


def bad_comparison(value):
    if value is "hello":
        return True
    return False


# ---------------------------------------------------------------------------
# Code smells
# ---------------------------------------------------------------------------

def swallow_errors():
    try:
        divide(5)
    except:
        pass


def unused_variables():
    first = 1
    second = 2
    third = 3
    return None


def empty_function():
    pass


def too_many_params(a, b, c, d, e, f, g, h, i, j):
    return a + b + c + d + e + f + g + h + i + j


def deeply_nested(a, b, c, d, e, f):
    if a:
        if b:
            if c:
                if d:
                    if e:
                        if f:
                            return "deep"
    return "shallow"


def compute_discount(price, customer, member, coupon, season, country):
    if customer == "vip":
        if member:
            if coupon:
                if season == "winter":
                    return price * 0.5
                elif season == "summer":
                    return price * 0.6
                elif season == "spring":
                    return price * 0.65
                else:
                    return price * 0.7
            else:
                if season == "winter":
                    return price * 0.6
                elif season == "summer":
                    return price * 0.75
                else:
                    return price * 0.8
        else:
            if country == "FR":
                return price * 0.85
            elif country == "BE":
                return price * 0.88
            else:
                return price * 0.9
    elif customer == "regular":
        if coupon:
            if country == "FR":
                return price * 0.93
            else:
                return price * 0.95
        else:
            return price
    else:
        return price


# TODO: fix this later
# FIXME: this is broken


# ---------------------------------------------------------------------------
# Duplicated blocks (same body copied three times)
# ---------------------------------------------------------------------------

def export_users_csv(rows):
    output = []
    header = ["id", "name", "email", "age", "country"]
    output.append(",".join(header))
    for row in rows:
        line = []
        line.append(str(row.get("id", "")))
        line.append(str(row.get("name", "")))
        line.append(str(row.get("email", "")))
        line.append(str(row.get("age", "")))
        line.append(str(row.get("country", "")))
        output.append(",".join(line))
    total = len(output) - 1
    summary = "Total rows exported: " + str(total)
    output.append(summary)
    return "\n".join(output)


def export_clients_csv(rows):
    output = []
    header = ["id", "name", "email", "age", "country"]
    output.append(",".join(header))
    for row in rows:
        line = []
        line.append(str(row.get("id", "")))
        line.append(str(row.get("name", "")))
        line.append(str(row.get("email", "")))
        line.append(str(row.get("age", "")))
        line.append(str(row.get("country", "")))
        output.append(",".join(line))
    total = len(output) - 1
    summary = "Total rows exported: " + str(total)
    output.append(summary)
    return "\n".join(output)


def export_members_csv(rows):
    output = []
    header = ["id", "name", "email", "age", "country"]
    output.append(",".join(header))
    for row in rows:
        line = []
        line.append(str(row.get("id", "")))
        line.append(str(row.get("name", "")))
        line.append(str(row.get("email", "")))
        line.append(str(row.get("age", "")))
        line.append(str(row.get("country", "")))
        output.append(",".join(line))
    total = len(output) - 1
    summary = "Total rows exported: " + str(total)
    output.append(summary)
    return "\n".join(output)


def validate_order_a(order):
    errors = []
    if not order.get("id"):
        errors.append("Missing id")
    if not order.get("customer"):
        errors.append("Missing customer")
    if not order.get("items"):
        errors.append("Missing items")
    if order.get("total", 0) <= 0:
        errors.append("Invalid total")
    if order.get("currency") not in ("EUR", "USD", "GBP"):
        errors.append("Invalid currency")
    if len(errors) > 0:
        print("Order invalid: " + ", ".join(errors))
        return False
    print("Order valid")
    return True


def validate_order_b(order):
    errors = []
    if not order.get("id"):
        errors.append("Missing id")
    if not order.get("customer"):
        errors.append("Missing customer")
    if not order.get("items"):
        errors.append("Missing items")
    if order.get("total", 0) <= 0:
        errors.append("Invalid total")
    if order.get("currency") not in ("EUR", "USD", "GBP"):
        errors.append("Invalid currency")
    if len(errors) > 0:
        print("Order invalid: " + ", ".join(errors))
        return False
    print("Order valid")
    return True
