# ================================
#   MeowOS 4.5 — ПОЛНАЯ СБОРКА
#   для Pydroid 3 (Android)
# ================================

import time
import os
import random
import json

GREEN, RED, YELLOW, BLUE, RESET = "\033[92m", "\033[91m", "\033[93m", "\033[94m", "\033[0m"

LOGO = r"""
   /\_/\    МУР-техника
  ( o.o )   MeowOS 4.5
   > ^ <    на базе Linux
"""

# ---------- ПУТИ / СОХРАНЕНИЯ ----------
SAVE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "meowcoins.json")
STATS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "meowstats.json")

def clear():
    os.system('clear')

def load_balance():
    try:
        with open(SAVE_FILE, "r") as f:
            return json.load(f).get("balance", 100)
    except (FileNotFoundError, json.JSONDecodeError):
        return 100

def save_balance(balance):
    try:
        with open(SAVE_FILE, "w") as f:
            json.dump({"balance": balance}, f)
    except Exception as e:
        print(RED + f"⚠ не смог сохранить: {e}" + RESET)

def load_stats():
    try:
        with open(STATS_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"wins": 0, "losses": 0, "best_balance": 100}

def save_stats(stats):
    try:
        with open(STATS_FILE, "w") as f:
            json.dump(stats, f)
    except Exception:
        pass

def update_stats(win=None, balance=None):
    stats = load_stats()
    if win is True:
        stats["wins"] = stats.get("wins", 0) + 1
    elif win is False:
        stats["losses"] = stats.get("losses", 0) + 1
    if balance is not None:
        if balance > stats.get("best_balance", 0):
            stats["best_balance"] = balance
    save_stats(stats)

# ---------- ЗАГРУЗКА ----------
def boot():
    clear()
    print(GREEN)
    print(LOGO)
    print(RESET)
    time.sleep(0.5)
    steps = [
        "загрузка ядра meow-6.9...",
        "проверка мур-памяти...",
        "запуск FilyaGPT...",
        "поиск Фили...",
        "Филя найден! 🐱",
    ]
    for s in steps:
        print(GREEN + "[*] " + s + RESET)
        time.sleep(0.4)
    print(GREEN + "✔ система готова!" + RESET)
    time.sleep(0.5)

# ---------- ИНФО О СИСТЕМЕ ----------
def sysinfo():
    clear()
    print(GREEN + "=== MeowOS 4.5 ===" + RESET)
    print("Процессор : МУР 9999 PRO MAX ULTRA")
    print("ОЗУ       : 10 терамур")
    print("Диск      : 15 ТБ мяу-стор")
    print("Ядро      : meow-6.9-generic")
    print("Филя      : 🐱 на связи")
    print(GREEN + "===================" + RESET)

    # статистика
    stats = load_stats()
    balance = load_balance()
    print(f"\n💰 Баланс: {balance} 🪙")
    print(f"🏆 Побед: {stats.get('wins', 0)}")
    print(f"💀 Поражений: {stats.get('losses', 0)}")
    print(f"👑 Рекорд баланса: {stats.get('best_balance', 0)} 🪙")
    input("\nEnter — назад...")

# ---------- СТАТУС ФИЛИ ----------
def filya_status():
    clear()
    moods = {
        "🔴": "Филя злой или очень игривый",
        "🔵": "Филя спокойный",
        "⚪": "Филя спит",
    }
    mood = random.choice(list(moods.keys()))
    print(GREEN + f"🐱 Настроение Фили: {mood}" + RESET)
    print(f"   {moods[mood]}")
    bowl = input("\n🥩 Миска полная? (да/нет): ").strip().lower()
    if bowl in ("нет", "no", "n", "не"):
        print(RED + "⚠ ПОКОРМИ ФИЛЮ! 🥩" + RESET)
    else:
        print(GREEN + "😺 Филя доволен" + RESET)
    input("\nEnter — назад...")

# ---------- КАЛЬКУЛЯТОР ----------
def calculator():
    clear()
    print(GREEN + "=== МУР-калькулятор ===" + RESET)
    try:
        a = float(input("число 1: "))
        op = input("оператор (+ - * /): ").strip()
        b = float(input("число 2: "))
        if op == "+": result = a + b
        elif op == "-": result = a - b
        elif op == "*": result = a * b
        elif op == "/":
            if b == 0:
                print(RED + "⚠ на ноль делить нельзя!" + RESET)
                input("\nEnter — назад...")
                return
            result = a / b
        else:
            print(RED + "⚠ неизвестный оператор" + RESET)
            input("\nEnter — назад...")
            return
        print(GREEN + f"{a} {op} {b} = {result}" + RESET)
    except ValueError:
        print(RED + "⚠ это не число!" + RESET)
    input("\nEnter — назад...")

