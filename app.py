# filename: app.py

from flask import Flask, request, send_file, jsonify
import yt_dlp
import uuid
import os

app = Flask(__name__)

@app.route("/download", methods=["GET"])
def download_video():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "Missing 'url' parameter"}), 400

    output_file = f"{uuid.uuid4()}.mp4"

    ydl_opts = {
        'format': 'best[ext=mp4]/best',
        'outtmpl': output_file,
        'merge_output_format': 'mp4',
        'quiet': True,
         'cookiefile': 'youtube_cookies.txt',  # Optional: ensure file exists
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        if not os.path.exists(output_file) or os.path.getsize(output_file) < 100000:
            return jsonify({"error": "Download failed or file too small"}), 500

        return send_file(output_file, mimetype="video/mp4", as_attachment=True, download_name="video.mp4")

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if os.path.exists(output_file):
            os.remove(output_file)

if __name__ == "__main__":
    app.run(debug=True)
