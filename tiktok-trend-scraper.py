import requests
import json

def get_tiktok_trending(limit=10):
    headers = {
        "User-Agent": "Mozilla/5.0",
    }

    # Unofficial API (used by some apps)
    url = f"https://www.tikwm.com/api/feed/list?count={limit}"

    response = requests.get(url, headers=headers)
    data = response.json()

    if data["code"] != 0:
        print("Failed to fetch data:", data.get("msg"))
        return []

    videos = data["data"]
    result = []

    for vid in videos:
        result.append({
            "desc": vid.get("title", "No caption"),
            "author": vid["author"].get("unique_id", "Unknown"),
            "views": vid.get("play_count", "N/A"),
            "likes": vid.get("digg_count", "N/A"),
            "url": f"https://www.tiktok.com/@{vid['author']['unique_id']}/video/{vid['video_id']}"
        })

    return result

# Example usage
if __name__ == "__main__":
    trending = get_tiktok_trending(5)
    for v in trending:
        print(f"\n@{v['author']} - {v['desc']}")
        print(f"❤️ {v['likes']}  👁️ {v['views']}")
        print(f"🔗 {v['url']}")
