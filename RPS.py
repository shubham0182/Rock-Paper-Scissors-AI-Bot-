import random

def player(prev_play, opponent_history=[]):
    # 🔥 RESET history at the start of each match
    if prev_play == "":
        opponent_history.clear()

    # Save opponent move
    if prev_play != "":
        opponent_history.append(prev_play)

    # First move
    if len(opponent_history) == 0:
        return random.choice(["R", "P", "S"])

    # Counter helper
    def counter(move):
        return {"R": "P", "P": "S", "S": "R"}[move]

    # -----------------------------
    # Frequency Analysis (SAFE)
    # -----------------------------
    move_counts = {
        "R": opponent_history.count("R"),
        "P": opponent_history.count("P"),
        "S": opponent_history.count("S"),
    }

    most_common = None
    max_count = -1

    for move in move_counts:
        if move_counts[move] > max_count:
            max_count = move_counts[move]
            most_common = move

    freq_counter = counter(most_common)

    # -----------------------------
    # Repetition Detection
    # -----------------------------
    if len(opponent_history) >= 3:
        if opponent_history[-1] == opponent_history[-2] == opponent_history[-3]:
            return counter(opponent_history[-1])

    # -----------------------------
    # Reactive / Copy Bot Defense
    # -----------------------------
    if len(opponent_history) >= 2:
        if opponent_history[-1] == opponent_history[-2]:
            return counter(opponent_history[-1])

    # -----------------------------
    # Transition Prediction
    # -----------------------------
    if len(opponent_history) >= 5:
        transitions = {"R": [], "P": [], "S": []}

        for i in range(len(opponent_history) - 1):
            transitions[opponent_history[i]].append(opponent_history[i + 1])

        last = opponent_history[-1]
        if transitions[last]:
            predicted = None
            max_freq = -1

            for m in transitions[last]:
                c = transitions[last].count(m)
                if c > max_freq:
                    max_freq = c
                    predicted = m

            return counter(predicted)

    # -----------------------------
    # Smart Random Fallback
    # -----------------------------
    return random.choice(["R", "P", "S", freq_counter])