import streamlit as st
import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("products.csv")
df["combined_features"] = df["category"]= "" + df["description"]

vectorizer= TfidfVectorizer()
feature_matrix = vectorizer.fit_transform(df["combined_features"])
similarity = cosine_similarity(feature_matrix)

def recommend(product_name):
    index=df[df["name"] == product_name].index[0]
    scores = list(enumerate(similarity[index]))
    scores = sorted(scores,key=lambda x:x[1], reverse = True)[1:6]
    return[df.iloc[i[0]]["name"] for i in scores]
    
st.title("Product Recommendation System")

product = st.selectbox("Choose a product",
df["name"].values)

if st.button("Recommend"):
    results = recommend(product)

    st.markdown("---")
    st.subheader(f"Top{len(results)}Recommended Products")

    for r in results:
        st.markdown(f"{r}")
        
