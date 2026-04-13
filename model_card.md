# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeMatch 1.0**

---

## 2. Intended Use  

This model recommends songs based on a user’s preferences such as genre, mood, and energy. It is designed for classroom learning purposes to simulate how recommendation systems work, not for real-world deployment.

---

## 3. How the Model Works  

The model compares each song’s features with the user’s preferences. It looks at attributes like genre, mood, energy, and tempo. Songs that match the user’s favorite genre and mood receive higher scores. For numerical features like energy, songs closer to the user’s preferred value receive better scores.

All features are combined into a weighted score, and songs are ranked from highest to lowest to generate recommendations.

---

## 4. Data  

The dataset contains a small collection of songs with attributes such as genre, mood, energy, tempo, valence, danceability, and acousticness.

The dataset is limited and does not cover all music styles or user preferences, which may affect recommendation quality. 

---

## 5. Strengths  

- Works well for users with clear preferences (e.g., pop + happy songs)
- Easy to understand and explain
- Produces consistent and predictable recommendations

---

## 6. Limitations and Bias 

- Does not consider user listening history
- May over-recommend one genre or mood
- Dataset may not represent diverse music tastes
- Cannot capture complex or changing preferences 

---

## 7. Evaluation  

The model was tested using different user profiles with varying preferences. The recommendations were evaluated based on whether the top results matched the expected vibe. In most cases, songs with similar genre and mood appeared at the top.

---

## 8. Future Work  

- Add more features such as artist popularity or lyrics
- Include collaborative filtering using multiple users
- Improve diversity in recommendations
- Add explanation transparency for each recommendation 

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
