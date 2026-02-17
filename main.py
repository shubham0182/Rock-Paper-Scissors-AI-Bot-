from RPS_game import play, quincy, abbey, kris, mrugesh
from RPS import player

# -----------------------------
# Manual Testing
# -----------------------------
print("\nTesting against Quincy (random bot)")
play(player, quincy, 1000)

print("\nTesting against Abbey (pattern bot)")
play(player, abbey, 1000)

print("\nTesting against Kris (copy bot)")
play(player, kris, 1000)

print("\nTesting against Mrugesh (frequency bot)")
play(player, mrugesh, 1000)

# -----------------------------
# Run Unit Tests (Optional)
# -----------------------------
# Uncomment the line below to run tests automatically
# from test_module import test
# test()