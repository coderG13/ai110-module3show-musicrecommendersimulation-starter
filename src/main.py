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
        "High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.9,
            "likes_acoustic": False
        },
        "Chill Lofi": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.2,
            "likes_acoustic": True
        },
        "Deep Intense Rock": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.8,
            "likes_acoustic": False
        },
        "Moody High Energy": {
            "genre": "pop",
            "mood": "moody",
            "energy": 0.9,
            "likes_acoustic": False
        },
        "Unknown Genre Preference": {
            "genre": "classical",
            "mood": "chill",
            "energy": 0.4,
            "likes_acoustic": True
        }
    }

    print(f"Loaded songs: {len(songs)}")

    for profile_name, user_prefs in profiles.items():
        print("\n" + "=" * 55)
        print(f"PROFILE: {profile_name}")
        print(f"Preferences: {user_prefs}")
        print("=" * 55)

        recommendations = recommend_songs(user_prefs, songs, k=5)

        print("\nTop recommendations:\n")
        for song, score, explanation in recommendations:
            print(f"{song['title']} by {song['artist']}")
            print(f"Score: {score:.2f}")
            print(f"Reasons: {explanation}")
            print("-" * 40)

if __name__ == "__main__":
    main()