# ================================
#   СТАРЫЕ ИГРЫ
# ================================

# ---------- ИГРА: УГАДАЙ ЧИСЛО ----------
def guess_game():
    clear()
    print(GREEN + "=== 🎯 Угадай число от 1 до 100 ===" + RESET)
    secret = random.randint(1, 100)
    attempts = 0
    max_tries = 10
    while attempts < max_tries:
        print(f"Попытка {attempts + 1}/{max_tries}")
        try:
            guess = int(input("введи число (0 — выход): "))
        except ValueError:
            print(RED + "⚠ введи число!" + RESET)
            continue
        if guess == 0:
            return
        attempts += 1
        if guess < secret:
            print("📈 Больше!")
        elif guess > secret:
            print("📉 Меньше!")
        else:
            print(GREEN + f"🎉 Угадал! Число {secret}, попыток: {attempts}" + RESET)
            update_stats(win=True)
            input("\nEnter — назад...")
            return
    print(RED + f"💀 Не угадал! Было: {secret}" + RESET)
    update_stats(win=False)
    input("\nEnter — назад...")

# ---------- ИГРА: КНБ ----------
def rps():
    clear()
    print(GREEN + "=== ✊✋✌ Камень-Ножницы-Бумага ===" + RESET)
    options = {"1": "✊ Камень", "2": "✋ Бумага", "3": "✌ Ножницы"}
    wins = {"1": "3", "2": "1", "3": "2"}
    score_p, score_c = 0, 0
    while True:
        print(f"\n{YELLOW}Счёт: ты {score_p} : {score_c} Филя{RESET}")
        for k, v in options.items():
            print(f"  {k}. {v}")
        print("  0. Выход")
        choice = input("\nмяу> ").strip()
        if choice == "0":
            if score_p > score_c:
                update_stats(win=True)
            elif score_p < score_c:
                update_stats(win=False)
            return
        if choice not in options:
            print(RED + "⚠ выбери 1, 2 или 3" + RESET)
            continue
        comp = random.choice(list(options.keys()))
        print(f"Ты: {options[choice]}  |  Филя: {options[comp]}")
        if choice == comp:
            print(YELLOW + "🤝 Ничья!" + RESET)
        elif wins[choice] == comp:
            print(GREEN + "🎉 Ты выиграл!" + RESET)
            score_p += 1
        else:
            print(RED + "🐱 Филя выиграл!" + RESET)
            score_c += 1

# ---------- ИГРА: ВИСЕЛИЦА ----------
def hangman():
    clear()
    print(GREEN + "=== 🐱 Виселица ===" + RESET)
    words = ["кошка", "молоко", "мяу", "филя", "мурка", "лапка", "хвост", "мурлыка", "котёнок"]
    word = random.choice(words)
    guessed = set()
    tries = 6
    while tries > 0:
        display = " ".join(c if c in guessed else "_" for c in word)
        print(f"\n{YELLOW}Слово: {display}{RESET}")
        print(f"Попыток: {tries}")
        if guessed:
            print(f"Буквы: {' '.join(sorted(guessed))}")
        if all(c in guessed for c in word):
            print(GREEN + f"\n🎉 Угадал! Слово: {word}" + RESET)
            update_stats(win=True)
            input("\nEnter — назад...")
            return
        letter = input("буква (0 — выход): ").strip().lower()
        if letter == "0":
            return
        if len(letter) != 1 or not letter.isalpha():
            print(RED + "⚠ одна буква!" + RESET)
            continue
        if letter in guessed:
            print(YELLOW + "уже была" + RESET)
            continue
        guessed.add(letter)
        if letter in word:
            print(GREEN + "✔ есть!" + RESET)
        else:
            print(RED + "✘ нет" + RESET)
            tries -= 1
    print(RED + f"\n💀 Проиграл! Слово было: {word}" + RESET)
    update_stats(win=False)
    input("\nEnter — назад...")

