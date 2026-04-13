# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeMatch 1.0**

---

## 2. Intended Use  

This recommender is designed to generate song suggestions from a small song catalog based on a user’s preferences, such as genre, mood, energy, and acoustic style. It is intended for classroom exploration and learning, not for real-world deployment.

The model assumes that a user’s taste can be represented using a few fixed features and that songs with similar attributes will be more relevant to that user.

---

## 3. How the Model Works  

This is a content-based recommender. It looks at features of each song and compares them to features in a user profile.

The main song features used are:
- genre
- mood
- energy
- acousticness

The user profile stores:
- favorite genre
- favorite mood
- target energy level
- whether the user prefers acoustic music

Each song receives a weighted score. Matching genre and mood receive strong points, while energy contributes partial credit depending on how close the song is to the user’s preferred energy level. Acousticness adds a smaller bonus depending on whether the user likes acoustic songs. After all songs are scored, they are ranked from highest to lowest and the top results are recommended.

---

## 4. Data  

The dataset is a small song catalog stored in `songs.csv`. It includes song-level attributes such as title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness.

The dataset includes genres such as pop, lofi, rock, ambient, jazz, synthwave, and indie pop, and moods such as happy, chill, intense, relaxed, moody, and focused.

This is a limited dataset and does not represent the full range of musical taste. It also does not include listening history, lyrics, or cultural context.

---

## 5. Strengths  

This recommender works well for users who have clear and simple preferences, such as wanting energetic pop songs or chill lofi songs. It is also easy to understand because the scoring logic is transparent and explainable.

In testing, the output usually matched the expected vibe of the profile. For example, rock profiles produced more intense rock songs, while lofi profiles returned calmer, lower-energy songs.

---

## 6. Limitations and Bias

One weakness I discovered is that the recommender can over-prioritize genre and energy when those features have strong weights. This causes some songs to appear in more than one profile, even when the users are meant to be different.

The system also struggles with conflicting preferences. For example, the “Sad But High Energy” profile mostly returned energetic songs, which suggests that the high-energy preference had more influence than mood. Another limitation is that if the preferred genre is missing from the dataset, the system falls back mostly to energy-based matching, which may not feel musically accurate.

Because the dataset is small, the recommender can easily create a filter bubble by repeatedly suggesting songs with very similar characteristics.

---

## 7. Evaluation  

I tested the model using five user profiles:
- High-Energy Pop
- Chill Lofi
- Deep Intense Rock
- Sad But High Energy
- Unknown Genre Preference

I checked whether the top recommendations matched the expected vibe of each profile. In most cases, the results made sense. High-Energy Pop ranked upbeat pop songs highly, Chill Lofi returned low-energy lofi tracks, and Deep Intense Rock ranked intense rock songs near the top.

What surprised me most was how much the system depended on energy when a profile had conflicting preferences or when the requested genre was not present in the dataset. This showed that the scoring rule was reasonable, but also somewhat narrow.

---

## 8. Future Work  

If I continued this project, I would improve it by:
- adding more songs and a more diverse dataset
- supporting more detailed user preferences
- using tempo, valence, and danceability more directly in scoring
- improving diversity so the top results are not too repetitive
- adding better explanation features for why each song was recommended
- exploring collaborative filtering instead of relying only on content-based matching


---

## 9. Personal Reflection  

This project helped me understand that recommendation systems are not magic. They are built from data, feature choices, scoring rules, and ranking logic. Even a small system can feel convincing when the features align well with user expectations.

At the same time, building this made me more aware of bias and oversimplification. A recommender can seem accurate while still ignoring important parts of human taste. That made me think more critically about how apps like Spotify or TikTok shape what people hear and discover.