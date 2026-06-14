#!/usr/bin/env python3
"""사이트맵 핑 — 검색엔진에 sitemap 갱신을 알림.

[중요] 구글은 2023-06 sitemap ping 엔드포인트를 폐기했고 Bing도 마찬가지입니다.
따라서 구글/Bing 핑은 더 이상 효과가 없을 수 있으며, 실질적인 즉시 색인은
IndexNow(scripts/indexnow_submit.py)와 Search Console / 네이버 서치어드바이저
사이트맵 제출이 담당합니다. 이 스크립트는 핑을 지원하는 엔진을 위한 보조 수단입니다.

사용법:
  python3 scripts/ping_sitemap.py
"""
import os
import sys
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from content.site import BASE_URL  # noqa: E402

SITEMAP = f"{BASE_URL.rstrip('/')}/sitemap.xml"

# 폐기 여부와 무관하게 시도할 엔드포인트 목록
TARGETS = {
    "Google(폐기)": "https://www.google.com/ping?sitemap=",
    "Bing(폐기)": "https://www.bing.com/ping?sitemap=",
}


def ping():
    enc = urllib.parse.quote(SITEMAP, safe="")
    for name, base in TARGETS.items():
        url = base + enc
        try:
            with urllib.request.urlopen(url, timeout=20) as r:
                print(f"{name}: {r.status}")
        except urllib.error.HTTPError as e:
            print(f"{name}: HTTP {e.code} (폐기된 엔드포인트일 수 있음)")
        except Exception as e:  # noqa: BLE001
            print(f"{name}: 실패 {e}")
    print("\n권장: 즉시 색인은 IndexNow + Search Console/네이버 사이트맵 제출을 사용하세요.")


if __name__ == "__main__":
    ping()
