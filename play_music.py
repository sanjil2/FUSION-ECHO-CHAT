import youtube_dl


def get_youtube_video_id(song_name):
    ydl_opts = {
        'format': 'best',
        'extract_flat': 'in_playlist',
        'simulate': True,
        'quiet': True,
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            # Perform a search query on YouTube for the song name
            info = ydl.extract_info(f"ytsearch1:{song_name}", download=False)
            video_id = info['entries'][0]['id']
            return video_id
        except Exception as e:
            print(f"Error: {e}")


video_url = f"https://www.youtube.com/watch?v=<ID>"

# Open the video URL in the default web browser
