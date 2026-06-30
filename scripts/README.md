# 색인(인덱싱) 자동화 가이드

빠른 색인을 위한 구성 요소와 사용법입니다. 빌드(`python3 build.py`)만 하면
아래 파일들이 사이트 루트에 자동 생성됩니다.

| 파일 | 역할 |
|------|------|
| `sitemap.xml` | 색인 대상 72개 URL (구글·네이버 공통) |
| `rss.xml` | 매거진 글 피드 — 신규 글 발행 시 색인 신호 (robots.txt에도 등록됨) |
| `robots.txt` | 전 봇 + 네이버 Yeti 허용, `sitemap.xml`·`rss.xml` 위치 명시 |
| `<INDEXNOW_KEY>.txt` | IndexNow 키 검증 파일 (Bing·네이버·Yandex가 읽음) |

키는 `content/site.py`의 `INDEXNOW_KEY` 에 있습니다.

---

## 1. 가장 빠른 색인 경로 (요약)

1. **배포** — Netlify에 배포 → `https://gangnam-swedish-massage.netlify.app/` 반영
2. **사이트 소유확인 + 사이트맵 제출** (1회)
   - 구글 Search Console: 속성 등록 → `sitemap.xml` 제출
   - 네이버 서치어드바이저: 사이트 등록(메인페이지 메타태그 이미 삽입됨) → `sitemap.xml`·`rss.xml` 제출
3. **글 올릴 때마다** — IndexNow로 즉시 통보 (Bing·네이버):
   ```bash
   python3 build.py
   python3 scripts/indexnow_submit.py https://gangnam-swedish-massage.netlify.app/magazine/새글/
   ```
4. **구글은 IndexNow 미참여** → 새 글은 Search Console "URL 검사 → 색인 요청"
   또는 `scripts/google_index_submit.py` (서비스 계정 필요).

---

## 2. IndexNow (Bing·네이버·Yandex 즉시 통보) — `indexnow_submit.py`

IndexNow 참여 엔진은 키를 공유하므로 `api.indexnow.org` 한 곳에 보내면
네이버·Bing 등 전체에 전파됩니다. 별도 가입/키 없이 작동합니다.

```bash
# 특정 URL만 (글 발행 시 권장)
python3 scripts/indexnow_submit.py https://gangnam-swedish-massage.netlify.app/magazine/새글/

# 인자 없이 실행하면 sitemap.xml 전체 통보
python3 scripts/indexnow_submit.py
```
전제: 키 파일 `<INDEXNOW_KEY>.txt`가 **배포된 사이트 루트에서 접근 가능**해야 검증됩니다.
(빌드 시 자동 생성되므로 배포만 되어 있으면 OK)

## 3. 구글 Indexing API — `google_index_submit.py`

구글은 IndexNow에 참여하지 않습니다. 공식적으로 Indexing API는
JobPosting·BroadcastEvent용이지만 `URL_UPDATED` 통보는 일반 URL에도 쓰입니다.
가장 확실한 일반 색인은 Search Console + sitemap이며, 이 스크립트는 보조 수단입니다.

```bash
pip install google-auth requests
export GOOGLE_APPLICATION_CREDENTIALS=/path/service_account.json
python3 scripts/google_index_submit.py https://gangnam-swedish-massage.netlify.app/magazine/새글/
```
1회 준비: Cloud 프로젝트에서 Indexing API 활성화 → 서비스 계정 JSON 발급 →
Search Console 속성에 서비스 계정 이메일을 **소유자**로 추가.

## 4. 사이트맵 핑 — `ping_sitemap.py`

> 구글·Bing은 2023년 sitemap ping 엔드포인트를 폐기했습니다. 효과가 제한적이며,
> 실질적 즉시 색인은 IndexNow + Search Console 제출이 담당합니다. 보조용입니다.

```bash
python3 scripts/ping_sitemap.py
```

## 5. (선택) 배포 시 자동 통보

`.github/workflows/indexnow.yml` 가 main 브랜치 푸시 시 IndexNow로 사이트맵
전체를 자동 통보합니다. Cloudflare Pages 배포가 끝난 뒤 실행되도록 약간의
지연을 두며, 별도 시크릿이 필요 없습니다(IndexNow 키는 저장소에 포함).
구글 Indexing API 자동화를 원하면 서비스 계정 JSON을 GitHub Secret으로 넣고
같은 워크플로에 단계를 추가하면 됩니다.
