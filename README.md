# 🎬 Movie Recommendation System

Content-Based Filtering using the TMDB 5000 Movies dataset.  
Recommends **10 similar movies** for any input title based on genres, cast, director, and plot keywords.

---

## 🗂️ Project Structure

```text
movie-recommender/
├── Movie_Recommendation_System.ipynb   ← Complete Colab notebook
├── app.py                              ← Streamlit web app
├── requirements.txt                    ← Python dependencies
├── .gitignore
└── README.md
```

> **Note:** `movies.pkl`, `similarity.pkl`, and the CSV datasets are not included  
> because `similarity.pkl` is too large for GitHub upload limits.  
> Generate them by running the notebook — Step 10 will create/download them automatically.

---

## 🚀 Quick Start

### Option A — Run in Google Colab (Recommended)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/p-r-a-t-i-k-ghadge/movie-recommender/blob/main/Movie_Recommendation_System.ipynb)

1. Upload your Kaggle API token (`kaggle.json`) in Step 0
2. Run all notebook cells — dataset downloads automatically
3. Get recommendations in the interactive widget (Step 9)

---

### Option B — Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/p-r-a-t-i-k-ghadge/movie-recommender.git
cd movie-recommender

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the notebook to generate pickle files
jupyter notebook Movie_Recommendation_System.ipynb

# 4. Launch the web app
streamlit run app.py
```

---

## 🔧 Tech Stack

| Library | Purpose |
|---|---|
| `pandas` | Data loading and manipulation |
| `numpy` | Numerical operations |
| `scikit-learn` | CountVectorizer + Cosine Similarity |
| `nltk` | Porter Stemmer for text normalization |
| `streamlit` | Web app deployment |

---

## 🧠 How It Works

```text
Load CSVs → Merge → Feature Engineering → Preprocess → Vectorize → Similarity → Recommend
```

1. **Load & Merge** — combines `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`
2. **Feature Engineering** — extracts genres, top-3 cast, director, keywords from JSON columns
3. **Preprocessing** — collapses multi-word names, lowercases, applies Porter Stemming
4. **Count Vectorization** — builds 4803 × 5000 sparse word-count matrix
5. **Cosine Similarity** — computes 4803 × 4803 pairwise similarity matrix
6. **Recommend** — sorts by similarity score, returns top-10 titles

---

## 🧪 Example Recommendations

```text
Because you liked: The Dark Knight

1. The Dark Knight Rises
2. Batman Begins
3. Batman
4. Superman Returns
5. Man of Steel
...
```

---

## 🌐 Deploy to Streamlit Cloud (Free)

1. Push this repo to GitHub
2. Go to https://share.streamlit.io
3. Connect your GitHub repo
4. Set **Main file path** to `app.py`
5. Click **Deploy** — live in ~2 minutes

> ⚠️ `similarity.pkl` can exceed GitHub's file size limit because it stores the full cosine similarity matrix.  
> For cloud deployment, either:
> - generate the file locally,
> - use Git LFS,
> - or optimize the similarity storage format.

---

## 📊 Dataset

Dataset: **TMDB 5000 Movies** from Kaggle

Source:  
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

Required files:
- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

The notebook downloads them automatically using your Kaggle API token (`kaggle.json`).

---

## 📄 License

MIT License — free to use, modify, and distribute.
