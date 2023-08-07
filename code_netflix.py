import pandas as pd
import matplotlib.pyplot as plt

# Loading the CSV file
netflix=pd.read_csv('netflix_data.csv',sep=",")

# Filtering data
netflix_subset=netflix[netflix['type']=='Movie']
netflix_movies=netflix_subset[["title", "country", "genre", "release_year", "duration"]]
short_movies=netflix_movies[netflix_movies['duration']<60]

# Assigning colours
colors=[]
for label, row in netflix_movies.iterrows():
    if row['genre'] == "Children":
        colors.append('red')
    elif row['genre'] == "Documentaries":
        colors.append('blue')
    elif row['genre'] == "Stand-Up":
        colors.append('green')
    else:
        colors.append('black')

# Chart
plt.style.use('fivethirtyeight')
fig=plt.figure(figsize=(12,8))
plt.scatter(netflix_movies.loc[:,'release_year'],
            netflix_movies.loc[:,'duration'],color=colors)
plt.title('Movie Duration by Year of Release')
plt.xlabel('Release year')
plt.ylabel('Duration (min)')
plt.show()

# Are we certain that movies are getting shorter?
answer="maybe"
