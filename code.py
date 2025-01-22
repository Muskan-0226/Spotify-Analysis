#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# Load the CSV file
tracks = pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\Spotify\tracks.csv")

tracks.head()


# In[3]:


# nulll values
pd.isnull(tracks).sum()


# In[4]:


tracks.info()


# In[5]:


tracks.columns


# In[6]:


sorted_tracks = tracks.sort_values('popularity', ascending = True).head(10)
sorted_tracks                                   
                                   


# In[7]:


tracks.describe().transpose()


# In[8]:


# most popular song
most_popular = tracks.query('popularity>90', inplace = False).sort_values('popularity', ascending = False)
most_popular[:10]


# In[9]:


# Reset the index if "release_date" is already the index
tracks.reset_index(inplace=True)

# Remove rows with dates that don't match the "YYYY-MM-DD" format
tracks = tracks[tracks['release_date'].str.match(r'^\d{4}-\d{2}-\d{2}$', na=False)]

# Now set the index to "release_date" and convert to datetime
tracks.set_index("release_date", inplace=True)
tracks.index = pd.to_datetime(tracks.index)

# Display the cleaned DataFrame
print(tracks.head())



# In[10]:


tracks[['artists']].iloc[15]


# In[11]:


# convert the ms into second
tracks['duration'] = tracks["duration_ms"].apply(lambda x: round(x/1000))
tracks.drop("duration_ms", inplace = True, axis=1)


# In[12]:


tracks.duration.head()


# In[13]:


import seaborn as sns
import matplotlib.pyplot as plt

# Drop unwanted columns and select only numeric columns
corr_tracks = tracks.drop(["key", "mode", "explicit"], axis=1).select_dtypes(include=[float, int]).corr(method="pearson")

# Plotting the heatmap
plt.figure(figsize=(14, 6))
heatmap = sns.heatmap(corr_tracks, annot=True, fmt=".1g", vmin=-1, vmax=1, center=0,
                      cmap="inferno", linewidth=1, linecolor="Black")

# Customize title and x-axis labels
heatmap.set_title('Correlation Heatmap between Variables')
heatmap.set_xticklabels(heatmap.get_xticklabels(), rotation=90)
heatmap.set_yticklabels(heatmap.get_yticklabels(), rotation=0)

# Show plot
plt.show()


# In[14]:


sample_tracks = tracks.sample(int(0.004*len(tracks)))


# In[15]:


print(len(sample_tracks))


# In[16]:


# Set the figure size
plt.figure(figsize=(10, 6))

# Create a regression plot
sns.regplot(data=sample_tracks, y="loudness", x="energy", color="c").set(title="Loudness vs Energy Correlation")

# Show the plot
plt.show()


# In[17]:


# Set the figure size
plt.figure(figsize=(10, 6))

# Create a regression plot
sns.regplot(data=sample_tracks, y="popularity", x="acousticness", color="b").set(title="popularity vs acousticness Correlation")

# Show the plot
plt.show()


# In[18]:


tracks['dates'] = tracks.index.get_level_values("release_date")
tracks.dates= pd.to_datetime(tracks.dates)
years = tracks.dates.dt.year


# In[19]:


# Create a displot for the 'years' data
sns.displot(years, discrete=True, aspect=2, height=5, kind="hist").set(title="Number of Songs per Year")


# In[20]:


# Assuming 'tracks' DataFrame has 'duration' and 'years' columns
total_duration = tracks['duration']
fig_dims = (18, 7)
fig, ax = plt.subplots(figsize=fig_dims)

# Plotting the barplot with corrected syntax
sns.barplot(x=years, y=total_duration, ax=ax, errwidth=0).set(title="Years vs Duration")

plt.xticks(rotation=90)
plt.show()


# In[21]:


# Assuming 'tracks' DataFrame has 'duration' and 'years' columns
total_duration = tracks['duration']
sns.set_style("whitegrid")  # Apply white grid style

fig_dims = (10, 5)
fig, ax = plt.subplots(figsize=fig_dims)

# Correct variable name in the line plot
sns.lineplot(x=years, y=total_duration, ax=ax).set(title="Year vs Duration")

plt.xticks(rotation=60)
plt.show()


# In[22]:


genre = pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\Spotify\SpotifyFeatures.csv")


# In[23]:


genre.head()


# In[24]:


plt.title("Duration of the songs in diff genre")
sns.color_palette("rocket", as_cmap = True)
sns.barplot(y = 'genre', x = 'duration_ms', data= genre)
plt.xlabel("Duration in milli seconds")
plt.ylabel("Genre")


# In[25]:


sns.set_style(style = "darkgrid")
plt.figure(figsize=(10,5))
famous = genre.sort_values("popularity", ascending = False).head(10)
sns.barplot(y='genre', x = 'popularity', data = famous).set(title= "Top 5 Genre by popularity")


# In[ ]:





# In[ ]:
