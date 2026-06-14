# 간다GO — 강남 출장마사지·강남구 홈타이 안내 사이트

강남구 전지역 방문 관리(출장마사지·홈타이) 안내용 정적 사이트입니다.
예약전화: **0508-202-4719**

## 구조

- 정적 HTML 사이트 — 어느 호스팅(GitHub Pages, Netlify, 일반 웹서버)에서든 그대로 서빙 가능
- `build.py` + `content/` 패키지에서 페이지를 생성하는 빌드 방식
- 생성물(각 디렉터리의 `index.html`, `sitemap.xml`, `robots.txt`)도 저장소에 포함

```
build.py            # 빌드 스크립트 (레이아웃·글자수 검사·sitemap 생성)
content/
  site.py           # 상호(간다GO)·전화·BASE_URL·메뉴 구조
  main.py           # 메인 페이지 (+ WebPage/Organization/FAQPage JSON-LD)
  areas.py          # 지역별: 강남구 허브 + 대표 행정동 12개
  stations.py       # 지하철역별: 허브 + 역 28개 (_stations_a / _stations_b 병합)
  _stations_a.py    # 역 1~14 (강남대로·압구정·청담·삼성 라인)
  _stations_b.py    # 역 15~28 (대치·도곡·개포·일원·수서 라인)
  themes.py         # 테마별: 허브 + 14개 테마
  info.py           # 출장마사지 안내·코스·예약·가이드·후기·고객센터·약관
  magazine.py       # 매거진 글 + 허브
  about.py          # 운영자 소개·콘텐츠 원칙
assets/             # CSS, 모바일 내비 JS
```

## 빌드

```bash
python3 build.py
```

빌드 시 페이지별 본문 글자수 리포트가 출력됩니다.

## SEO 운영 원칙 (빌드에 강제됨)

- 본문 **2,000자 미만 페이지는 자동 `noindex`** 처리되고 sitemap에서 제외
- 지역은 대표 행정동 12개만 — 번호 행정동(개포1~4동, 역삼1·2동 등)은 통합, 개별 페이지 없음
- 역은 역 1개당 페이지 1개 — 환승역도 URL 하나, 노선별·출구별 페이지 없음
- **지역+역+테마 조합 페이지 없음** (도어웨이 방지) — 테마는 독립 페이지로만 운영
- 모든 지역·역 페이지의 description 은 **80자 이내**, 페이지별 고유 작성
- 실제 오프라인 사업장 주소가 없으므로 LocalBusiness 계열 Schema 미사용 (WebPage·Organization·FAQPage 만 사용)
- 상단/하위 메뉴와 푸터에 키워드·지역명·역명 대량 나열 없음
- 모든 페이지 본문은 페이지별 고유 작성 (지역명만 바꾼 복붙 없음)

## 배포 전 해야 할 일

1. `content/site.py`의 `BASE_URL`을 실제 도메인으로 변경
2. `python3 build.py` 재실행 (canonical·sitemap·robots.txt에 반영됨)
3. Google Search Console에 `sitemap.xml` 제출
