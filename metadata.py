import json
from threading import local
from typing import List, Set

METADATA_FILE_NAME = 'metadata-tracks.json'

# Metadata file looks like 
# {
#     "playlists" : [
#         {
#             "id" : str,
#             "tracks" : [
#                 {
#                     "spotify_id" : str,
#                     "local_filename" : str
#                 }
#             ]
#         }
#     ]
# }

class Metadata:
    original_data : dict
    modified_data : dict
    tracks : Set

    def __init__(self):
        # Load metadata file in memory
        try:
            with open(METADATA_FILE_NAME, 'r') as metadata_file:
                self.original_data = json.load(metadata_file)
                self.process()
        except FileNotFoundError:
            print("Did not find an existing metadata-tracks.json file, continuing...")

    def process(self) -> None:
        self._get_track_set()
        self.modified_data = self.original_data.copy()

    def _get_track_set(self) -> None:
        all_track_ids = set()
        playlists = self.data['playlists']
        for playlist in playlists:
            tracks = playlist['tracks']
            [all_track_ids.add(track['spotify_id']) for track in tracks]
        
        self.tracks = all_track_ids


    def track_contained(self, id:str) -> bool:
        return (id in self.tracks)
    
    def write_track_to_metadata(self, playlist_id:str, spotify_id: str, local_filename:str) -> None:
        for playlist in self.modified_data['playlists']:
            if playlist['id'] == playlist_id:
                playlist['tracks'].append({
                    'spotify_id':spotify_id,
                    'local_filename':local_filename,
                })

    def write_metadata_file(self) -> None:
        # Write this metadata file to disk
        with open(METADATA_FILE_NAME, 'w') as metadata_file:
            json.dump(self.modified_data, metadata_file)
