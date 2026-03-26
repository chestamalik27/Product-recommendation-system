#  Product Recommendation System

##  Overview
This project is a **Product Recommendation System** built using Machine Learning techniques.  
It recommends similar products based on user selection using **content-based filtering**.

The system uses **TF-IDF vectorization** and **cosine similarity** to find and suggest relevant products.

---

## Objective
To recommend products to users based on product features such as category, brand, and description.

---

##  Tech Stack
- Python
- Pandas
- Scikit-learn
- Streamlit

---

##  Dataset
- The dataset used in this project is **manually created and structured** for learning purposes.  
- Stored in CSV format (`products.csv`)  
- Features included:
  - `name`
  - `brand`
  - `category`
  - `description`

---

##  How It Works

1. Load dataset using pandas  
2. Clean and preprocess data  
3. Combine features (category + description)  
4. Convert text into vectors using TF-IDF  
5. Compute similarity using cosine similarity  
6. Recommend top similar products  

## Output
1. Select a product from Dropdown.
2. Click Recommend
3. Get top similar product suggestions


## Output:
(<Product Recommendation Ss.png>)