# ---------- ИГРА: ЗМЕЙКА ----------
def snake():
    clear()
    print(GREEN + "=== 🐍 Змейка (пошаговая) ===" + RESET)
    print("Управление: w/a/s/d + Enter, q — выход")
    print("Поле 10x10\n")
    time.sleep(1)

    W, H = 10, 10
    snake_body = [(5, 5), (5, 4), (5, 3)]
    food = (random.randint(1, H-2), random.randint(1, W-2))
    score = 0

    while True:
        clear()
        print(GREEN + f"Счёт: {score}   (w/a/s/d + Enter, q — выход)" + RESET)
        for y in range(H):
            row = ""
            for x in range(W):
                if (y, x) == snake_body[0]:
                    row += "🟢"
                elif (y, x) in snake_body:
                    row += "🟩"
                elif (y, x) == food:
                    row += "🍎"
                elif y == 0 or y == H-1 or x == 0 or x == W-1:
                    row += "⬛"
                else:
                    row += "⬜"
            print(row)

        move = input("\nмяу> ").strip().lower()
        if move == "q":
            print(RED + f"выход. Счёт: {score}" + RESET)
            if score > 0:
                update_stats(win=True)
            input("Enter...")
            return
        if move not in ("w", "a", "s", "d"):
            continue

        head_y, head_x = snake_body[0]
        if move == "w": head_y -= 1
        elif move == "s": head_y += 1
        elif move == "a": head_x -= 1
        elif move == "d": head_x += 1

        new_head = (head_y, head_x)

        if (head_y <= 0 or head_y >= H-1 or
            head_x <= 0 or head_x >= W-1 or
            new_head in snake_body):
            print(RED + f"\n💀 Игра окончена! Счёт: {score}" + RESET)
            update_stats(win=False)
            input("Enter...")
            return

        snake_body.insert(0, new_head)

        if new_head == food:
            score += 1
            while True:
                food = (random.randint(1, H-2), random.randint(1, W-2))
                if food not in snake_body:
                    break
        else:
            snake_body.pop()

# ================================
#   КАРТОЧНЫЕ ИГРЫ
# ================================

# ---------- ОЧКО (русское) ----------
def ochko():
    clear()
    print(GREEN + "=== 🇷🇺 ОЧКО (русская версия) ===" + RESET)
    print("Цель: набрать 21 очко или близко к нему")
    print("6,7,8,9,10 = номинал; В/Д/К/Т = 11")
    print("Филя добирает до 17\n")
    time.sleep(0.5)

    deck = [6, 7, 8, 9, 10, 11, 11, 11, 11] * 4
    random.shuffle(deck)

    def draw():
        return deck.pop()

    player = [draw(), draw()]
    dealer = [draw(), draw()]

    def show(cards):
        return " + ".join(str(c) for c in cards) + f" = {sum(cards)}"

    print(f"Твои карты: {show(player)}")
    print(f"Карты Фили: {dealer[0]} + [?] = ?")

    while sum(player) < 21:
        choice = input("\n1 — взять, 2 — хватит, 0 — выход: ").strip()
        if choice == "0":
            return
        if choice == "2":
            break
        if choice == "1":
            card = draw()
            player.append(card)
            print(f"Взял: {card}  →  {show(player)}")
            if sum(player) > 21:
                print(RED + f"\n💥 Перебор! {sum(player)}. Филя выиграл!" + RESET)
                update_stats(win=False)
                input("\nEnter — назад...")
                return
        else:
            print(RED + "⚠ введи 1, 2 или 0" + RESET)

    print(YELLOW + f"\n🐱 Филя открывает вторую: {dealer[1]}" + RESET)
    print(f"У Фили: {show(dealer)}")
    time.sleep(0.8)
    while sum(dealer) < 17:
        card = draw()
        dealer.append(card)
        print(f"Филя взял: {card}  →  {show(dealer)}")
        time.sleep(0.5)

    p, d = sum(player), sum(dealer)
    print(f"\n{YELLOW}Ты: {p}  |  Филя: {d}{RESET}")
    if d > 21:
        print(GREEN + "🎉 У Фили перебор! Ты выиграл!" + RESET)
        update_stats(win=True)
    elif p > d:
        print(GREEN + "🎉 Ты выиграл!" + RESET)
        update_stats(win=True)
    elif p < d:
        print(RED + "🐱 Филя выиграл!" + RESET)
        update_stats(win=False)
    else:
        print(YELLOW + "🤝 Ничья!" + RESET)
    input("\nEnter — назад...")

