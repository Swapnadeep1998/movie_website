import pandas as pd

item_similarity_df = pd.read_csv("item_similarity_df.csv")

def get_similar_movies(movie_name, user_ratings):
    movie_name = movie_name.lower()
    if movie_name not in item_similarity_df['title'].unique():
        print("This movie is not in our dataset \nPlease try another movie")
        return False
    else:
        similar_score = item_similarity_df[movie_name]*(user_ratings-2.5)
        similar_score = similar_score.sort_values(ascending = False)
        names = item_similarity_df.iloc[similar_score.index]['title']
        return(names.head(15).to_string(index=False).title())
        


