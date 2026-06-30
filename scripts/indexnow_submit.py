#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 — Bing·네이버·Yandex·Seznam에 한 번에 전달.

IndexNow는 참여 검색엔진이 키를 공유하므로, api.indexnow.org 한 곳에
보내면 네이버(Yeti)·Bing 등 참여 엔진 전체에 전파됩니다.
(구글은 IndexNow 미참여 → google_index_submit.py 또는 Search Console 사용)

사용법:
  # 새 글/수정 페이지만 즉시 통보 (글 올릴 때마다 권장)
  python3 scripts/indexnow_submit.py https://gangnam-swedish-massage.netlify.app/magazine/new-post/

  # URL 인자를 주지 않으면 sitemap.xml 전체를 통보
  python3 scripts/indexnow_submit.py

키 파일은 빌드 시 루트에 자동 생성됩니다: {INDEXNOW_KEY}.txt
"""
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from content.site import BASE_URL, INDEXNOW_KEY  # noqa: E402

HOST = re.sub(r"^https?://", "", BASE_URL.rstrip("/"))
ENDPOINT = "https://api.indexnow.org/indexnow"


def sitemap_urls():
    path = os.path.join(ROOT, "sitemap.xml")
    with open(path, encoding="utf-8") as f:
        return re.findall(r"<loc>([^<]+)</loc>", f.read())


def submit(urls):
    urls = [u for u in urls if u][:10000]
    if not urls:
        print("보낼 URL이 없습니다.")
        return 1
    payload = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{BASE_URL.rstrip('/')}/{INDEXNOW_KEY}.txt",
        "urlList": urls,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT, data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"IndexNow 응답: {resp.status} {resp.reason}  (URL {len(urls)}건)")
            print("→ 200/202 면 정상 접수입니다. (네이버·Bing 등 참여 엔진에 전파)")
            return 0
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code}: {e.read().decode('utf-8', 'ignore')}")
        return 1
    except Exception as e:  # noqa: BLE001
        print(f"요청 실패: {e}")
        return 1


if __name__ == "__main__":
    args = sys.argv[1:]
    urls = args if args else sitemap_urls()
    print(f"host={HOST}  대상 URL {len(urls)}건")
    sys.exit(submit(urls))
