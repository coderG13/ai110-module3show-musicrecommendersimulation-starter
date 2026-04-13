# 🎧 Model Card: Music Recommender Simulation

---

## Model Name  
**VibeMatch 1.0**

---

## Goal / Task  

The goal of this system is to recommend songs that match a user’s preferences.  
It predicts which songs a user might like based on features such as genre, mood, and energy.

---

## Data Used  

The system uses a small dataset of songs stored in `songs.csv`.  
It contains about 10 songs.

Each song includes features like:
- genre  
- mood  
- energy  
- tempo  
- valence  
- danceability  
- acousticness  

The dataset is limited in size and does not include user history, lyrics, or popularity data.

---

## Algorithm Summary  

This is a content-based recommender.

The system compares each song to the user’s preferences and gives it a score.

- Songs get points if the genre matches  
- Songs get points if the mood matches  
- Songs get partial points if the energy is close to the user’s preference  
- Songs may get a small bonus based on acoustic preference  

After scoring all songs, the system sorts them and returns the top results.

---

## Observed Behavior / Biases  

The system tends to favor genre and energy heavily.

One issue is that songs with high energy can appear in multiple profiles, even when the mood is different. This means energy sometimes dominates mood.

Another limitation is that if a user selects a genre that does not exist in the dataset, the system ignores genre and relies mostly on energy.

Because the dataset is small, the system can repeat similar types of songs, creating a “filter bubble.”

---

## Evaluation Process  

I tested the system using multiple user profiles, including:

- High-Energy Pop  
- Chill Lofi  
- Deep Intense Rock  
- Moody High Energy  
- Unknown Genre Preference  

I ran the recommender in the terminal and observed the top 5 results for each profile.

I also tested an experiment by changing the scoring logic (for example, increasing the importance of energy or removing mood) to see how the results changed.

These tests helped me understand how different features affect the final recommendations.

---

## Intended Use and Non-Intended Use  

### Intended Use  
- Learning how recommendation systems work  
- Demonstrating scoring and ranking logic  
- Simple music suggestion simulation  

### Non-Intended Use  
- Real-world music recommendation systems  
- Personalized streaming platforms like Spotify  
- Decisions based on large-scale user behavior  

---

## Ideas for Improvement  

If I continued this project, I would:

- Add more songs to increase diversity  
- Use more features like tempo, valence, and danceability  
- Improve scoring so results are less repetitive  
- Add collaborative filtering (using other users’ data)  

---

## Personal Reflection  

The biggest thing I learned is that recommendation systems are built from simple rules, but they can still feel very real. Even a basic scoring system can produce results that seem personalized.

Using AI tools helped me generate ideas and structure my code faster, especially when implementing functions and debugging errors. However, I had to double-check the logic to make sure it actually matched my design.

What surprised me the most is how small changes in weights or features can completely change the recommendations. This showed me how sensitive these systems are.

If I extended this project, I would try combining content-based filtering with collaborative filtering to make the recommendations more realistic and diverse.