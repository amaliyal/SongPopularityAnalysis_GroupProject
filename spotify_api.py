import csv
from pprint import pprint as pp
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import re
import country_converter as coco

client_id = "c1a29ab79687431bb0e73dcdd5bd4f33"
client_secret = "d184f3c690914218b328a36685122072"
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id, client_secret))

playlist_id = '2mgjdYuT12BEqCGbKuMp9s'
longest_playlist_id = '5S8SJdl1BDc0ugpkEvFsIL'
test_id = '6IPIIlGv1iYoR8D0ZkhDC9'

# pp(sp.search(q='artist:Rachael Yamagata track:even so', type='track')['tracks']['items'])

# # generating original file
# def songs_in_playlist(playlist_id):
#     field_names = ['song', 'track_id', 'release_date', 'song_popularity', 'duration(ms)', 'explicit', 'artist_name', 'artist_id']
#     with open('track_feature.csv', 'w', encoding='utf-8', newline='') as f:
#         writer = csv.writer(f)
#         writer.writerow(field_names)
#         len_playlist = sp.playlist(playlist_id)['tracks']['total']
#         limit = 100
#         tracks = []
#         for i in range(0, len_playlist, limit):
#             playlist = sp.playlist_items(playlist_id, offset=i)['items']
#
#             for playlist_info in playlist:
#                 track_info = playlist_info['track']
#                 song_name = track_info['name']
#                 if song_name == '':
#                     continue
#
#                 artist_info = track_info['artists']
#                 if len(artist_info) != 1:
#                     continue
#
#                 for artist in artist_info:
#                     artist_name = artist['name']
#
#                 query = 'artist:{} track:{}'.format(artist_name, song_name)[0:100]
#
#                 track_info = sp.search(q=query, type='track', limit=10)['tracks']['items']
#
#                 song_popularity = 0
#
#                 for info_test in track_info:
#                     print(info_test)
#                     artist_info = info_test['artists']
#                     if len(artist_info) != 1:
#                         continue
#
#                     if info_test['popularity'] > song_popularity:
#                         info = info_test
#                         song_popularity = info_test['popularity']
#
#                 song_popularity = info['popularity']
#
#                 artist_name = artist_info[0]['name']
#                 artist_id = artist_info[0]['id']
#
#                 release_date = info['album']['release_date']
#                 explicit = info['explicit']
#                 duration_ms = info['duration_ms']
#                 song_name = info['name']
#                 track_id = info['id']
#
#                 info_list = [song_name, track_id, release_date, song_popularity, duration_ms, explicit, artist_name, artist_id]
#                 tracks.append(info_list)
#                 # pp(info_list)
#         # pp(tracks)
#         writer.writerows(tracks)
#         f.close()
#
#     return tracks

# songs_in_playlist(longest_playlist_id)

# # clean up via panda before continuing
# df = pd.read_csv("track_feature.csv").drop_duplicates().dropna()
# df.to_csv('track_feature_cleaned.csv', index=False)

# # remove artists with the same name
# df = pd.read_csv("track_feature_cleaned.csv").sort_values(by=["artist_name", 'artist_id'], ascending=[True, True])
# df.to_csv('track_feature_sorted.csv', index=False)
#
# artist_name = df.iat[0, 6]
# artist_id = df.iat[0, 7]
# drop_list = []
#
# for i in range(1, len(df.index)):
#     artist_name_test = df.iat[i, 6]
#     artist_id_test = df.iat[i, 7]
#     if artist_name_test == artist_name and artist_id_test != artist_id:
#         drop_list.append(artist_name)
#     artist_name = artist_name_test
#     artist_id = artist_id_test
#
# drop_list = list(set(drop_list))
#
# for row in df.index:
#     if df.loc[row, "artist_name"] in drop_list:
#         df.drop(row, inplace=True)
#
# df.to_csv('track_feature_corrected.csv', index=False)


