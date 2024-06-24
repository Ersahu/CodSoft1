import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

data = {'user': ['User1', 'User1', 'User2', 'User2', 'User3'],
        'item': ['ItemA', 'ItemB', 'ItemB', 'ItemC', 'ItemA'],
        'rating': [5, 4, 3, 5, 4]}
df = pd.DataFrame(data)

user_item_matrix = df.pivot_table(index='user', columns='item', values='rating').fillna(0)

item_similarity = cosine_similarity(user_item_matrix.T)

def get_recommendations(user, top_n=3):
    user_ratings = user_item_matrix.loc[user]
    weighted_sums = item_similarity.dot(user_ratings)
    recommendations = pd.Series(weighted_sums, index=user_item_matrix.columns)
    recommendations = recommendations.sort_values(ascending=False).head(top_n)
    return recommendations

recommendations_for_user1 = get_recommendations('User1')
print(recommendations_for_user1)
