#!/usr/bin/env python
# coding: utf-8

# In[80]:


pip install spotipy


# In[84]:


# Upgrade pip using Jupyter Notebook cell
get_ipython().system('pip3 install --upgrade pip')



# In[56]:


import spotipy
import pandas as pd


# In[6]:


from spotipy.oauth2 import SpotifyClientCredentials


# In[11]:


client_credentials_manager= SpotifyClientCredentials(client_id="748871c60a664203b95bc971547f5b89", client_secret="4562b205a4db46a7a7a042cc84d9b50b")


# In[13]:


sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# In[14]:


playlist_link = "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M"


# In[22]:


playlist_URI = playlist_link.split("/")[-1]


# In[23]:


sp.playlist_tracks(playlist_URI)


# In[24]:


data= sp.playlist_tracks(playlist_URI)


# In[26]:


data['items'] [0] ['track']['album']['id']


# In[27]:


data['items'] [0] ['track']['album']['name']


# In[28]:


data['items'] [0] ['track']['album']['release_date']


# In[30]:


data['items'] [0] ['track']['album']['total_tracks']


# In[32]:


data['items'] [0] ['track']['album']['external_urls']['spotify']


# In[41]:


album_list = []
for row in data['items']:
    album_id = row['track']['album']['id']
    album_name = row['track']['album']['name']
    album_release_date = row['track']['album']['release_date']
    album_total_tracks = row['track']['album']['total_tracks']
    album_url = row['track']['album']['external_urls']['spotify']
    album_element = {
        'album_id': album_id,
        'album_name': album_name,
        'album_release_date': album_release_date,
        'album_total_tracks': album_total_tracks,
        'album_url': album_url
    }
    album_list.append(album_element)


# In[42]:


album_list 


# In[44]:


data['items'][0]['track']['artists']


# In[49]:


artist_list=[]
for row in data ['items']:
    for key,value in row.items():
        if key == "track":
            for artist in value['artists']:
                artist_dict = {'artist_id':artist['id'],'artist_name': artist['name'],'external_url': artist['href']}
                artist_list.append(artist_dict)


# In[50]:


artist_list


# In[54]:


song_list = []
for row in data['items']:
    song_id = row['track']['id']
    song_name = row['track']['name']
    song_duration = row['track']['duration_ms']
    song_url = row['track']['external_urls']['spotify']
    song_popularity = row['track']['popularity']
    song_added=row['added_at']
    album_id=row ['track']['album'] ['id']
    artist_id=row['track']['album']['artists'] [0] ['id']
    song_element = {
        'song_id': song_id,
        'song_name': song_name,
        'duration_ms':song_duration,
        'url': song_url,
        'popularity': song_popularity,
        'song_added':  song_added,
        'album_id': album_id ,
        'artist_id': artist_id,
        
        
    }
    song_list.append(song_element)


# In[55]:


song_list


# In[57]:


album_df= pd.DataFrame.from_dict(album_list)


# In[58]:


album_df.head()


# In[59]:


album_df.info()


# In[60]:


album_df= album_df.drop_duplicates(subset=['album_id'])


# In[61]:


artist_df= pd.DataFrame.from_dict(artist_list)


# In[63]:


artist_df.head()


# In[64]:


artist_df= artist_df.drop_duplicates(subset=['artist_id'])


# In[65]:


song_df= pd.DataFrame.from_dict(song_list)


# In[66]:


song_df= song_df.drop_duplicates(subset=['song_id'])


# In[70]:


album_df['album_release_date'] = pd.to_datetime(album_df['album_release_date'])


# In[72]:


album_df.info()


# In[74]:


song_df['song_added'] = pd.to_datetime(song_df['song_added'])


# In[76]:


song_df.info()


# In[ ]:




