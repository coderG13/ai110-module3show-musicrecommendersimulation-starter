# 🎵 Music Recommender Simulation

## Project Summary

This project simulates a small content-based music recommender system. The goal is to model how recommendation systems turn user preferences into predictions by comparing song features such as genre, mood, and energy with a user's taste profile. The recommender assigns each song a weighted score, ranks the songs from highest to lowest, and returns the top matches.

This project helped me understand how recommendation systems use structured data, scoring logic, and ranking to generate personalized suggestions. It also showed how even a simple system can develop limitations such as repetition, narrow recommendations, and bias toward certain types of songs.

---

## How The System Works
This recommender uses a content-based approach. Instead of learning from many users, it compares each song directly to a single user’s preferences.

### Song Features
Each song includes:
- genre
- mood
- energy
- tempo_bpm
- valence
- danceability
- acousticness

### User Profile
Each user profile stores:
- preferred genre
- preferred mood
- preferred energy level
- optional acoustic preference

### Scoring Rule
The recommender computes a score for each song using weighted matching:
- genre match adds strong points
- mood match adds strong points
- energy gives partial credit based on closeness to the user’s target
- acousticness can add a small bonus depending on preference

### Ranking Rule
After every song is scored:
- the songs are sorted from highest score to lowest score
- the top 5 songs are returned as recommendations

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

To evaluate the recommender, I tested it with multiple user profiles representing different music tastes. These included:

High-Energy Pop
Chill Lofi
Deep Intense Rock
Moody High Energy
Unknown Genre Preference

The first three profiles were used to test clear differences in genre, mood, and energy. The last two profiles were used as edge cases to see how the recommender handled conflicting preferences or missing genres.

The results mostly matched expectations:

The pop profile returned more upbeat songs
The lofi profile returned calmer low-energy songs
The rock profile returned intense rock tracks

The edge-case profiles revealed that the recommender relies heavily on energy when mood conflicts exist or when the preferred genre is not available.


## Screenshots
![image1](images/image1.png)
![image2](images/image2.png)
![image3](images/image3.png)
![image](images/image.png)


---

## Limitations and Risks

The dataset is small and may not represent all music tastes
The system only considers a few features and ignores lyrics, artist popularity, and user history
It may over-recommend one genre if the user strongly prefers it
It does not include collaborative filtering, so it cannot learn from other users
---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

This project helped me understand how recommendation systems turn user preferences into predictions using structured data. I learned how features like genre, mood, and energy are compared with song attributes to generate a score, which is then used to rank songs.

While testing different profiles, I noticed that the system often relied heavily on energy and genre, especially when preferences were conflicting or missing. This showed me how even simple recommender systems can develop bias or become repetitive.

Overall, building this system helped me realize that platforms like Spotify and TikTok are not random. Their recommendations are based on patterns, weights, and data limitations, and they can strongly influence what users discover.