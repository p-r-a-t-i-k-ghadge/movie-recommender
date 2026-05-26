# =============================================================================
#  app.py — Movie Recommendation System · Streamlit Web App
#
#  Setup:
#    pip install streamlit pandas scikit-learn
#    streamlit run app.py
#
#  Files required in same folder:
#    movies.pkl      ← downloaded from Colab Step 10
#    similarity.pkl  ← downloaded from Colab Step 10
# =============================================================================

import streamlit as st
import pickle
import pandas as pd

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="🎬 Movie Recommender",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ── Load pre-computed model artifacts ─────────────────────────────────────────
@st.cache_resource
def load_artifacts():
    """Load pickled model — cached so it only runs once."""
    movies     = pickle.load(open('movies.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    return movies, similarity

movies_df, similarity = load_artifacts()

# ── Recommendation logic ──────────────────────────────────────────────────────
def recommend(title, n=10):
    """Return top-n similar movie titles."""
    matches = movies_df[movies_df['title'].str.lower() == title.lower()]
    if matches.empty:
        return []
    idx    = matches.index[0]
    scores = sorted(enumerate(similarity[idx]), key=lambda x: x[1], reverse=True)[1:n+1]
    return [movies_df.iloc[i[0]]['title'] for i in scores]

# ── UI — Header ───────────────────────────────────────────────────────────────
st.title("🎬 Movie Recommendation System")
st.markdown(
    "**Content-Based Filtering** · TMDB 5000 Movies  \n"
    "Recommendations powered by genres, cast, director & plot keywords."
)

st.divider()

# ── Movie selector ────────────────────────────────────────────────────────────
selected_movie = st.selectbox(
    "🎥 Choose a movie:",
    options=[""] + sorted(movies_df['title'].values.tolist()),
    index=0,
    placeholder="Start typing to search..."
)

# ── Number of recommendations ─────────────────────────────────────────────────
n_recs = st.slider(
    "📋 Number of recommendations",
    min_value=5,
    max_value=20,
    value=10,
    step=1
)

# ── Recommend button ──────────────────────────────────────────────────────────
col1, col2 = st.columns([3, 1])
with col1:
    clicked = st.button("🎯 Get Recommendations", type="primary", use_container_width=True)
with col2:
    st.markdown("")  # spacer

# ── Results ───────────────────────────────────────────────────────────────────
if clicked:
    if not selected_movie or selected_movie == "":
        st.warning("⚠️ Please select a movie first.")
    else:
        recs = recommend(selected_movie, n=n_recs)
        if recs:
            st.success(f"**Top {n_recs} movies similar to '{selected_movie}':**")
            st.divider()

            # Display as numbered list with visual formatting
            for i, title in enumerate(recs, 1):
                col_num, col_title = st.columns([0.08, 0.92])
                with col_num:
                    st.markdown(f"**{i}.**")
                with col_title:
                    st.markdown(title)
        else:
            st.error(f"❌ '{selected_movie}' not found. Try selecting from the dropdown.")

# ── Footer ────────────────────────────────────────────────────────────────────
st.divider()
st.caption(
    "Built with Scikit-learn · CountVectorizer · Cosine Similarity  |  "
    "Dataset: TMDB 5000 Movies  |  "
    "[GitHub Repo](#)"
)
