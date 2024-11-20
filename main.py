import vlc
import time
import sys
import os

def play_audio_file(file_path):
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        return
    
    # Create an instance of the VLC player
    vlc_instance = vlc.Instance()
    player = vlc_instance.media_player_new()

    # Create a new media object
    media = vlc_instance.media_new(file_path)
    player.set_media(media)

    # Play the media
    player.play()
    time.sleep(0.1)
    
    # Duration of media from milliseconds to seconds
    total_duration_seconds = (player.get_length()) // 1000 
    # Calculate minutes and seconds for media duration
    media_minutes = total_duration_seconds // 60
    media_seconds = total_duration_seconds % 60 
    # Format output to print duration of media
    formatted_media_duration = f"Duration:{media_minutes} minutes and {media_seconds} seconds"
    print(formatted_media_duration)

    # Wait until the media is playing
    playing = True
    while playing:
        state = player.get_state()
        if state in [vlc.State.Ended, vlc.State.Error]:
            playing = False
        time.sleep(0.1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python play_flac.py /path/to/your/song.flac")
    else:
        flac_file = sys.argv[1]
        play_audio_file(flac_file)
