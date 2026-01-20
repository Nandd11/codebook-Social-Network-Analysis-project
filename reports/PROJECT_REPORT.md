# Project Report - CodeBook Social Network Analysis (Ultimate)

## Objective
Analyze a social network dataset and replicate real platform features such as network insights and recommendations.

## Pipeline
1. **Load Data**: Read raw JSON datasets.
2. **Clean Data**: Normalize schema, remove duplicates, handle missing values.
3. **Build Graph**: Construct an undirected user-user graph using NetworkX.
4. **Compute Metrics**:
   - Degree centrality
   - Betweenness centrality
   - PageRank
   - Connected components
5. **Community Detection**: Greedy modularity communities.
6. **Recommendations**:
   - People You May Know: mutual friends
   - Pages You Might Like: shared interests overlap

## Results / Insights
- Identifies top influential users using graph metrics
- Discovers communities (clusters)
- Generates personalized friend/page recommendations

## Future Enhancements
- Louvain community detection for better clustering
- Evaluation metrics for recommendations
- Flask/Streamlit web demo
