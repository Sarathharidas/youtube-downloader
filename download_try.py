import yt_dlp, os

def save_video(url, dest_dir="downloads"):
    os.makedirs(dest_dir, exist_ok=True)
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'outtmpl': os.path.join(dest_dir, '%(title)s-%(id)s.%(ext)s'),
        'quiet': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        if not filename.endswith('.mp4'):
            filename = os.path.splitext(filename)[0] + '.mp4'
    return filename

# Example:
path = save_video('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
#print(path)
