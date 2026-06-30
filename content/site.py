# 사이트 공통 설정
# 배포 도메인(넷리파이)으로 확정.
BASE_URL = "https://gangnam-swedish-massage.netlify.app"

BRAND = "간다GO"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 검색엔진 사이트 소유확인 코드
NAVER_VERIFY = "6a1f4db7cccf19b5e7fb851543e61a73b6bebe3d"

# 통합 평점 — Service/AggregateRating 스키마 공용. 후기 페이지 노출 후기 수와 일치시킨다.
RATING_VALUE = "4.8"
# REVIEWS 항목 수로 자동 계산되지만 import 순환을 피하려 정적으로 둔다(아래 REVIEWS와 일치).
REVIEW_COUNT = "12"

# 코스별 기본 요금(원) — Offer 스키마와 요금 블록 공용.
OFFERS = [
    ("60분 코스", "90000", "기본 컨디션·릴랙스 케어"),
    ("90분 코스", "150000", "아로마 포함 추천 구성"),
    ("120분 코스", "180000", "전신 집중 프리미엄 케어"),
]

# IndexNow 키 — Bing·네이버·Yandex 즉시 색인 통보용.
# 빌드 시 루트에 "{INDEXNOW_KEY}.txt" 파일이 생성되며 그 안에 이 키가 들어간다.
INDEXNOW_KEY = "a20c79d068cef7caab0b163f8e33d4f1"

