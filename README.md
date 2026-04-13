# 🎵 Music Recommender Simulation

## Project Summary

This project simulates a content-based music recommender system. The goal is to understand how recommendation systems turn user preferences into predictions by comparing song features such as genre, mood, and energy.

The system assigns each song a weighted score, ranks all songs, and returns the top recommendations. This project helped me understand how simple algorithms can still create meaningful and personalized suggestions.


---

## How The System Works
This recommender uses a content-based approach. It compares each song directly with a user’s preferences.

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
Each user profile includes:
- preferred genre  
- preferred mood  
- target energy level  
- acoustic preference


## Scoring Logic

Each song is scored based on how well it matches the user:

- Genre match → high points  
- Mood match → high points  
- Energy → partial points based on closeness  
- Acoustic preference → small bonus  

After scoring:
- Songs are sorted from highest to lowest  
- Top 5 songs are returned

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

I tested the recommender using multiple user profiles:

High-Energy Pop
Chill Lofi
Deep Intense Rock
Moody High Energy
Unknown Genre Preference
Observations
High-Energy Pop → returned energetic pop songs
Chill Lofi → returned calm, low-energy songs
Deep Intense Rock → returned intense rock songs
Edge Cases
Moody High Energy → energy dominated over mood
Unknown Genre → system relied mostly on energy
Experiment

I modified the scoring logic (e.g., increasing energy weight or removing mood).

Result:

Recommendations changed significantly
The system is sensitive to feature weights
Over-weighting one feature reduces balance

## Screenshots
![image1](images/image1.png)
![image2](images/image2.png)
![image3](images/image3.png)
![image](images/image.png)
![image11](images/image11.png)
![image12](images/image12.png)
![image13](images/image13.png)
![image14](images/image14.png)


---

## Limitations and Risks

Small dataset (~10 songs)
Limited features (no lyrics, popularity, or user history)
Can repeat similar songs across profiles
Struggles with conflicting preferences
Can create “filter bubbles”


---

## Reflection

This project helped me understand how recommendation systems turn user preferences into predictions using structured data and simple scoring rules.

I learned that even basic algorithms can feel realistic, but they are highly sensitive to the features and weights used. Small changes in scoring logic can completely change recommendations.

Using AI tools helped me generate ideas and debug code faster, but I had to verify the logic to make sure it matched my intended design.

What surprised me most is how simple systems can still produce convincing recommendations. If I extended this project, I would explore using more data and combining content-based filtering with collaborative filtering.


---

## 7. Model Card

For a detailed explanation, see:

[**Model Card**](model_card.md)