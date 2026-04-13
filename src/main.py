"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs

def main() -> None:
    songs = load_songs("data/songs.csv")

    profiles = {
        "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.9},
        "Chill Lofi": {"genre": "lofi", "mood": "calm", "energy": 0.2},
        "Deep Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.8},
        "Sad But High Energy": {"genre": "pop", "mood": "sad", "energy": 0.9},
        "Unknown Genre Preference": {"genre": "classical", "mood": "calm", "energy": 0.4}
    }

    for profile_name, user_prefs in profiles.items():
        print("\n" + "=" * 50)
        print(f"PROFILE: {profile_name}")
        print(f"Preferences: {user_prefs}")
        print("=" * 50)

        recommendations = recommend_songs(user_prefs, songs, k=5)

        print("\nTop recommendations:\n")
        for rec in recommendations:
            song, score, explanation = rec
            print(f"{song['title']} by {song['artist']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()

if __name__ == "__main__":
    main()