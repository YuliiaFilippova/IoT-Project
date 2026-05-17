import cv2
import yt_dlp


def get_stream_url(youtube_url):

    ydl_opts = {
        "quiet": True,
        "format": "best"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:

        info = ydl.extract_info(
            youtube_url,
            download=False
        )

        return info["url"]


def open_stream(youtube_url):

    stream_url = get_stream_url(youtube_url)

    cap = cv2.VideoCapture(stream_url)

    if not cap.isOpened():
        raise Exception("Could not open stream")

    return cap