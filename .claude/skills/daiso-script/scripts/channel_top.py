#!/usr/bin/env python3
"""유튜브 채널 쇼츠를 조회수 순으로 정리한다 (제목, 조회수만).

사용법:
    python3 channel_top.py https://www.youtube.com/@homeddakpick --keyword 다이소 --top 10

- yt-dlp가 필요하다: pip install yt-dlp
- 환경 네트워크 허용 목록에 www.youtube.com이 있어야 한다.
- 목록(flat-playlist)만 가져온다. 개별 영상 자막을 가져오다 봇 확인이 뜨면 우회하지 말고
  사용자에게 영상 파일을 받아 분석한다.
- 제목은 한국어로, 조회수는 기본 요청으로 받아 영상 ID로 합친다
  (한국어 요청에서는 조회수가 빠지는 경우가 있음).
"""
import argparse
import json
import re
import subprocess


def fetch(url: str, lang: str | None) -> list[dict]:
    cmd = ["yt-dlp", "--flat-playlist", "-J"]
    if lang:
        cmd += ["--extractor-args", f"youtube:lang={lang}"]
    out = subprocess.run(cmd + [url], capture_output=True, text=True, check=True).stdout
    return json.loads(out).get("entries") or []


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("channel", help="채널 URL (끝에 /shorts는 자동으로 붙음)")
    p.add_argument("--keyword", default="", help="제목 필터 정규식, 예: '다이소|무타공'")
    p.add_argument("--top", type=int, default=10)
    a = p.parse_args()

    url = a.channel.split("?")[0].rstrip("/")
    if not url.endswith("/shorts"):
        url += "/shorts"

    ko = {e["id"]: e.get("title") or "" for e in fetch(url, "ko")}
    rows = []
    for e in fetch(url, None):
        title = ko.get(e["id"]) or e.get("title") or ""
        if a.keyword and not re.search(a.keyword, title):
            continue
        rows.append((e.get("view_count") or 0, e["id"], title))

    rows.sort(reverse=True)
    print(f"{url}  (일치 {len(rows)}개)")
    for views, vid, title in rows[: a.top]:
        print(f"{views:>10,}  https://www.youtube.com/shorts/{vid}  {title}")


if __name__ == "__main__":
    main()
