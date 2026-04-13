from typing import List, Dict, Tuple
from dataclasses import dataclass
import csv


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        scored_songs = []

        for song in self.songs:
            score = 0.0

            if song.genre.lower() == user.favorite_genre.lower():
                score += 0.4

            if song.mood.lower() == user.favorite_mood.lower():
                score += 0.3

            energy_score = 1 - abs(song.energy - user.target_energy)
            energy_score = max(0.0, energy_score)
            score += 0.2 * energy_score

            if user.likes_acoustic:
                score += 0.1 * song.acousticness
            else:
                score += 0.1 * (1 - song.acousticness)

            scored_songs.append((score, song))

        scored_songs.sort(key=lambda x: x[0], reverse=True)
        return [song for score, song in scored_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        reasons = []

        if song.genre.lower() == user.favorite_genre.lower():
            reasons.append("genre matches")

        if song.mood.lower() == user.favorite_mood.lower():
            reasons.append("mood matches")

        if abs(song.energy - user.target_energy) <= 0.15:
            reasons.append("energy is close to your preference")

        if user.likes_acoustic and song.acousticness >= 0.6:
            reasons.append("it has an acoustic feel")
        elif not user.likes_acoustic and song.acousticness <= 0.4:
            reasons.append("it is less acoustic")

        if not reasons:
            return "It is a moderate overall match."

        return ", ".join(reasons).capitalize() + "."


def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs = []

    with open(csv_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }
            songs.append(song)

    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons = []

    # Weights
    genre_weight = 0.35
    mood_weight = 0.30
    energy_weight = 0.20
    acoustic_weight = 0.15

    # Genre match
    if song["genre"].lower() == user_prefs["genre"].lower():
        score += genre_weight
        reasons.append("genre matches")

    # Mood match
    if song["mood"].lower() == user_prefs["mood"].lower():
        score += mood_weight
        reasons.append("mood matches")

    # Energy closeness
    energy_gap = abs(song["energy"] - user_prefs["energy"])
    energy_score = 1 - energy_gap
    energy_score = max(0.0, energy_score)
    score += energy_weight * energy_score

    if energy_gap <= 0.15:
        reasons.append("energy is very close")
    elif energy_gap <= 0.30:
        reasons.append("energy is somewhat close")

    # Optional acoustic preference
    if "likes_acoustic" in user_prefs:
        if user_prefs["likes_acoustic"]:
            score += acoustic_weight * song["acousticness"]
            if song["acousticness"] >= 0.6:
                reasons.append("fits acoustic preference")
        else:
            score += acoustic_weight * (1 - song["acousticness"])
            if song["acousticness"] <= 0.4:
                reasons.append("fits non-acoustic preference")

    return score, reasons


def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5
) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored_results = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons) if reasons else "general match"
        scored_results.append((song, score, explanation))

    scored_results.sort(key=lambda x: x[1], reverse=True)
    return scored_results[:k]