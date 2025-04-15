# 🎵 Feature-Based Song Mixer using Spotify API

A system that generates a new song by analyzing and mixing top similar songs based on musical features like **tempo**, **acousticness**, and **energy** using data from the **Spotify API**.

---

## 🎯 Project Overview

This project uses audio features of songs to intelligently mix the most similar ones and create a new, coherent song that mimics the musical essence of its source tracks.

---

## 🧠 Key Features

- 🎧 **Chorus Detection**  
  Automatically identifies and extracts the chorus sections from a given list of songs.

- 🔍 **Feature Extraction via Spotify API**  
  Uses Spotify's powerful API to pull in audio features such as:
  - `tempo`
  - `acousticness`
  - `energy`
  - `key`
  - `valence`
  - `danceability`

- 📊 **Similarity Analysis**  
  Computes correlations between songs based on their feature vectors to find the most similar tracks.

- 🎼 **Song Generation**  
  Mixes the chorus segments of the top **‘X’** most similar songs to create a new hybrid song with similar musical characteristics.

---

## 🚀 Technologies Used

- **Python**  
- **Spotify Web API (Spotipy)**  
- **Librosa** – Audio analysis and processing  
- **NumPy / Pandas** – Data manipulation  
- **Scikit-learn** – Similarity and clustering  
- **Matplotlib / Seaborn** – Data visualization (optional)

---

## ⚙️ How It Works

1. **Input Songs**  
   Provide a list of songs via Spotify track IDs or URLs.

2. **Feature Extraction**  
   Retrieve the audio features using Spotify API.

3. **Chorus Identification**  
   Analyze song structure and isolate chorus segments.

4. **Similarity Calculation**  
   Compute similarity scores using cosine similarity or clustering.

5. **Mixing Engine**  
   Extract and combine chorus parts of the top **X** most similar songs into a new audio file.

---

## 🔮 Future Work

- Improve mixing transitions using beat-matching  
- Add support for generating entire tracks (not just chorus)  
- Web-based UI for uploading playlists and previewing mixes  
- Integration with generative AI for music synthesis
