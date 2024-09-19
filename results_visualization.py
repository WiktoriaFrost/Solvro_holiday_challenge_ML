import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('df_final.csv')
df_umap_clusters = pd.read_csv('umap_dbscan_clusters.csv')


def show_drink_details(selected_drink):
    """the function displays the details of a selected drink"""
    drink_data = df[df['name'] == selected_drink].iloc[0]
    st.write(f"**Category**: {drink_data['category']}")
    st.write(f"**Tags**: {drink_data['tags']}")
    st.write(f"**Alcoholic**: {'YES' if drink_data['alcoholic'] == 1 else 'NO'}")
    st.write(f"**Ingredients**: {drink_data['ingredients']}")
    st.write(f"**K-Means Cluster**: {drink_data['cluster']}")
    st.write(f"**DBSCAN Cluster**: {drink_data['dbscan_cluster']}")


def show_interactive_graph(df_umap):
    graph = px.scatter(
        df_umap,
        x='UMAP Dim 1',
        y='UMAP Dim 2',
        color='cluster',
        hover_name='name',
        title='DBSCAN Clusters (Drink Names on Hover)',
        labels={'UMAP Dim 1': 'UMAP Dimension 1', 'UMAP Dim 2': 'UMAP Dimension 2'},
        color_continuous_scale='Viridis'
    )
    st.plotly_chart(graph)

# DETAILS OF GRAPH:
st.title("Select a drink and see details")

drink_list = df['name'].tolist()
selected_drink = st.selectbox("Select a drink:", drink_list)

show_drink_details(selected_drink)

# GRAPH WITH CLUSTERS:
st.title('Drink Clustering with UMAP and DBSCAN')
show_interactive_graph(df_umap_clusters)

# CLUSTER LISTS:
cluster_list = df_umap_clusters['cluster'].unique().tolist()
selected_cluster = st.selectbox("Select a cluster:", cluster_list)

filtered_drinks = df_umap_clusters[df_umap_clusters['cluster'] == selected_cluster]

st.write(f"Drinks in Cluster {selected_cluster}:")
st.write(filtered_drinks['name'].tolist())