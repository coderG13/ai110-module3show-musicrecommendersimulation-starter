# 🎵 Music Recommender Simulation

## Project Summary

This project simulates a basic music recommender system similar to platforms like Spotify or TikTok. The system takes a user's music preferences (such as genre, mood, and energy) and compares them with song attributes from a dataset. It then assigns a score to each song based on how closely it matches the user's taste and recommends the top results.

The goal is to understand how real-world recommendation systems transform data into predictions using features, scoring rules, and ranking algorithms.

---

## How The System Works

This recommender system is a simple content-based model that suggests songs based on how similar they are to a user’s preferences.

### Song Features
Each song in the dataset has attributes such as:
- genre
- mood
- energy
- tempo_bpm
- valence
- danceability
- acousticness

### User Profile
The user profile includes:
- favorite genre
- favorite mood
- preferred energy level
- whether they like acoustic songs

### Scoring Rule
Each song is compared to the user profile and given a score:
- Songs with matching genre and mood get higher scores
- Songs with energy close to the user's preference score higher
- Additional features like tempo and acousticness help refine the score

### Ranking Rule
After scoring all songs:
- Songs are sorted from highest to lowest score
- The top K songs are recommended

This simulates how real-world systems rank content based on relevance.

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

- Tested different weights for genre and mood to see which influenced recommendations more
- Observed how changing energy preference affected results
- Compared recommendations for different user profiles (e.g., high-energy vs chill users)

---

## Limitations and Risks

- The dataset is small and may not represent all music tastes
- The system only considers a few features and ignores lyrics, artist popularity, and user history
- It may over-recommend one genre if the user strongly prefers it
- It does not include collaborative filtering, so it cannot learn from other users

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

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

