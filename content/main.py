# 메인 페이지 — 강남구 전체를 안내하고 행정동·역·테마 상세 페이지로 연결한다.
# 실제 오프라인 사업장 주소가 없으므로 LocalBusiness 계열 Schema는 쓰지 않고
# WebPage + Organization + FAQPage 만 사용한다.
from .site import BASE_URL, BRAND, PHONE, PHONE_DISPLAY
from .pricing import PRICING

_JSONLD = f"""<meta name="naver-site-verification" content="19ad8c6024a16da36f507ec74b89eb04256698d8" />
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "강남 출장마사지·강남구 홈타이 지역별 예약 안내",
  "url": "{BASE_URL}/",
  "description": "강남 출장마사지·홈타이 예약 전 행정동, 역세권, 이용 기준을 정리한 안내 페이지",
  "inLanguage": "ko-KR",
  "publisher": {{
    "@type": "Organization",
    "name": "{BRAND}",
    "url": "{BASE_URL}/",
    "telephone": "{PHONE}",
    "areaServed": {{
      "@type": "AdministrativeArea",
      "name": "서울특별시 강남구"
    }}
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "강남구 전지역 방문이 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "예약 시간, 정확한 위치, 배정 상황에 따라 가능 여부가 달라집니다. 지역별 안내에서 신사동, 압구정동, 청담동, 논현동, 삼성동, 역삼동, 대치동, 도곡동, 개포동, 일원동, 수서동, 세곡동 기준으로 확인할 수 있습니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "강남역이나 선릉역 근처도 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "주요 역세권은 역 상세 페이지에서 주변 생활권과 함께 안내합니다. 정확한 가능 여부는 예약 시 위치를 기준으로 확인합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "역삼1동과 역삼2동은 왜 따로 없나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "역삼1·2동, 삼성1·2동, 개포1~4동처럼 번호로 나뉜 동도 역삼동·삼성동·개포동 안내에서 함께 다룹니다. 어느 동에 계셔도 같은 기준으로 방문해 드립니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "당일 예약도 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "가능할 수 있지만 저녁 시간대와 주말은 문의가 많을 수 있어 사전 예약을 권장합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "홈타이는 출장마사지와 무엇이 다른가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "홈타이는 집에서 받는 타이마사지를 가리키는 말로 출장마사지의 대표 형태입니다. 오일 없이 편한 옷차림으로 받는 지압·스트레칭 구성이라 처음 이용하는 분도 부담이 적습니다."
      }}
    }}
  ]
}}
</script>
"""

_HERO = f"""<section class="hero">
  <div class="hero-inner">
    <p class="hero-badge">Premium Visiting Spa · 강남구 전지역</p>
    <h1>강남 출장마사지·강남구 홈타이<br>지역별 예약 안내</h1>
    <p class="hero-lead">샵까지 갈 필요 없이, 계신 곳에서 받는 프리미엄 방문 관리.<br>자택·오피스텔·숙소 어디든 전화 한 통이면 예약이 끝납니다.</p>
    <div class="hero-actions">
      <a class="hero-btn primary" href="tel:{PHONE}">📞 {PHONE_DISPLAY}</a>
      <a class="hero-btn" href="/courses/">코스 안내 보기</a>
    </div>
    <ul class="hero-stats">
      <li><strong>12개</strong><span>대표 행정동</span></li>
      <li><strong>28개</strong><span>역세권 안내</span></li>
      <li><strong>14개</strong><span>관리 테마</span></li>
      <li><strong>24시간</strong><span>예약 상담</span></li>
    </ul>
  </div>
</section>
"""

