#!/usr/bin/env python3
"""구글 Indexing API 색인 통보 (구글은 IndexNow 미참여).

구글 Indexing API는 공식적으로는 JobPosting·BroadcastEvent 구조화 페이지를
위한 것이지만, URL_UPDATED 통보 자체는 일반 URL에도 사용할 수 있습니다.
가장 확실한 일반 색인 경로는 Search Console + sitemap이며, 본 스크립트는
신규/수정 글을 빠르게 알리는 보조 수단입니다.

사전 준비 (1회):
  1) Google Cloud 프로젝트에서 "Indexing API" 활성화
  2) 서비스 계정 생성 → JSON 키 다운로드 (예: service_account.json)
  3) Search Console 속성에 그 서비스 계정 이메일을 "소유자"로 추가
  4) pip install google-auth requests

사용법:
  export GOOGLE_APPLICATION_CREDENTIALS=/path/service_account.json
  python3 scripts/google_index_submit.py https://gangnam-swedish-massage.pages.dev/magazine/new-post/
  # 인자 없으면 sitemap.xml 전체 (일일 쿼터 200건 주의)
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
SCOPES = ["https://www.googleapis.com/auth/indexing"]


def sitemap_urls():
    with open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8") as f:
        return re.findall(r"<loc>([^<]+)</loc>", f.read())


def main(urls):
    try:
        import google.auth.transport.requests
        from google.oauth2 import service_account
    except ImportError:
        print("의존성 누락: pip install google-auth requests")
        return 1
    cred_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not cred_path or not os.path.exists(cred_path):
        print("GOOGLE_APPLICATION_CREDENTIALS 환경변수에 서비스 계정 JSON 경로를 지정하세요.")
        return 1

    creds = service_account.Credentials.from_service_account_file(
        cred_path, scopes=SCOPES)
    authed = google.auth.transport.requests.AuthorizedSession(creds)

    ok = 0
    for url in urls:
        if not url:
            continue
        r = authed.post(ENDPOINT, json={"url": url, "type": "URL_UPDATED"})
        if r.status_code == 200:
            ok += 1
            print(f"OK   {url}")
        else:
            print(f"FAIL {r.status_code} {url} :: {r.text[:200]}")
    print(f"\n완료: {ok}/{len(urls)} 건 접수 (일일 쿼터 기본 200건)")
    return 0


if __name__ == "__main__":
    args = sys.argv[1:]
    sys.exit(main(args if args else sitemap_urls()))
