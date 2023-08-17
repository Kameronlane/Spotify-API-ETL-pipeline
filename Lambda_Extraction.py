
def lambda_handler(event, context):
    client_id = os.environ.get('client_id')
    client_secret = os.environ.get('client_secret')
    
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    playlist = sp.user_playlists('spotify')
    
    spotify_data = sp.playlist_tracks(playlist['items'][0]['uri'])
    
    client = boto3.client('s3')
    
    filename = "spotify_raw_" + str(datetime.now()) + ".json"
    client.put_object(
        Bucket="spotify-etl-project-lane",
        Key="raw_data/to_processed/" + filename,
        Body=json.dumps(spotify_data)
    )
    
