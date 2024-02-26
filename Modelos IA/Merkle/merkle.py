!pip install plotly
!pip install umap-learn
!pip install hdbscan

import pandas as pd
import numpy as np
import re
import hdbscan
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD, LatentDirichletAllocation
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import normalize
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.manifold import TSNE
from transformers import BertModel, BertTokenizer
import torch
import umap
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import cosine_distances
from sklearn.manifold import MDS
import plotly.graph_objects as go
from plotly.subplots import make_subplots

nltk.download('stopwords')
nltk.download('wordnet')

stop_words_es = ['de', 'ha', 'la', 'que', 'el', 'en', 'y', 'a', 'los', 'del', 'se', 'las', 'por', 'un', 'para', 'con', 'no', 'una', 'su', 'al', 'es', 'lo', 'como', 'más', 'pero', 'sus']

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zñáéíóú]', ' ', text)
    text = ' '.join([word for word in text.split() if word not in stop_words_es and len(word) > 2])
    return text

tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')
model = BertModel.from_pretrained('bert-base-multilingual-cased')

df_no_supervisado = pd.read_csv('/content/drive/MyDrive/Noticias/razon.csv').head(100)
df_no_supervisado['texto_limpio'] = df_no_supervisado['titular'] + ' ' + df_no_supervisado['cuerpo']
df_no_supervisado['texto_limpio'] = df_no_supervisado['texto_limpio'].apply(preprocess_text)

vectorizador = TfidfVectorizer(max_features=1000, stop_words=stop_words_es)
X_no_supervisado = vectorizador.fit_transform(df_no_supervisado['texto_limpio'])

lsa_model = TruncatedSVD(n_components=10, random_state=0)
X_lsa = lsa_model.fit_transform(X_no_supervisado)

lda_model = LatentDirichletAllocation(n_components=10, random_state=0)
X_lda = lda_model.fit_transform(X_no_supervisado)