# 상단 메뉴 — 하위 메뉴에는 키워드를 반복하지 않고 지역명·역명만 표시한다.
# 12개 행정동 전체는 지역 허브에서, 28개 역 전체는 역 허브에서 안내하고
# 메뉴에는 대표 항목만 노출해 키워드 대량 나열을 피한다.
NAV = [
    ("홈", "/", []),
    ("강남 출장마사지", "/massage/", [
        ("출장마사지 안내", "/massage/#service"),
        ("홈타이 안내", "/massage/#hometai"),
        ("전지역 방문 안내", "/massage/#coverage"),
        ("지하철역 인근 안내", "/massage/#stations"),
        ("예약 가능 시간", "/massage/#hours"),
        ("코스 선택 안내", "/massage/#course"),
        ("이용 전 확인사항", "/massage/#check"),
        ("위생·안전 안내", "/massage/#safety"),
        ("자주 묻는 질문", "/massage/#faq"),
    ]),
    ("지역별 안내", "/gangnam/", [
        ("강남구 전체", "/gangnam/"),
        ("신사동", "/gangnam/sinsa-dong-chuljangmassage/"),
        ("압구정동", "/gangnam/apgujeong-dong-chuljangmassage/"),
        ("청담동", "/gangnam/cheongdam-dong-chuljangmassage/"),
        ("논현동", "/gangnam/nonhyeon-dong-chuljangmassage/"),
        ("삼성동", "/gangnam/samseong-dong-chuljangmassage/"),
        ("역삼동", "/gangnam/yeoksam-dong-chuljangmassage/"),
        ("대치동", "/gangnam/daechi-dong-chuljangmassage/"),
        ("도곡동", "/gangnam/dogok-dong-chuljangmassage/"),
        ("개포동", "/gangnam/gaepo-dong-chuljangmassage/"),
        ("일원동", "/gangnam/irwon-dong-chuljangmassage/"),
        ("수서동", "/gangnam/suseo-dong-chuljangmassage/"),
        ("세곡동", "/gangnam/segok-dong-chuljangmassage/"),
    ]),
    ("지하철역별 안내", "/gangnam/stations/", [
        ("역 전체", "/gangnam/stations/"),
        ("강남역", "/gangnam/gangnam-station-chuljangmassage/"),
        ("신논현역", "/gangnam/sinnonhyeon-station-chuljangmassage/"),
        ("선릉역", "/gangnam/seolleung-station-chuljangmassage/"),
        ("역삼역", "/gangnam/yeoksam-station-chuljangmassage/"),
        ("삼성역", "/gangnam/samseong-station-chuljangmassage/"),
        ("압구정역", "/gangnam/apgujeong-station-chuljangmassage/"),
        ("청담역", "/gangnam/cheongdam-station-chuljangmassage/"),
        ("신사역", "/gangnam/sinsa-station-chuljangmassage/"),
        ("대치역", "/gangnam/daechi-station-chuljangmassage/"),
        ("도곡역", "/gangnam/dogok-station-chuljangmassage/"),
        ("수서역", "/gangnam/suseo-station-chuljangmassage/"),
    ]),
    ("테마별 안내", "/themes/", [
        ("전체 테마", "/themes/"),
        ("스웨디시", "/themes/swedish/"),
        ("로미로미", "/themes/lomilomi/"),
        ("타이마사지", "/themes/thai/"),
        ("중국마사지", "/themes/chinese/"),
        ("아로마테라피", "/themes/aroma/"),
        ("홈케어", "/themes/homecare/"),
        ("호텔식마사지", "/themes/hotel-style/"),
        ("발마사지", "/themes/foot/"),
        ("스포츠·경락", "/themes/sports/"),
        ("스킨케어", "/themes/skincare/"),
        ("왁싱", "/themes/waxing/"),
        ("커플 관리", "/themes/couple/"),
        ("24시간", "/themes/24hours/"),
        ("수면 가능", "/themes/overnight/"),
    ]),
    ("코스안내", "/courses/", [
        ("전체 코스", "/courses/"),
        ("피로 회복 관리", "/courses/#recovery"),
        ("아로마 관리", "/courses/#aroma"),
        ("스포츠 관리", "/courses/#sports"),
        ("홈타이 코스", "/courses/#hometai"),
        ("커플·가족 방문 관리", "/courses/#couple"),
        ("기업·단체 방문 관리", "/courses/#group"),
        ("가격 안내", "/courses/#price"),
        ("코스 선택 가이드", "/courses/#guide"),
    ]),
    ("예약안내", "/reservation/", [
        ("예약 방법", "/reservation/#how"),
        ("예약 가능 시간", "/reservation/#hours"),
        ("방문 가능 장소", "/reservation/#place"),
        ("결제 안내", "/reservation/#payment"),
        ("변경·취소 안내", "/reservation/#change"),
        ("예약 전 체크사항", "/reservation/#check"),
    ]),
    ("이용가이드", "/guide/", [
        ("처음 이용하시는 분", "/guide/#first"),
        ("방문 전 준비사항", "/guide/#prepare"),
        ("위생 및 안전 기준", "/guide/#hygiene"),
        ("관리 후 주의사항", "/guide/#after"),
        ("금지행위 안내", "/guide/#prohibited"),
        ("이용 FAQ", "/guide/#faq"),
    ]),
    ("매거진", "/magazine/", [
        ("전체 글", "/magazine/"),
        ("마사지 비교 가이드", "/magazine/swedish-vs-thai/"),
        ("처음 이용 가이드", "/magazine/first-time-guide/"),
        ("수면과 마사지", "/magazine/sleep-and-massage/"),
        ("운동 후 회복", "/magazine/post-workout-timing/"),
        ("어깨·목 결림 관리", "/magazine/neck-shoulder-care/"),
        ("부모님 선물 가이드", "/magazine/parents-gift/"),
    ]),
    ("후기", "/reviews/", [
        ("전체 후기", "/reviews/"),
        ("지역별 후기", "/reviews/#area"),
        ("역세권 후기", "/reviews/#station"),
        ("후기 작성 안내", "/reviews/#write"),
    ]),
    ("고객센터", "/support/", [
        ("공지사항", "/support/#notice"),
        ("자주 묻는 질문", "/support/#faq"),
        ("1:1 문의", "/support/#contact"),
        ("제휴·기업 문의", "/support/#biz"),
        ("개인정보처리방침", "/support/privacy/"),
        ("이용약관", "/support/terms/"),
    ]),
]
