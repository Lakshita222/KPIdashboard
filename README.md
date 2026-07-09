# KRI Dashboard

A simple Streamlit dashboard for viewing key risk indicators (KRIs), sentiment, and status trends.

## Run locally

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python -m textblob.download_corpora
streamlit run app.py
```

Then open the local URL shown in the terminal, typically http://localhost:8501.

## Deploy to GitHub and Streamlit Community Cloud

1. Initialize Git:

```bash
git init
git add .
git commit -m "Initial commit"
```

2. Create a new repository on GitHub.

3. Connect your local repo:

```bash
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo-name>.git
git push -u origin main
```

4. Deploy from GitHub:
   - Go to https://share.streamlit.io/
   - Sign in with GitHub
   - Click New app
   - Select your GitHub repo, branch, and main file `app.py`
   - Click Deploy

Your app will be available at a Streamlit-hosted URL.
