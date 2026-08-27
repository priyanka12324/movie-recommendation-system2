import html
import pickle
from pathlib import Path

import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


st.set_page_config(
    page_title="CineMatch | Movie Recommendations",
    page_icon="🎬",
    layout="wide",
)

st.markdown(
    """
    <style>
        .stApp {
            background:
                radial-gradient(circle at 10% 10%, rgba(229, 9, 20, 0.16), transparent 28%),
                radial-gradient(circle at 90% 20%, rgba(120, 55, 255, 0.14), transparent 26%),
                #080b12;
            color: #f8fafc;
        }
        [data-testid="stHeader"] { background: transparent; }
        [data-testid="stSidebar"] { background: #0f1420; }
        .block-container {
            max-width: 1180px;
            padding-top: 2.5rem;
            padding-bottom: 3rem;
        }
        .hero {
            text-align: center;
            padding: 2.3rem 1rem 1.6rem;
        }
        .hero-badge {
            display: inline-block;
            padding: .35rem .8rem;
            border: 1px solid rgba(255,255,255,.16);
            border-radius: 999px;
            color: #cbd5e1;
            font-size: .82rem;
            letter-spacing: .08em;
            text-transform: uppercase;
        }
        .hero h1 {
            margin: .8rem 0 .45rem;
            font-size: clamp(2.5rem, 7vw, 5rem);
            line-height: 1;
            background: linear-gradient(90deg, #ffffff, #ff5864);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .hero p {
            max-width: 650px;
            margin: 0 auto;
            color: #aab3c2;
            font-size: 1.05rem;
        }
        .search-panel {
            max-width: 850px;
            margin: .7rem auto 2rem;
            padding: 1.15rem 1.3rem .45rem;
            border: 1px solid rgba(255,255,255,.10);
            border-radius: 18px;
            background: rgba(17, 23, 36, .82);
            box-shadow: 0 20px 60px rgba(0,0,0,.24);
        }
        .section-title {
            margin: 2rem 0 1rem;
            font-size: 1.55rem;
            font-weight: 750;
        }
        .movie-card {
            min-height: 175px;
            padding: 1.15rem;
            border: 1px solid rgba(255,255,255,.10);
            border-radius: 16px;
            background: linear-gradient(145deg, rgba(28,35,52,.96), rgba(14,18,29,.96));
            box-shadow: 0 12px 30px rgba(0,0,0,.20);
        }
        .movie-card:hover {
            transform: translateY(-4px);
            border-color: rgba(255,88,100,.55);
            transition: .2s ease;
        }
        .rank {
            width: 2.1rem;
            height: 2.1rem;
            display: grid;
            place-items: center;
            border-radius: 50%;
            background: #e50914;
            color: white;
            font-weight: 800;
            margin-bottom: 1.2rem;
        }
        .movie-title {
            font-size: 1.05rem;
            line-height: 1.35;
            font-weight: 700;
            color: #f8fafc;
        }
        .movie-label {
            margin-top: .45rem;
            color: #8792a6;
            font-size: .82rem;
        }
        .footer {
            text-align: center;
            color: #6f7b8f;
            margin-top: 3rem;
            font-size: .88rem;
        }
        div.stButton > button {
            width: 100%;
            border: 0;
            border-radius: 10px;
            background: linear-gradient(90deg, #e50914, #ff4655);
            color: white;
            font-weight: 750;
            padding: .68rem 1rem;
        }
        div.stButton > button:hover {
            color: white;
            border: 0;
            box-shadow: 0 8px 24px rgba(229,9,20,.30);
        }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data(show_spinner=False)
def load_movies():
    data_path = Path(__file__).with_name("movies.pkl")
    if not data_path.exists():
        raise FileNotFoundError("movies.pkl was not found in the project folder.")

    with data_path.open("rb") as file:
        movies_data = pickle.load(file)

    frame = pd.DataFrame(movies_data).reset_index(drop=True)
    if "title" not in frame.columns:
        raise ValueError("The saved movie data must contain a 'title' column.")
    return frame


@st.cache_resource(show_spinner=False)
def build_feature_matrix(tags):
    vectorizer = CountVectorizer(max_features=5000, stop_words="english")
    return vectorizer.fit_transform(tags)


def recommend(selected_title, movies, feature_matrix, limit=5):
    selected_index = movies.index[movies["title"] == selected_title][0]
    scores = cosine_similarity(
        feature_matrix[selected_index],
        feature_matrix,
    ).ravel()

    ranked_indices = scores.argsort()[::-1]
    ranked_indices = [index for index in ranked_indices if index != selected_index]
    return movies.iloc[ranked_indices[:limit]]["title"].tolist()


st.markdown(
    """
    <section class="hero">
        <span class="hero-badge">AI-powered discovery</span>
        <h1>CineMatch</h1>
        <p>Choose a movie you love and instantly discover five similar titles
        selected using content-based machine learning.</p>
    </section>
    """,
    unsafe_allow_html=True,
)

try:
    movies_df = load_movies()

    if "tags" not in movies_df.columns:
        st.error(
            "The movie data does not contain the required 'tags' column. "
            "Please regenerate movies.pkl using preprocessing.ipynb."
        )
        st.stop()

    movie_tags = movies_df["tags"].fillna("").astype(str).tolist()
    features = build_feature_matrix(movie_tags)
    movie_titles = sorted(movies_df["title"].dropna().astype(str).unique())

    st.markdown('<div class="search-panel">', unsafe_allow_html=True)
    selected_movie = st.selectbox(
        "What movie did you enjoy?",
        movie_titles,
        index=None,
        placeholder="Search or select a movie...",
    )
    find_movies = st.button(
        "Find Similar Movies",
        type="primary",
        disabled=selected_movie is None,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    if find_movies and selected_movie:
        with st.spinner("Finding your perfect matches..."):
            recommendations = recommend(
                selected_movie,
                movies_df,
                features,
            )

        st.markdown(
            f'<div class="section-title">Because you liked “{html.escape(selected_movie)}”</div>',
            unsafe_allow_html=True,
        )

        columns = st.columns(5)
        for rank, (column, title) in enumerate(
            zip(columns, recommendations),
            start=1,
        ):
            with column:
                st.markdown(
                    f"""
                    <article class="movie-card">
                        <div class="rank">{rank}</div>
                        <div class="movie-title">{html.escape(str(title))}</div>
                        <div class="movie-label">Recommended for you</div>
                    </article>
                    """,
                    unsafe_allow_html=True,
                )
    else:
        st.info("Select a movie above to generate your recommendations.")

    st.markdown(
        """
        <div class="footer">
            Built by Priyanka Rawat · Python · Scikit-learn · Streamlit
        </div>
        """,
        unsafe_allow_html=True,
    )

except (FileNotFoundError, ValueError, KeyError, IndexError) as error:
    st.error(f"Unable to start the recommender: {error}")
    st.caption(
        "Make sure movies.pkl is available and was generated by preprocessing.ipynb."
    )
