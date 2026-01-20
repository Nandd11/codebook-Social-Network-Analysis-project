from pathlib import Path
import matplotlib.pyplot as plt
import networkx as nx

from src.data_loader import load_datasets
from src.cleaning import normalize_users
from src.utils import write_json
from src.graph_builder import build_graph
from src.sna_metrics import compute_metrics, top_n
from src.community import detect_communities
from src.louvain import detect_communities_louvain, communities_summary
from src.recommender_people import people_you_may_know
from src.recommender_pages import pages_you_might_like

def main():
    data_dir = Path("data")
    datasets = load_datasets(data_dir)
    if not datasets:
        print("❌ No data files found inside ./data")
        return

    users=[]
    for d in datasets:
        users.extend(normalize_users(d))

    cleaned_path = data_dir / "cleaned_data.json"
    write_json(cleaned_path, users)

    print(f"Loaded datasets: {len(datasets)}")
    print(f"Cleaned users: {len(users)}")
    if not users:
        return

    # Build graph
    G = build_graph(users)
    print(f"Graph nodes: {G.number_of_nodes()} | edges: {G.number_of_edges()}")

    metrics = compute_metrics(G)

    # Top influencers
    print("\n🏆 Top Influencers (Degree Centrality)")
    for i,(uid,score) in enumerate(top_n(metrics['degree_centrality'], 5),1):
        print(f"{i}) {uid}: {score:.4f}")

    print("\n🏆 Top Influencers (PageRank)")
    for i,(uid,score) in enumerate(top_n(metrics['pagerank'], 5),1):
        print(f"{i}) {uid}: {score:.6f}")

    # Communities
    comms = detect_communities(G)
    print(f"\n👥 Communities found: {len(comms)}")
    for i,c in enumerate(comms[:3],1):
        print(f"- Community {i}: size {len(c)}")

    # Louvain communities (advanced)
    try:
        partition = detect_communities_louvain(G)
        summary = communities_summary(partition)
        print(f"\n🧩 Louvain Communities found: {len(summary)}")
        for cid, size in summary[:5]:
            print(f"- Community {cid}: size {size}")

        # Save community-colored graph (small graphs only)
        try:
            if G.number_of_nodes() <= 200:
                import matplotlib.pyplot as plt
                import networkx as nx
                from collections import defaultdict

                assets_dir = Path("assets")
                assets_dir.mkdir(exist_ok=True)

                pos = nx.spring_layout(G, seed=42)

                # group nodes by community id
                comm_nodes = defaultdict(list)
                for node, cid in partition.items():
                    comm_nodes[cid].append(node)

                plt.figure(figsize=(9,7))
                for cid, nodes in comm_nodes.items():
                    nx.draw_networkx_nodes(G, pos, nodelist=nodes, node_size=90)
                nx.draw_networkx_edges(G, pos, alpha=0.35, width=0.8)
                plt.title("Louvain Communities (Colored)")
                plt.axis("off")
                plt.tight_layout()
                plt.savefig(assets_dir / "community_graph_louvain.png")
                plt.close()
        except Exception:
            pass
    except Exception as e:
        print("\nℹ️ Louvain community detection skipped (install python-louvain to enable).")

    # Recommendations
    target_id = users[0]['id']
    print(f"\n🎯 Target user: {target_id} ({users[0]['name']})")

    print("\n🤝 People You May Know (Top 5):")
    for i,(uid,score) in enumerate(people_you_may_know(users, target_id, 5),1):
        print(f"{i}) {uid} (mutual friends: {score})")

    print("\n📄 Pages You Might Like (Top 5):")
    for i,(page,score) in enumerate(pages_you_might_like(users, target_id, 5),1):
        print(f"{i}) {page} (score: {score})")

    # Simple visualization saved into assets
    assets_dir = Path("assets")
    assets_dir.mkdir(exist_ok=True)

    degrees = [d for _, d in G.degree()]
    plt.figure()
    plt.hist(degrees, bins=min(20, max(5, len(set(degrees)))))
    plt.title("Degree Distribution")
    plt.xlabel("Degree")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(assets_dir / "degree_distribution.png")
    plt.close()

    # Draw graph (small graphs only)
    if G.number_of_nodes() <= 100:
        plt.figure(figsize=(8,6))
        pos = nx.spring_layout(G, seed=42)
        nx.draw(G, pos, node_size=80, with_labels=False)
        plt.title("Social Graph Visualization")
        plt.tight_layout()
        plt.savefig(assets_dir / "graph.png")
        plt.close()

    print("\n✅ Saved plots to ./assets")

if __name__ == "__main__":
    main()