# ---------- BLACKJACK (казино) ----------
def blackjack():
    clear()
    print(GREEN + "=== 🎰 BLACKJACK (казино) ===" + RESET)
    print("Цель: набрать 21 или обыграть Филю, не перебрав")
    print("J/Q/K = 10, Туз = 1 или 11")
    print("Филя стоит на 17, берёт до 16\n")

    suits = ["♠", "♥", "♦", "♣"]
    ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

    def make_deck():
        d = [(r, s) for s in suits for r in ranks]
        random.shuffle(d)
        return d

    def card_value(rank):
        if rank in ("J", "Q", "K"):
            return 10
        if rank == "A":
            return 11
        return int(rank)

    def hand_value(hand):
        total = sum(card_value(r) for r, s in hand)
        aces = sum(1 for r, s in hand if r == "A")
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

    def show(hand, hide_first=False):
        if hide_first:
            return f"[{hand[0][0]}{hand[0][1]}] [?]"
        return " ".join(f"[{r}{s}]" for r, s in hand)

    balance = load_balance()
    print(f"💰 Твой баланс: {balance} мяу-коинов\n")

    while True:
        if balance <= 0:
            print(RED + "💸 Ты банкрот! Филя забирает всё 🐱" + RESET)
            save_balance(balance)
            input("\nEnter — назад...")
            return

        try:
            bet = int(input(f"Ставка (1-{balance}, 0 — выход): ").strip())
        except ValueError:
            print(RED + "⚠ введи число" + RESET)
            continue
        if bet == 0:
            print(GREEN + f"💰 Ты уходишь с {balance} мяу-коинами" + RESET)
            save_balance(balance)
            input("\nEnter — назад...")
            return
        if bet < 1 or bet > balance:
            print(RED + f"⚠ ставка от 1 до {balance}" + RESET)
            continue

        deck = make_deck()
        player = [deck.pop(), deck.pop()]
        dealer = [deck.pop(), deck.pop()]

        clear()
        print(GREEN + f"=== 🎰 Ставка: {bet} 🪙 ===" + RESET)
        print(f"Твои карты: {show(player)}  = {hand_value(player)}")
        print(f"Карты Фили: {show(dealer, hide_first=True)}")

        p_bj = len(player) == 2 and hand_value(player) == 21
        d_bj = len(dealer) == 2 and hand_value(dealer) == 21

        if p_bj or d_bj:
            print(f"\n{YELLOW}Филя открывает: {show(dealer)} = {hand_value(dealer)}{RESET}")
            if p_bj and d_bj:
                print(YELLOW + "🤝 У обоих Blackjack! Ничья." + RESET)
            elif p_bj:
                print(GREEN + "🎉 BLACKJACK! Ты выиграл x2.5!" + RESET)
                balance += int(bet * 1.5)
                update_stats(win=True)
            else:
                print(RED + "🐱 У Фили Blackjack! Ты проиграл." + RESET)
                balance -= bet
                update_stats(win=False)
            save_balance(balance)
            update_stats(balance=balance)
            print(f"💰 Баланс: {balance}")
            input("\nEnter — продолжить...")
            continue

        # ход игрока
        while True:
            pv = hand_value(player)
            if pv >= 21:
                break
            print(f"\n{YELLOW}Твои карты: {show(player)} = {pv}{RESET}")
            opts = "1 — взять, 2 — хватит"
            if len(player) == 2 and balance >= bet * 2:
                opts += ", 3 — удвоить"
            opts += ", 0 — выход"
            choice = input(opts + "\nмяу> ").strip()

            if choice == "0":
                save_balance(balance)
                return
            if choice == "1":
                player.append(deck.pop())
                nv = hand_value(player)
                print(f"Взял: [{player[-1][0]}{player[-1][1]}] → {nv}")
                if nv > 21:
                    print(RED + f"\n💥 Перебор! {nv} > 21." + RESET)
                    balance -= bet
                    save_balance(balance)
                    update_stats(win=False, balance=balance)
                    print(f"💰 Баланс: {balance}")
                    input("\nEnter — продолжить...")
                    break
            elif choice == "2":
                break
            elif choice == "3" and len(player) == 2 and balance >= bet * 2:
                bet *= 2
                player.append(deck.pop())
                print(f"Удвоил! Ставка: {bet}")
                print(f"Взял: [{player[-1][0]}{player[-1][1]}] → {hand_value(player)}")
                if hand_value(player) > 21:
                    print(RED + f"💥 Перебор! {hand_value(player)}" + RESET)
                    balance -= bet
                    save_balance(balance)
                    update_stats(win=False, balance=balance)
                    print(f"💰 Баланс: {balance}")
                    input("\nEnter — продолжить...")
                    break
                break
            else:
                print(RED + "⚠ неверный ввод" + RESET)

        if hand_value(player) > 21:
            continue

        # ход Фили
        print(YELLOW + f"\n🐱 Филя открывает: {show(dealer)} = {hand_value(dealer)}" + RESET)
        time.sleep(0.8)
        while hand_value(dealer) < 17:
            dealer.append(deck.pop())
            print(f"Филя взял: [{dealer[-1][0]}{dealer[-1][1]}] → {hand_value(dealer)}")
            time.sleep(0.6)

        pv, dv = hand_value(player), hand_value(dealer)
        print(f"\n{YELLOW}Ты: {pv}  |  Филя: {dv}{RESET}")

        if dv > 21:
            print(GREEN + f"🎉 У Фили перебор! Ты выиграл +{bet} 🪙" + RESET)
            balance += bet
            update_stats(win=True)
        elif pv > dv:
            print(GREEN + f"🎉 Ты выиграл +{bet} 🪙" + RESET)
            balance += bet
            update_stats(win=True)
        elif pv < dv:
            print(RED + f"🐱 Филя выиграл -{bet} 🪙" + RESET)
            balance -= bet
            update_stats(win=False)
        else:
            print(YELLOW + "🤝 Ничья. Ставка возвращается." + RESET)

        save_balance(balance)
        update_stats(balance=balance)
        print(f"💰 Баланс: {balance}")
        input("\nEnter — продолжить...")

