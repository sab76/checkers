import subprocess
import concurrent.futures

def run_script_and_get_output():
    result = subprocess.run(["python3", "AI_Runner.py", "8", "8", "3", "l", "../src/checkers-python/main.py", "./Sample_AIs/Random_AI/main.py"], capture_output=True, text=True)
    return result.stdout.strip()

def calculate_win_rate():
    player1_wins = 0
    total_games = 100

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit all games to be run in parallel
        futures = [executor.submit(run_script_and_get_output) for _ in range(total_games)]

        for future in concurrent.futures.as_completed(futures):
            output = future.result()
            lines = output.split('\n')
            if lines and ("player 1 wins" in lines[-1] or "Tie" in lines[-1]):
                player1_wins += 1

    win_rate = player1_wins / total_games
    return win_rate

# Run the win rate calculation
win_rate = calculate_win_rate()
print(f"Player 1 Win Rate: {win_rate * 100}%")
