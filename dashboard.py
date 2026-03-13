import fastf1
import pandas as pd
import os

if not os.path.exists('cache'):
    os.makedirs('cache')

fastf1.Cache.enable_cache('cache') 

print("System Ready: F1 Cache Enabled.")

ergast = fastf1.ergast.Ergast()

def get_driver_dashboard(driver_id):


    # LOADING THE DATA AND SAVING IT

    print(f"Fetching data for: {driver_id}...")
    results = ergast.get_race_results(driver = driver_id, limit = 1000)
    if not results.content:
        print(f"""Error: No data found for '{driver_id}'. Check the spelling!
              NOTE: Driver id is usually lowercase last name (e.g., 'hamilton', 'verstappen')""")
        return
    df = pd.concat(results.content)


    # ANALYSIS OF DATA
    total_races = len(df)
    wins = len(df[df['position'] == 1])
    podiums = len(df[df['position'] <= 3])
    total_points = df['points'].sum()
    avg_finish = df['position'].mean()


    print("-" * 30)
    print(f" {driver_id.upper()}'s CAREER DASHBOARD")
    print("-" * 30)
    print(f"Starts:       {total_races}")
    print(f"Wins:         {wins}")
    print(f"Podiums:      {podiums}")
    print(f"Total Points: {total_points}")
    print(f"Avg Position: {avg_finish:.3f}")
    print("-" * 30)

# --- EXECUTION ---
if __name__ == "__main__":
    user_input = input("Enter Driver ID (last name): ").lower().strip()
    get_driver_dashboard(user_input)
