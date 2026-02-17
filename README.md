# 🪨📄✂️ Rock Paper Scissors AI Bot (Python)

## 📌 Overview
This project implements an intelligent **Rock, Paper, Scissors AI bot** in Python.  
The bot is designed to compete against multiple opponent bots and achieve a **minimum 60% win rate** in every match.

Unlike a random player, this bot **analyzes opponent behavior**, detects patterns, and adapts its strategy dynamically.

---

## 🎯 Objective
- Play Rock, Paper, Scissors against four different bots
- Win **at least 60%** of the games against each bot
- Use only the provided game engine
- Modify code **only** in `RPS.py`

---

## 🧠 Strategy Used
The bot uses a combination of techniques:

- **Frequency Analysis**  
  Counts how often the opponent uses each move and counters the most common one.

- **Pattern Detection**  
  Detects repeated moves and predictable behavior.

- **Reactive Strategy Handling**  
  Handles copy and counter-based bots effectively.

- **Move Transition Prediction**  
  Predicts the opponent’s next move based on past transitions.

- **Controlled Randomness**  
  Prevents opponents from exploiting predictable behavior.

---

## 🛠️ Technologies
- Python 3
- Game strategy logic
- Pattern recognition
- State management using function arguments

---

## 📁 Project Structure

├── RPS.py # AI player logic (modified)
├── RPS_game.py # Game engine and bots (do not modify)
├── main.py # Local testing file
├── test_module.py # Automated tests


---

## ▶️ How to Run
Run the program using:

```bash
python main.py

Test against a specific bot:

play(player, quincy, 1000)

Enable verbose mode:
play(player, quincy, 100, verbose=True)

✅ Results

Successfully defeats all four opponent bots

Achieves 60%+ win rate consistently

Passes all automated unit tests

🧪 Testing

Unit tests are included in test_module.py.

To run tests automatically, uncomment the test call in main.py.

🏆 Key Learnings

Avoiding mutable default argument bugs in Python

Designing adaptive algorithms

Writing test-compliant competitive code

Implementing intelligent behavior without ML libraries


---


Just tell me 🚀
