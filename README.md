# CodeBook Social Network Analysis (SNA) + Recommendation System (Python)

A complete **Social Network Analysis + Recommendation System** project built in Python.  
This repository is designed as a **CV/portfolio-ready** data science project with:

- ✅ Data cleaning pipeline (raw JSON → cleaned dataset)
- ✅ Social Network Analysis (graph metrics + community detection)
- ✅ Visualizations (network graphs, degree distributions)
- ✅ Two recommendation systems:
  - **People You May Know**
  - **Pages You Might Like**
- ✅ Reproducible script (`main.py`) + modular `src/` code + notebooks

> Built by **Nand Patel**.

---

## 🌟 Key Modules

### 1) Data Cleaning
- Load raw JSON datasets
- Normalize schema (id, name, friends, pages)
- Handle duplicates + missing values
- Export cleaned dataset

### 2) Social Network Analysis (NetworkX)
- ✅ Louvain community detection (python-louvain)
- Build user-user graph
- Metrics:
  - Degree centrality
  - Betweenness centrality
  - PageRank
  - Connected components
- Community detection (greedy modularity)

### 3) Recommendation Systems
#### People You May Know
- Mutual friend based friend suggestions (ranked)

#### Pages You Might Like
- Interest overlap recommendations (ranked)

---

## 🛠 Tech Stack
- Python 3
- pandas
- networkx
- matplotlib
- Jupyter Notebook

---

## 📂 Project Structure
```txt
CodeBook-Social-Network-Analysis/
│── main.py
│── src/
│   ├── data_loader.py
│   ├── cleaning.py
│   ├── graph_builder.py
│   ├── sna_metrics.py
│   ├── community.py
│   ├── recommender_people.py
│   ├── recommender_pages.py
│   └── utils.py
│── notebooks/
│   ├── 01_introduction.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_people_you_may_know.ipynb
│   ├── 04_pages_you_might_like.ipynb
│   └── 05_networkx_sna_visuals.ipynb
│── data/
│   ├── data.json
│   ├── data2.json
│   ├── massive_data.json
│   └── cleaned_data.json
│── assets/                 # charts/plots (exported)
│── reports/
│   └── PROJECT_REPORT.md
│── FEATURES.md
│── requirements.txt
│── .gitignore
│── LICENSE
│── README.md
```

---

## ⚙️ Installation
```bash
git clone https://github.com/Nandd11/CodeBook-Social-Network-Analysis.git
cd CodeBook-Social-Network-Analysis
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## 📊 Visual Outputs
Running the pipeline will also generate plots in the `assets/` folder:
- `degree_distribution.png`
- `graph.png` (only for small graphs)
- `community_graph_louvain.png` (colored Louvain communities)

## ▶️ Run Full Pipeline
```bash
python main.py
```

This will:
1) Clean raw data → `data/cleaned_data.json`
2) Build NetworkX graph + compute metrics
3) Print top influencers
4) Detect communities
5) Print recommendations

---

## ✅ Resume Bullet Points
- Built a Python Social Network Analysis project using NetworkX to compute centrality metrics, PageRank, and community detection on user connection graphs
- Developed recommendation engines for friend suggestions and page recommendations based on mutual connections and shared interests
- Designed a portfolio-ready repository with reusable modules, notebooks, and reproducible scripts

---

## 👤 Author
**Nand Patel**  
GitHub: https://github.com/Nandd11
