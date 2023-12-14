import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('steam_reviews.csv')

df['ano'] = pd.to_datetime(df['date_posted']).dt.year

ano = st.sidebar.selectbox('Selecione o Ano', options=df['ano'].unique())
early_access = st.sidebar.checkbox('Apenas Early Access')
recommendation = st.sidebar.checkbox('Apenas Recomendados')

filtered_df = df[df['ano'] == ano]
if early_access:
    filtered_df = filtered_df[filtered_df['is_early_access_review'] == "Not Recommended"]
if recommendation:
    filtered_df = filtered_df[filtered_df['recommendation'] == "Recommended"]

game = st.sidebar.selectbox('Selecione um Jogo', options=df['title'].unique())
game_df = filtered_df[filtered_df['title'] == game]

st.write(game_df)


st.header('Gráficos')

# Média de horas de jogo de cada jogo
avg_hours = df.groupby('title')['hour_played'].mean()
fig, ax = plt.subplots(figsize=(10,4))
ax.bar(avg_hours.index, avg_hours.values)
plt.xticks(rotation=90)
plt.title('Média de Horas Jogadas por Jogo')
plt.xlabel('Jogo')
plt.ylabel('Média de Horas Jogadas')
st.pyplot(fig)

# Quantidade de funny
funny_counts = df.groupby('title')['funny'].sum()
fig, ax = plt.subplots(figsize=(10,4))
ax.bar(funny_counts.index, funny_counts.values)
plt.xticks(rotation=90)
plt.title('Quantidade de Reações Engraçadas por Jogo')
plt.xlabel('Jogo')
plt.ylabel('Quantidade de Reações Engraçadas')
st.pyplot(fig)

# Quantidade de helpful por jogo
helpful_counts = df.groupby('title')['helpful'].sum()
fig, ax = plt.subplots(figsize=(10,4))
ax.bar(helpful_counts.index, helpful_counts.values)
plt.xticks(rotation=90)
plt.title('Quantidade de Reações Úteis por Jogo')
plt.xlabel('Jogo')
plt.ylabel('Quantidade de Reações Úteis')
st.pyplot(fig)