# df = pd.read_csv("track_feature_corrected.csv")
# follower_no_dic = {}
# genres_dic = {}
# artist_popularity_dic = {}
#
# artist_id_list = df['artist_id'].tolist()
# artist_id_list = list(set(artist_id_list))
#
# for artist_id in artist_id_list:
#     artist_info = sp.artist(artist_id)
#     print(artist_info)
#     follower_no_dic[artist_id] = artist_info['followers']['total']
#     artist_popularity_dic[artist_id] = artist_info['popularity']
#     genres_dic[artist_id] = artist_info['genres']
#
# df['artist_follower_no'] = df['artist_id'].map(follower_no_dic)
# df['artist_genres'] = df['artist_id'].map(genres_dic)
# df['artist_popularity'] = df['artist_id'].map(artist_popularity_dic)
#
# df.to_csv('track_artist_features.csv', index=False)
#
# # clean up via panda before continuing
# df = pd.read_csv("track_artist_features.csv")
# for row in df.index:
#     if df.loc[row, 'artist_genres'] == '[]':
#         df.loc[row, 'artist_genres'] = 'N/A'
# df.to_csv('track_artist_features_cleaned.csv', index=False)


# df = pd.read_csv("track_artist_features_cleaned.csv")
# acousticness = {}
# danceability = {}
# energy = {}
# instrumentalness = {}
# key = {}
# liveness = {}
# loudness = {}
# mode = {}
# speechiness = {}
# tempo = {}
# time_signature = {}
# valence = {}
#
# track_id_list = df['track_id'].tolist()
# track_id_list = list(set(track_id_list))
#
# for track_id in track_id_list:
#     track_infos = sp.audio_features(track_id)
#     print(track_infos)
#     for track_info in track_infos:
#         if track_info is None:
#             acousticness[track_id] = 'N/A'
#             danceability[track_id] = 'N/A'
#             energy[track_id] = 'N/A'
#             instrumentalness[track_id] = 'N/A'
#             key[track_id] = 'N/A'
#             liveness[track_id] = 'N/A'
#             loudness[track_id] = 'N/A'
#             mode[track_id] = 'N/A'
#             speechiness[track_id] = 'N/A'
#             tempo[track_id] = 'N/A'
#             time_signature[track_id] = 'N/A'
#             valence[track_id] = 'N/A'
#             continue
#         acousticness[track_id] = track_info['acousticness']
#         danceability[track_id] = track_info['danceability']
#         energy[track_id] = track_info['energy']
#         instrumentalness[track_id] = track_info['instrumentalness']
#         key[track_id] = track_info['key']
#         liveness[track_id] = track_info['liveness']
#         loudness[track_id] = track_info['loudness']
#         mode[track_id] = track_info['mode']
#         speechiness[track_id] = track_info['speechiness']
#         tempo[track_id] = track_info['tempo']
#         time_signature[track_id] = track_info['time_signature']
#         valence[track_id] = track_info['valence']
#
# df['acousticness'] = df['track_id'].map(acousticness)
# df['danceability'] = df['track_id'].map(danceability)
# df['energy'] = df['track_id'].map(energy)
# df['instrumentalness'] = df['track_id'].map(instrumentalness)
# df['key'] = df['track_id'].map(key)
# df['liveness'] = df['track_id'].map(liveness)
# df['loudness'] = df['track_id'].map(loudness)
# df['mode'] = df['track_id'].map(mode)
# df['speechiness'] = df['track_id'].map(speechiness)
# df['tempo'] = df['track_id'].map(tempo)
# df['time_signature'] = df['track_id'].map(time_signature)
# df['valence'] = df['track_id'].map(valence)
#
# df.to_csv('track_artist_audio_features.csv', index=False)


# # clean up via panda before continuing
# df = pd.read_csv("track_artist_audio_features.csv")
# for row in df.index:
#     if df.loc[row, 'time_signature'] < 3:
#         df.loc[row, 'acousticness'] = ''
#         df.loc[row, 'danceability'] = ''
#         df.loc[row, 'energy'] = ''
#         df.loc[row, 'instrumentalness'] = ''
#         df.loc[row, 'key'] = ''
#         df.loc[row, 'liveness'] = ''
#         df.loc[row, 'loudness'] = ''
#         df.loc[row, 'mode'] = ''
#         df.loc[row, 'speechiness'] = ''
#         df.loc[row, 'tempo'] = ''
#         df.loc[row, 'time_signature'] = ''
#         df.loc[row, 'valence'] = ''
#
#
# df.to_csv('track_artist_audio_features_cleaned.csv', index=False)