def mostrar_topicos(modelo, vectorizador, n_top_words=10):
    feature_names = vectorizador.get_feature_names_out()
    for topic_idx, topic in enumerate(modelo.components_):
        print(f"Tópico {topic_idx + 1}:")
        print(" ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]))

print("Tópicos LDA:")
mostrar_topicos(lda_model, vectorizador)

print("\nTópicos LSA:")
mostrar_topicos(lsa_model, vectorizador)

combined_features_lda_lsa = np.hstack((normalize(X_lda), normalize(X_lsa)))

min_cluster_size = 5
min_samples = 10
clusterer = hdbscan.HDBSCAN(min_cluster_size=min_cluster_size, min_samples=min_samples, metric='euclidean')
clusters = clusterer.fit_predict(combined_features_lda_lsa)

tsne = TSNE(n_components=2, perplexity=30, n_iter=300, random_state=42)
tsne_results = tsne.fit_transform(combined_features_lda_lsa)

plt.figure(figsize=(12, 10))
palette = sns.color_palette("bright", len(np.unique(clusters)))
sns.scatterplot(x=tsne_results[:, 0], y=tsne_results[:, 1], hue=clusters, palette=palette, legend="full", s=100, alpha=0.7)
plt.title('HDBSCAN Clusters con TSNE Mejorado')
plt.show()

topic_weights = X_lda.sum(axis=0)
topic_labels = ['Tópico {}'.format(i) for i in range(1, lda_model.n_components + 1)]
fig = px.scatter(x=topic_labels, y=topic_weights, size=topic_weights, color=topic_labels,
                 title="Distribución de Tópicos en LDA",
                 labels={"x": "Tópico", "y": "Peso del Tópico", "size": "Peso del Tópico"})
fig.show()

topic_weights_lsa = np.abs(X_lsa).sum(axis=0)

topic_labels_lsa = ['Tópico {}'.format(i) for i in range(1, lsa_model.n_components + 1)]
fig_lsa = px.scatter(x=topic_labels_lsa, y=topic_weights_lsa, size=topic_weights_lsa, color=topic_labels_lsa,
                     title="Distribución de Tópicos en LSA",
                     labels={"x": "Tópico", "y": "Peso del Tópico", "size": "Peso del Tópico"})
fig_lsa.show()

lda_similarity = cosine_similarity(X_lda.T)
lsa_similarity = cosine_similarity(X_lsa.T)

combined_similarity = (lda_similarity + lsa_similarity) / 2.0

mds = MDS(n_components=2, random_state=42, dissimilarity="precomputed")
mds_coords = mds.fit_transform(1 - combined_similarity)

most_representative_topic_index = np.argmax(combined_similarity.sum(axis=1))

combined_topic_terms = lda_model.components_[most_representative_topic_index, :] + lsa_model.components_[most_representative_topic_index, :]
combined_topic_terms /= combined_topic_terms.sum()

most_relevant_terms_indices = combined_topic_terms.argsort()[-10:][::-1]
most_relevant_terms = [vectorizador.get_feature_names_out()[i] for i in most_relevant_terms_indices]

bubble_trace = go.Scatter(
    x=mds_coords[:, 0],
    y=mds_coords[:, 1],
    mode='markers',
    marker=dict(
        size=combined_similarity.sum(axis=1) * 100,
        color=most_representative_topic_index,
        colorscale='Viridis',
        showscale=True
    ),
    text=['Tópico {}'.format(i) for i in range(len(combined_similarity))]
)

bar_trace = go.Bar(
    x=combined_topic_terms[most_relevant_terms_indices],
    y=most_relevant_terms,
    orientation='h'
)

fig = go.Figure(data=[bubble_trace, bar_trace])

fig.update_layout(
    title='Visualización Combinada de LDA y LSA',
    xaxis=dict(title='MDS dim 1'),
    yaxis=dict(title='MDS dim 2'),
    showlegend=False
)

fig.show()

distances = cosine_distances(combined_features_lda_lsa.T)

mds_model = MDS(n_components=2, dissimilarity='precomputed', random_state=42)
mds_coords = mds_model.fit_transform(distances)

mds_fig = go.Figure(data=go.Scatter(
    x=mds_coords[:, 0],
    y=mds_coords[:, 1],
    mode='markers+text',
    marker=dict(size=10, color=np.arange(len(mds_coords))),
    text=['Tópico ' + str(i) for i in range(len(mds_coords))],
    textposition='bottom center'
))
mds_fig.update_layout(title="Mapa de Distancia Intertópico")
mds_fig.show()

selected_topic_index = 0

lda_topic = lda_model.components_[selected_topic_index]
lsa_topic = lsa_model.components_[selected_topic_index]

combined_topic = (lda_topic + lsa_topic) / 2
combined_topic /= np.sum(combined_topic)

sorted_terms_indices = combined_topic.argsort()[::-1]

top_terms_indices = sorted_terms_indices[:30]
top_terms = [vectorizador.get_feature_names_out()[i] for i in top_terms_indices]
top_terms_relevance = combined_topic[top_terms_indices]

words_fig = go.Figure([go.Bar(x=top_terms_relevance, y=top_terms, orientation='h')])
words_fig.update_layout(title=f"Palabras Clave del Tópico Combinado {selected_topic_index}")
words_fig.show()

fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'scatter'}, {'type': 'bar'}]])

fig.add_trace(
    go.Scatter(x=mds_coords[:, 0], y=mds_coords[:, 1], mode='markers+text',
               marker=dict(size=10, color=np.arange(len(mds_coords))),
               text=['Tópico ' + str(i) for i in range(len(mds_coords))],
               textposition='bottom center'),
    row=1, col=1
)

fig.add_trace(
    go.Bar(x=top_terms_relevance, y=top_terms, orientation='h'),
    row=1, col=2
)

fig.update_layout(title_text="Visualización Combinada de LDA y LSA")
fig.show()

pca = PCA(n_components=3)
lsa_embeddings_3d = pca.fit_transform(X_lsa)

df_lsa_3d = pd.DataFrame(lsa_embeddings_3d, columns=['x', 'y', 'z'])
df_lsa_3d['tópico'] = np.argmax(X_lsa, axis=1)

fig_3d = px.scatter_3d(df_lsa_3d, x='x', y='y', z='z', color='tópico', title="Visualización 3D de Tópicos LSA")
fig_3d.show()

df_supervisado = pd.read_csv('/content/drive/MyDrive/Noticias/supervisado/df_total.csv')
df_supervisado['texto_limpio'] = df_supervisado['news'].apply(preprocess_text)

X_supervisado = vectorizador.transform(df_supervisado['texto_limpio'])

X_train_sup, X_test_sup, y_train_sup, y_test_sup = train_test_split(X_supervisado, df_supervisado['Type'], test_size=0.2, random_state=42)

modelo_svc = SVC(kernel='linear', C=1.0)
modelo_svc.fit(X_train_sup, y_train_sup)
predicciones_svc = modelo_svc.predict(X_test_sup)
exactitud_svc = accuracy_score(y_test_sup, predicciones_svc)
print(f"Exactitud del modelo SVC: {exactitud_svc}")

cm = confusion_matrix(y_test_sup, predicciones_svc)
sns.heatmap(cm, annot=True, fmt="d")
plt.ylabel('Verdaderos')
plt.xlabel('Predicciones')
plt.title('Matriz de Confusión para el Modelo SVC')
plt.show()

reducer = umap.UMAP(n_jobs=-1)
embedding = reducer.fit_transform(combined_features_lda_lsa)

plt.figure(figsize=(10, 6))
sns.scatterplot(x=embedding[:, 0], y=embedding[:, 1], hue=clusters, palette="deep", legend="full")
plt.title('Clusters con UMAP')
plt.show()

tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')
model = BertModel.from_pretrained('bert-base-multilingual-cased')

model.eval()

def bert_encode(texts, tokenizer, model, max_length=512):
    all_embeddings = []
    for text in texts:
        input_ids = tokenizer.encode(text, add_special_tokens=True, max_length=max_length, truncation=True)
        attention_mask = [1] * len(input_ids)
        padding_length = max_length - len(input_ids)
        input_ids = input_ids + ([0] * padding_length)
        attention_mask = attention_mask + ([0] * padding_length)
        input_ids = torch.tensor(input_ids).unsqueeze(0)
        attention_mask = torch.tensor(attention_mask).unsqueeze(0)
        with torch.no_grad():
            last_hidden_states = model(input_ids, attention_mask=attention_mask)
        embeddings = last_hidden_states[0][:, 0, :].numpy()
        all_embeddings.append(embeddings.flatten())
    return np.array(all_embeddings)

texts_to_encode = df_no_supervisado['texto_limpio'][:5].tolist()

def bert_encode(texts, tokenizer, model):
    encoded_inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**encoded_inputs)
    embeddings = outputs.last_hidden_state.mean(1)
    return embeddings

embeddings = bert_encode(texts_to_encode, tokenizer, model)
embeddings = embeddings.detach().numpy()

pca = PCA(n_components=3)
embeddings_3d = pca.fit_transform(embeddings)

df_embeddings = pd.DataFrame(embeddings_3d, columns=['x', 'y', 'z'])
df_embeddings['texto'] = texts_to_encode

fig_3d = px.scatter_3d(df_embeddings, x='x', y='y', z='z', color='texto', size_max=18, opacity=0.7)
fig_3d.update_layout(title="Representación 3D de los Embeddings de BERT")
fig_3d.show()

similarity_matrix = cosine_similarity(embeddings)

plt.figure(figsize=(10, 8))
sns.heatmap(similarity_matrix, annot=True, cmap='coolwarm')
plt.title("Mapa de Calor de Similitud de Embeddings de BERT")
plt.xlabel("Textos")
plt.ylabel("Textos")
plt.show()

perplexity_value = len(embeddings) - 1

tsne_model = TSNE(n_components=2, perplexity=perplexity_value, random_state=42)
embeddings_tsne = tsne_model.fit_transform(embeddings)

plt.figure(figsize=(12, 8))
plt.scatter(embeddings_tsne[:, 0], embeddings_tsne[:, 1])
for i, txt in enumerate(texts_to_encode):
    plt.annotate(txt, (embeddings_tsne[i, 0], embeddings_tsne[i, 1]), alpha=0.7)
plt.title("Representación 2D de los Embeddings de BERT con t-SNE")
plt.show()
