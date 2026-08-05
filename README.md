# 🎬 Movie Recommendation System

A **Content-Based Movie Recommendation System** built using **Python**, **Pandas**, **Scikit-learn**, and **Streamlit**. The system recommends movies similar to a user's selected movie by analyzing movie metadata such as genres, keywords, cast, crew, and overview using Natural Language Processing (NLP) techniques.

---

# 📌 Overview

The project aims to help users discover movies similar to the ones they already enjoy. Instead of relying on user ratings, it recommends movies based on their content.

The recommendation engine uses **CountVectorizer** to convert movie metadata into numerical vectors and **Cosine Similarity** to identify movies with similar characteristics.

---

# 🚀 Features

* Content-based movie recommendation
* Interactive Streamlit web interface
* Fast recommendations using a precomputed similarity matrix
* Simple and user-friendly movie selection
* Real-time top 5 movie recommendations

---

# 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* Streamlit
* Pickle

---

# 📂 Dataset

The project uses the **TMDB 5000 Movie Dataset** consisting of:

* `tmdb_5000_movies.csv`
* `tmdb_5000_credits.csv`

The datasets were merged using the common **title** column to create a unified dataset.

---

# ⚙️ Data Preprocessing

The following preprocessing pipeline was implemented:

* Loaded movie and credits datasets
* Merged datasets using the movie title
* Selected important features:

  * Movie ID
  * Title
  * Overview
  * Genres
  * Keywords
  * Cast
  * Crew
* Removed missing values
* Converted JSON-like strings into Python objects using `ast.literal_eval()`
* Extracted:

  * Genre names
  * Keyword names
  * Top three cast members
  * Director name
* Removed spaces from names
* Combined all important textual information into a single **tags** column
* Converted all text to lowercase
* Applied Porter Stemming using NLTK

---

# 🧠 Recommendation Pipeline

1. Convert movie tags into numerical vectors using **CountVectorizer**.
2. Generate feature vectors with the top 5000 words.
3. Compute cosine similarity between all movies.
4. Store the processed dataset and similarity matrix using Pickle.
5. Load the processed files in the Streamlit application.
6. Recommend the five most similar movies based on cosine similarity.

---

# 💻 Streamlit Application

The web application allows users to:

* Select a movie from the dropdown menu.
* Generate recommendations with a single click.
* View the top five most similar movies instantly.

---

## 📁 Project Structure

```text
Movie-Recommendation-System/
│
├── app.py
├── preprocessing.ipynb
├── requirements.txt
├── README.md
├── .gitignore
├── LICENSE
└── assets/
    └── screenshot.png
```
---

# ▶️ Installation

Clone the repository:
Download the TMDB 5000 Movie Dataset and place the following files in the project root:

- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`
  https://www.kaggle.com/datasets/ahsanaseer/top-rated-tmdb-movies-10k?fbclid=IwAR2MpWrWpcw2QNCv_FZg2l0sjBh9xAvhrqtnZBO9K-QS6PHI1aHkdB6qLa0 download these data set from this site 

Run the preprocessing notebook to generate the required pickle files:

```bash
jupyter notebook preprocessing.ipynb
```

After generating `movies.pkl` and `similarity.pkl`, start the website:

```bash
streamlit run app.py
```

```bash
git clone https://github.com/priyanka12324/movie-recommendation-system2
```

Move to the project folder:

```bash
cd Movie-Recommendation-System2
```

Install dependencies:

```bash
pip install -r requirements.txt
```

 Run the website locally:
 streamlit run app.py

```bash
streamlit run app.py
```

---
## 📂 Dataset

This project uses the **TMDB 5000 Movie Dataset**.

Due to GitHub's browser upload size limitations, the dataset files are **not included** in this repository.

Download the following files separately and place them in the project root before running the preprocessing notebook:

- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`
- https://www.kaggle.com/datasets/ahsanaseer/top-rated-tmdb-movies-10k?fbclid=IwAR2MpWrWpcw2QNCv_FZg2l0sjBh9xAvhrqtnZBO9K-QS6PHI1aHkdB6qLa0

Running `preprocessing.ipynb` will generate:

- `movies.pkl`
- `similarity.pkl`

These files are required to run the Streamlit web application.

# 📸 Application Screenshot

Add your Streamlit application screenshot here.

```
Movie-Recommendation-System2\assets\movie_screenshot.png
```

---

# 🔮 Future Improvements

* Display movie posters using the TMDB API.
* Add movie descriptions and ratings.
* Integrate movie trailers.
* Improve recommendations using TF-IDF or transformer embeddings.
* Deploy the application online using Streamlit Community Cloud.

---

# 📖 What I Learned

* Data preprocessing using Pandas
* Feature engineering
* Natural Language Processing (NLP)
* Content-based recommendation systems
* Cosine similarity
* Streamlit web application development
* Git and GitHub version control

---

# 👨‍💻 Author
**Priyanka Rawat**
GitHub:https://github.com/priyanka12324

## note 
