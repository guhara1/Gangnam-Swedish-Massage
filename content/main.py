# 메인 페이지 — 허브 역할. 모든 키워드를 밀어 넣지 않고 상세 페이지로 연결한다.
# 실제 오프라인 사업장 주소가 없으므로 LocalBusiness 계열 Schema는 쓰지 않고
# WebPage + Organization + FAQPage 만 사용한다.
from .site import BASE_URL, BRAND, PHONE, PHONE_DISPLAY
from .pricing import PRICING

_JSONLD = f"""<script type="application/ld+json">
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
        "text": "번호가 붙은 행정동은 역삼동, 삼성동, 개포동처럼 대표 행정동 한 페이지로 통합해 중복 페이지 위험을 줄입니다."
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
<p>강남 출장마사지를 찾는 분들은 대부분 지금 계신 곳에서 가까운 방문 가능 지역을 먼저 확인합니다. 강남구는 서울에서도 업무지구와 상권, 병원, 호텔, 고급 주거지가 한데 모인 지역입니다. 강남역과 역삼역 주변은 직장인 수요가 많고, 삼성역과 봉은사역 주변은 코엑스·무역센터 이용자가 많습니다. 압구정동·청담동·신사동은 고급 주거지와 상권이 함께 있고, 대치동과 도곡동은 학원가와 주거권 중심의 검색 의도가 강합니다. 그래서 {BRAND}는 행정동과 지하철역을 함께 정리하는 구조로 강남 홈타이 안내를 구성했습니다. 이 페이지는 강남구 전체 구조를 설명하는 허브이며, 자세한 내용은 행정동별·역세권별·테마별 안내 페이지에서 확인하실 수 있습니다.</p>
</section>

<section id="hometai">
<h2>강남 홈타이 이용 전 확인할 사항</h2>
<p>강남 홈타이는 자택, 숙소, 사무실 인근에서 예약 가능 여부를 먼저 확인한 뒤 이용하는 방문형 관리 서비스입니다. 홈타이는 오일을 쓰지 않고 편한 옷차림으로 받는 지압·스트레칭 구성이라 샤워 부담이 적어 처음 이용하는 분이 시작하기 좋습니다. 출장마사지와 홈타이는 같은 방문형 서비스의 다른 이름에 가깝고, 코스와 시간 구성에 따라 선택하시면 됩니다. 예약 전에는 방문 가능 주소, 관리 가능 시간, 추가 이동비 여부, 결제 방식, 취소 기준, 서비스 범위를 먼저 확인하시는 것이 좋습니다. 관리 유형이 궁금하시면 <a href="/themes/thai/">타이마사지</a>와 <a href="/themes/swedish/">스웨디시</a> 안내를, 시간 구성은 <a href="/courses/#hometai">홈타이 코스</a>를 참고해 주세요.</p>
</section>

<section id="areas">
<h2>대표 행정동별 방문 가능 지역 안내</h2>
<p>강남구 안내에서 가장 중요한 원칙은 행정동을 너무 잘게 쪼개지 않는 것입니다. 개포1동부터 개포4동, 논현1·2동, 대치1·2·4동, 삼성1·2동, 역삼1·2동처럼 번호가 붙은 행정동을 각각 만들면 페이지 수는 늘지만 내용이 비슷해질 위험이 큽니다. 그래서 번호 동은 모두 통합해 아래 12개 대표 행정동 페이지로만 안내합니다. 각 페이지에서는 생활권 특징, 가까운 역세권, 방문 형태, 어울리는 테마를 동마다 고유하게 설명합니다.</p>
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
<h2>지하철역별 출장마사지 지역 SEO 구조</h2>
<p>지하철역별 안내는 강남구를 지나는 2·3·7·9호선과 수인분당선, 신분당선의 주요 역세권을 기준으로 구성합니다. 강남역 출장마사지, 신논현역 출장마사지, 선릉역 출장마사지, 삼성역 출장마사지처럼 실제 검색어에 가까운 제목을 사용하되, 같은 역을 노선별로 중복해서 만들지는 않습니다. 예를 들어 강남역은 2호선과 신분당선이 만나지만 페이지는 하나만 두고 본문에서 환승역 특징을 설명합니다. 아래는 대표 역세권이며, 28개 역 전체는 역 허브에서 확인하실 수 있습니다.</p>
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
<h2>강남 출장마사지 사이트 이용 가이드</h2>
<p>이 사이트는 메인페이지가 강남구 전체 안내를 맡고, 대표 행정동 페이지가 신사동·압구정동·청담동·논현동·삼성동·역삼동·대치동·도곡동·개포동·일원동·수서동·세곡동 검색을, 역세권 페이지가 강남역·신논현역·선릉역·삼성역·압구정역·수서역 같은 실제 검색 수요를 담당하도록 설계했습니다. 사이트 전체 문구는 과장된 표현보다 신뢰를 주는 안내형 문장으로 구성하며, 불법 서비스나 선정적 표현, 허위 후기, 과도한 할인 문구는 사용하지 않습니다. 처음 이용하신다면 <a href="/massage/">강남 출장마사지 안내</a>와 <a href="/guide/">이용가이드</a>를 먼저 읽어보시기를 권합니다.</p>
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
<p>번호가 붙은 행정동은 역삼동, 삼성동, 개포동처럼 대표 행정동 한 페이지로 통합해 중복 페이지 위험을 줄입니다.</p>
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