# ================================
#   МЕНЮ
# ================================

def games_menu():
    while True:
        clear()
        print(GREEN + "=== 🎮 ИГРЫ MeowOS ===" + RESET)
        print("1. 🎯 Угадай число")
        print("2. ✊ Камень-Ножницы-Бумага")
        print("3. 🐱 Виселица")
        print("4. 🐍 Змейка")
        print("5. 🃏 Карточные игры")
        print("0. ↩ Назад")
        cmd = input("\nмяу> ").strip()
        if cmd == "1":
            guess_game()
        elif cmd == "2":
            rps()
        elif cmd == "3":
            hangman()
        elif cmd == "4":
            snake()
        elif cmd == "5":
            card_games_menu()
        elif cmd == "0":
            return
        else:
            print(RED + "❓ нет такой игры" + RESET)
            time.sleep(0.8)

def card_games_menu():
    while True:
        clear()
        print(GREEN + "=== 🃏 КАРТОЧНЫЕ ИГРЫ ===" + RESET)
        print("1. 🇷🇺 Очко (русская версия)")
        print("2. 🎰 Blackjack (казино, со ставками)")
        print("3. 🗑 Сбросить баланс (100 🪙)")
        print("0. ↩ Назад")
        cmd = input("\nмяу> ").strip()
        if cmd == "1":
            ochko()
        elif cmd == "2":
            blackjack()
        elif cmd == "3":
            save_balance(100)
            print(GREEN + "💰 Баланс сброшен до 100 🪙" + RESET)
            input("Enter...")
        elif cmd == "0":
            return
        else:
            print(RED + "❓ нет такого пункта" + RESET)
            time.sleep(0.8)

def menu():
    while True:
        print("\n" + GREEN + "=== MeowOS Меню ===" + RESET)
        print("1. 🎮 Игры")
        print("2. 🧮 Калькулятор")
        print("3. 🐱 Статус Фили")
        print("4. 💻 Инфо о системе")
        print("0. 📴 Выход")
        cmd = input("\n" + GREEN + "мяу> " + RESET).strip()
        if cmd == "1":
            games_menu()
        elif cmd == "2":
            calculator()
        elif cmd == "3":
            filya_status()
        elif cmd == "4":
            sysinfo()
        elif cmd == "0":
            print(RED + "📴 выключение MeowOS..." + RESET)
            time.sleep(0.5)
            print(GREEN + "🐱 мяу! до связи!" + RESET)
            break
        else:
            print(RED + "❓ неизвестная команда" + RESET)

# ================================
#   ЗАПУСК
# ================================
boot()
menu()