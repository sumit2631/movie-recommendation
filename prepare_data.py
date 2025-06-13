import pandas as pd

# Load CSV
movies = pd.read_csv("movies.csv")

# Fill null values with empty strings
for feature in ['genres', 'keywords', 'cast', 'director']:
    movies[feature] = movies[feature].fillna('')

# Combine features
def combine_features(row):
    return f"{row['genres']} {row['keywords']} {row['cast']} {row['director']}"

movies['combined_features'] = movies.apply(combine_features, axis=1)

# Save updated CSV
movies.to_csv("movies.csv", index=False)

print("✅ combined_features column added and movies.csv updated.")
