from pytube import Playlist

# URL de la playlist YouTube
playlist_url = "https://music.youtube.com/playlist?list=PLFYmBLX6OnjfZOHdSQG21QD4Wa79B1i_1"

# Instancier un objet Playlist avec l'URL de la playlist
playlist = Playlist(playlist_url)

# Parcourir chaque vidéo de la playlist et télécharger
for video in playlist.videos:
    try:
        # Télécharger la vidéo
        video.streams.filter(only_audio=True).first().download(output_path='Chemin_du_dossier_de_sortie')
        print(f"Téléchargement de {video.title} terminé.")
    except Exception as e:
        print(f"Impossible de télécharger {video.title}: {str(e)}")
