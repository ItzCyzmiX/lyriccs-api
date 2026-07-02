from fastapi import FastAPI
from librelyrics import LibreLyrics

app = FastAPI()
ll = LibreLyrics()

@app.get("/lyrics/")
async def get_lyrics(id: str):
    results = {"lyrics": ""}
    if id:
        response = ll.fetch("https://open.spotify.com/track/" + id)
        lrc = response.to_lrc()
        lyrics = lrc.split('\n', 4)[4]
        results["lyrics"] = lyrics
        
    return results