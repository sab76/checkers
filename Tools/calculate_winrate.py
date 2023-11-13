import subprocess

def run_script_and_get_output():
    result = subprocess.run(["python3", "AI_Runner.py", "8", "8", "3", "l", "../src/checkers-python/main.py", "./Sample_AIs/Random_AI/main.py"], capture_output=True, text=True)
    return result.stdout.strip()

def calculate_win_rate():
    player1_wins = 0

    for _ in range(100):
        output = run_script_and_get_output()
        lines = output.split('\n') # Split output into lines
        if lines and ("player 1 wins" in lines[-1] or "Tie" in lines[-1]): # Check last line
            player1_wins += 1

    win_rate = player1_wins / 100
    return win_rate

# Run the win rate calculation
win_rate = calculate_win_rate()
print(f"Player 1 Win Rate: {win_rate * 100}%")