_BODY = f"""
<section id="why">
<h2>강남구에서 출장마사지를 찾는 이유</h2>
<p>강남 출장마사지를 찾는 분들은 대부분 지금 계신 곳에서 가까운 방문 가능 지역을 먼저 확인합니다. 강남구는 서울에서도 업무지구와 상권, 병원, 호텔, 고급 주거지가 한데 모인 지역입니다. 강남역과 역삼역 주변은 직장인 수요가 많고, 삼성역과 봉은사역 주변은 코엑스·무역센터 이용자가 많습니다. 압구정동·청담동·신사동은 고급 주거지와 상권이 함께 있고, 대치동과 도곡동은 학원가와 조용한 주거지가 중심입니다. 그래서 {BRAND}는 행정동과 지하철역을 함께 정리해, 어디에 계시든 가까운 지역 안내를 쉽게 찾으실 수 있도록 했습니다. 이 페이지에서 강남구 전체를 한눈에 보시고, 자세한 내용은 행정동별·역세권별·테마별 안내에서 확인하실 수 있습니다.</p>
</section>

<section id="hometai">
<h2>강남 홈타이 이용 전 확인할 사항</h2>
<p>강남 홈타이는 자택, 숙소, 사무실 인근에서 예약 가능 여부를 먼저 확인한 뒤 이용하는 방문형 관리 서비스입니다. 홈타이는 오일을 쓰지 않고 편한 옷차림으로 받는 지압·스트레칭 구성이라 샤워 부담이 적어 처음 이용하는 분이 시작하기 좋습니다. 출장마사지와 홈타이는 같은 방문형 서비스의 다른 이름에 가깝고, 코스와 시간 구성에 따라 선택하시면 됩니다. 예약 전에는 방문 가능 주소, 관리 가능 시간, 추가 이동비 여부, 결제 방식, 취소 기준, 서비스 범위를 먼저 확인하시는 것이 좋습니다. 관리 유형이 궁금하시면 <a href="/themes/thai/">타이마사지</a>와 <a href="/themes/swedish/">스웨디시</a> 안내를, 시간 구성은 <a href="/courses/#hometai">홈타이 코스</a>를 참고해 주세요.</p>
</section>

<section id="areas">
<h2>대표 행정동별 방문 가능 지역 안내</h2>
<p>강남구는 행정동이 번호로 잘게 나뉘어 있습니다. 개포1동부터 개포4동, 논현1·2동, 대치1·2·4동, 삼성1·2동, 역삼1·2동처럼 같은 생활권이 여러 동으로 갈리는데, {BRAND}는 이를 아래 12개 대표 행정동으로 묶어 안내합니다. 내가 사는 곳이 몇 동이든 헷갈릴 필요 없이, 대표 동 안내 한 곳에서 생활권 특징과 가까운 역, 방문 형태, 어울리는 관리까지 한 번에 확인하실 수 있습니다.</p>
<ul class="card-grid">
<li><a href="/gangnam/sinsa-dong-chuljangmassage/">신사동</a></li>
<li><a href="/gangnam/apgujeong-dong-chuljangmassage/">압구정동</a></li>
<li><a href="/gangnam/cheongdam-dong-chuljangmassage/">청담동</a></li>
<li><a href="/gangnam/nonhyeon-dong-chuljangmassage/">논현동</a></li>
<li><a href="/gangnam/samseong-dong-chuljangmassage/">삼성동</a></li>
<li><a href="/gangnam/yeoksam-dong-chuljangmassage/">역삼동</a></li>
<li><a href="/gangnam/daechi-dong-chuljangmassage/">대치동</a></li>
<li><a href="/gangnam/dogok-dong-chuljangmassage/">도곡동</a></li>
<li><a href="/gangnam/gaepo-dong-chuljangmassage/">개포동</a></li>
<li><a href="/gangnam/irwon-dong-chuljangmassage/">일원동</a></li>
<li><a href="/gangnam/suseo-dong-chuljangmassage/">수서동</a></li>
<li><a href="/gangnam/segok-dong-chuljangmassage/">세곡동</a></li>
</ul>
<p>강남구 전체 구조가 궁금하시면 <a href="/gangnam/">강남구 지역별 안내</a>에서 한눈에 확인하실 수 있습니다.</p>
</section>

<section id="stations">
<h2>지하철역으로 찾는 강남 방문 안내</h2>
<p>역 이름으로 위치를 설명하시는 편이 익숙하다면 지하철역별 안내가 편합니다. 강남구를 지나는 2·3·7·9호선과 수인분당선, 신분당선의 주요 역세권을 기준으로, 역마다 인근 생활권과 방문 조건을 정리했습니다. 강남역이나 선릉역처럼 여러 노선이 만나는 환승역도 어느 노선으로 오시든 한 곳에서 함께 안내해 드립니다. 아래는 대표 역세권이며, 28개 역 전체는 지하철역별 안내에서 확인하실 수 있습니다.</p>
<ul class="card-grid">
<li><a href="/gangnam/gangnam-station-chuljangmassage/">강남역</a></li>
<li><a href="/gangnam/sinnonhyeon-station-chuljangmassage/">신논현역</a></li>
<li><a href="/gangnam/seolleung-station-chuljangmassage/">선릉역</a></li>
<li><a href="/gangnam/samseong-station-chuljangmassage/">삼성역</a></li>
<li><a href="/gangnam/apgujeong-station-chuljangmassage/">압구정역</a></li>
<li><a href="/gangnam/cheongdam-station-chuljangmassage/">청담역</a></li>
<li><a href="/gangnam/daechi-station-chuljangmassage/">대치역</a></li>
<li><a href="/gangnam/suseo-station-chuljangmassage/">수서역</a></li>
</ul>
<p>역 전체 목록과 노선별 구분은 <a href="/gangnam/stations/">지하철역별 안내</a>에서 확인하세요.</p>
</section>

<section id="themes">
<h2>테마별 관리 안내</h2>
<p>테마별 안내에서는 관리 유형별 특징, 추천 대상, 예약 전 확인사항을 설명합니다. 테마는 각각 독립 페이지로 운영하며, 지역 페이지와 역 페이지에서는 관련 테마로 연결만 해 드립니다. 특정 역과 테마를 조합한 페이지는 운영하지 않으니, 원하시는 관리 유형을 먼저 고른 뒤 예약 시 위치를 알려주시면 됩니다.</p>
<ul class="card-grid">
<li><a href="/themes/swedish/">스웨디시</a></li>
<li><a href="/themes/lomilomi/">로미로미</a></li>
<li><a href="/themes/thai/">타이마사지</a></li>
<li><a href="/themes/chinese/">중국마사지</a></li>
<li><a href="/themes/aroma/">아로마테라피</a></li>
<li><a href="/themes/homecare/">홈케어</a></li>
<li><a href="/themes/hotel-style/">호텔식마사지</a></li>
<li><a href="/themes/foot/">발마사지</a></li>
<li><a href="/themes/sports/">스포츠·경락</a></li>
<li><a href="/themes/skincare/">스킨케어</a></li>
<li><a href="/themes/waxing/">왁싱</a></li>
<li><a href="/themes/couple/">커플 관리</a></li>
<li><a href="/themes/24hours/">24시간</a></li>
<li><a href="/themes/overnight/">수면 가능</a></li>
</ul>
</section>

<section id="check">
<h2>예약 전 꼭 확인해야 할 기준</h2>
<p>예약 전에는 방문 가능 주소, 관리 가능 시간, 추가 이동비, 결제 방식, 취소 기준, 서비스 범위를 먼저 확인해야 합니다. 강남구는 같은 구 안에서도 강남역·역삼역 업무권, 삼성역·봉은사역 전시권, 압구정·청담 상권, 수서·세곡 주거권의 이동 시간이 다를 수 있습니다. 특히 평일 저녁과 퇴근 시간, 주말 행사 시간대에는 방문 가능 시간이 달라질 수 있으므로 미리 연락 주시는 편이 좋습니다. 예약은 위치 확인, 시간 확인, 코스·인원 확인, 방문 가능 여부 안내, 예약 확정의 순서로 진행됩니다. 자세한 절차는 <a href="/reservation/">예약안내</a>에서 확인하실 수 있습니다.</p>
</section>

<section id="guide">
<h2>처음 오신 분을 위한 이용 안내</h2>
<p>이 페이지에서 강남구 전체를 살펴보시고, 거주하시거나 머무시는 곳에 맞춰 행정동별 안내나 지하철역별 안내로 들어가시면 됩니다. 신사동·압구정동·청담동·논현동·삼성동·역삼동·대치동·도곡동·개포동·일원동·수서동·세곡동 열두 개 동과 강남역·선릉역·삼성역·압구정역·수서역을 비롯한 역세권을 모두 다룹니다. 모든 안내는 과장 없이 사실대로 적었고, 불법적이거나 선정적인 요청은 어떤 경우에도 받지 않습니다. 처음 이용하신다면 <a href="/massage/">강남 출장마사지 안내</a>와 <a href="/guide/">이용가이드</a>를 먼저 읽어보시기를 권합니다.</p>
</section>

<section id="faq">
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>강남구 전지역 방문이 가능한가요?</h3>
<p>예약 시간, 정확한 위치, 배정 상황에 따라 가능 여부가 달라집니다. 지역별 안내에서 12개 대표 행정동 기준으로 확인할 수 있습니다.</p>
</div>
<div class="faq-item">
<h3>강남역이나 선릉역 근처도 가능한가요?</h3>
<p>주요 역세권은 역 상세 페이지에서 주변 생활권과 함께 안내합니다. 정확한 가능 여부는 예약 시 위치를 기준으로 확인합니다.</p>
</div>
<div class="faq-item">
<h3>역삼1동과 역삼2동은 왜 따로 없나요?</h3>
<p>역삼1·2동, 삼성1·2동, 개포1~4동처럼 번호로 나뉜 동도 역삼동·삼성동·개포동 안내에서 함께 다룹니다. 어느 동에 계셔도 같은 기준으로 방문해 드립니다.</p>
</div>
<div class="faq-item">
<h3>홈타이는 출장마사지와 무엇이 다른가요?</h3>
<p>홈타이는 집에서 받는 타이마사지를 가리키는 말로 출장마사지의 대표 형태입니다. 오일 없이 편한 옷차림으로 받아 처음 이용하는 분도 부담이 적습니다.</p>
</div>
</section>

{PRICING}
<section id="contact" class="cta">
<h2>예약문의</h2>
<p>강남구 방문 관리 예약과 상담은 전화로 가장 빠르게 진행됩니다. 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

PAGE = {
    "path": "",
    "title": "강남 출장마사지｜강남구 홈타이 지역별 예약 안내",
    "desc": "강남 출장마사지·홈타이 예약 전 행정동, 역세권, 이용 기준을 정리했습니다.",
    "h1": "강남 출장마사지·강남구 홈타이 지역별 예약 안내",
    "body": _BODY,
    "extra_head": _JSONLD,
    "breadcrumb": [],
    "hero": _HERO,
}
