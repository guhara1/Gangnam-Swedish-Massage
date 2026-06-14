# 지하철역별 안내 — 허브 1개 + 역 28개(_stations_a 14 + _stations_b 14).
# 환승역도 URL은 하나만 사용한다. 출구별·노선별·역+테마 조합 페이지는 만들지 않는다.
from .pricing import PRICING
from .site import PHONE, PHONE_DISPLAY
from ._stations_a import STATIONS as STATIONS_A
from ._stations_b import STATIONS as STATIONS_B

_CTA = f"""
<section class="cta">
<h2>예약문의</h2>
<p>역 인근 위치와 희망 시간을 알려주시면 방문 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

_HUB_BODY = """
<p class="lead">강남구를 지나는 2·3·7·9호선과 수인분당선, 신분당선의 주요 역세권을 기준으로 방문 관리를 안내합니다. 환승역은 노선이 여러 개라도 페이지는 하나만 운영합니다.</p>

<section>
<h2>강남구를 지나는 지하철 노선</h2>
<p>강남구는 서울에서 지하철 노선이 가장 촘촘하게 얽힌 지역입니다. 2호선이 강남대로와 테헤란로를 따라 강남역·역삼역·선릉역·삼성역을 잇고, 3호선이 신사역부터 압구정·대치·일원·수서까지 남북으로 흐르며, 7호선·9호선·수인분당선·신분당선이 그 사이를 격자처럼 채웁니다. 강남역·선릉역·도곡역·수서역처럼 여러 노선이 만나는 환승역도, 어느 노선을 타고 오시든 한곳에서 함께 안내해 드립니다. 어느 역에서 출발하시든 예약 절차와 이용 기준은 같으니, 익숙한 역을 기준으로 보시면 됩니다. 강남구는 업무권과 상권, 학원가, 재건축 단지, 병원, 환승 거점이 한 구 안에 모여 있어 같은 역세권이라도 시간대별 예약 흐름이 크게 다릅니다. 그래서 아래에서는 역을 다섯 개 권역으로 나눠 정리했으니, 본인 생활 패턴과 가까운 역을 고르시면 필요한 정보를 더 빨리 찾으실 수 있습니다. 각 역 안내에서는 역세권 분위기, 인근 대표 행정동, 방문 형태, 예약 시 참고사항을 역마다 자세히 설명합니다.</p>
</section>

<section>
<h2>강남대로·테헤란로 업무 상권 역</h2>
<p>강남구의 한복판을 가르는 강남대로와 테헤란로 라인입니다. <a href="/gangnam/gangnam-station-chuljangmassage/">강남역</a>, <a href="/gangnam/sinnonhyeon-station-chuljangmassage/">신논현역</a>, <a href="/gangnam/yeoksam-station-chuljangmassage/">역삼역</a>, <a href="/gangnam/seolleung-station-chuljangmassage/">선릉역</a>, <a href="/gangnam/samseong-station-chuljangmassage/">삼성역</a>이 여기에 속합니다. 오피스와 호텔, 오피스텔이 밀집한 구간이라 회식·모임 이후의 심야 방문, 출장으로 머무는 숙소 방문 문의가 가장 많은 라인입니다.</p>
</section>

<section>
<h2>압구정·청담·신사 상권 역</h2>
<p>한강과 가까운 강남 북부의 패션·상권 라인입니다. <a href="/gangnam/sinsa-station-chuljangmassage/">신사역</a>의 가로수길, <a href="/gangnam/apgujeong-station-chuljangmassage/">압구정역</a>과 <a href="/gangnam/apgujeongrodeo-station-chuljangmassage/">압구정로데오역</a>의 로데오거리, <a href="/gangnam/cheongdam-station-chuljangmassage/">청담역</a>의 명품거리가 이어집니다. 고급 주거와 주상복합이 많아 자택 방문 비중이 높고, <a href="/gangnam/gangnam-gu-office-station-chuljangmassage/">강남구청역</a>, <a href="/gangnam/hakdong-station-chuljangmassage/">학동역</a>, <a href="/gangnam/eonju-station-chuljangmassage/">언주역</a>, 그리고 <a href="/gangnam/nonhyeon-station-chuljangmassage/">논현역</a>까지 논현·청담 생활권을 함께 묶어 안내합니다.</p>
</section>

<section>
<h2>삼성·코엑스 전시 업무권 역</h2>
<p>코엑스와 무역센터를 중심으로 한 전시·업무권입니다. <a href="/gangnam/samseong-station-chuljangmassage/">삼성역</a>, <a href="/gangnam/samseong-jungang-station-chuljangmassage/">삼성중앙역</a>, <a href="/gangnam/bongeunsa-station-chuljangmassage/">봉은사역</a>, 그리고 삼성동과 역삼동 사이의 <a href="/gangnam/seonjeongneung-station-chuljangmassage/">선정릉역</a>이 이 구간입니다. 전시·행사 일정에 맞춰 호텔과 숙소 방문이 몰리는 시기가 뚜렷한 것이 특징입니다.</p>
</section>

<section>
<h2>대치·도곡 학원가·주거권 역</h2>
<p>학원가와 고급 주거가 함께 있는 강남 중부 라인입니다. <a href="/gangnam/hanti-station-chuljangmassage/">한티역</a>, <a href="/gangnam/daechi-station-chuljangmassage/">대치역</a>, <a href="/gangnam/hangnyeoul-station-chuljangmassage/">학여울역</a>이 대치동 학원가와 주거권을, <a href="/gangnam/dogok-station-chuljangmassage/">도곡역</a>, <a href="/gangnam/maebong-station-chuljangmassage/">매봉역</a>, <a href="/gangnam/yangjae-station-chuljangmassage/">양재역</a>이 도곡동 생활권을 지납니다. 학사 일정과 가족 단위 자택 방문 문의가 많은 구간입니다.</p>
</section>

<section>
<h2>개포·일원·수서 주거권 역</h2>
<p>대모산과 양재천을 끼고 재건축 단지와 병원, 환승 거점이 모인 강남 남부 라인입니다. <a href="/gangnam/guryong-station-chuljangmassage/">구룡역</a>, <a href="/gangnam/gaepo-dong-station-chuljangmassage/">개포동역</a>이 개포 재건축 단지를, <a href="/gangnam/daemosan-station-chuljangmassage/">대모산입구역</a>, <a href="/gangnam/daecheong-station-chuljangmassage/">대청역</a>, <a href="/gangnam/irwon-station-chuljangmassage/">일원역</a>이 일원동과 삼성서울병원 생활권을, <a href="/gangnam/suseo-station-chuljangmassage/">수서역</a>이 SRT 환승권을 지납니다. 가족 자택 방문과 병원 인근 회복 관리, 환승객 숙소 방문이 고루 섞입니다.</p>
</section>

<section>
<h2>역 기준으로 예약하실 때</h2>
<p>역 이름은 위치를 설명하는 좋은 기준이지만, 실제 방문에는 정확한 주소가 필요합니다. 예약 전화에서 가까운 역과 함께 건물명 또는 도로명 주소를 알려주시면 도착 시간을 정확히 안내해 드립니다. 거주 지역 기준 안내가 편하시면 <a href="/gangnam/">지역별 안내</a>를, 관리 유형이 먼저 궁금하시면 <a href="/themes/">테마별 안내</a>를 확인해 주세요. 어느 역에서 출발하든 예약 절차와 이용 기준은 동일하며, 두 역 사이 애매한 위치라면 둘 중 어느 페이지를 보셔도 무방합니다. 최종 안내는 언제나 주소 기준으로 이루어집니다.</p>
</section>

<section>
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>역에서 만나서 같이 이동하는 방식인가요?</h3>
<p>아니요, 관리사가 장비를 챙겨 알려주신 주소로 직접 방문합니다. 역은 위치를 설명하는 기준일 뿐 만남 장소가 아닙니다.</p>
</div>
<div class="faq-item">
<h3>환승역인데 무슨 호선 쪽인지 말해야 하나요?</h3>
<p>노선 구분은 필요 없습니다. 환승역 페이지는 하나로 통합되어 있고, 방문은 주소 기준으로 진행됩니다.</p>
</div>
<div class="faq-item">
<h3>역에서 먼 곳은 안 되나요?</h3>
<p>역과의 거리는 가능 여부와 무관합니다. 강남구 전지역이 방문 범위이며, 역 페이지는 위치 설명을 돕는 안내일 뿐입니다.</p>
</div>
</section>
""" + PRICING + _CTA

HUB = {
    "path": "gangnam/stations/",
    "title": "강남 지하철역 출장마사지·홈타이 | 역세권 방문 관리 안내",
    "desc": "강남구 28개 역세권 출장마사지·홈타이 안내입니다. 강남역, 선릉역, 삼성역 등 역별 방문 기준을 확인하세요.",
    "h1": "강남구 지하철역별 안내",
    "body": _HUB_BODY,
    "breadcrumb": [("지하철역별 안내", None)],
}

PAGES = [HUB] + STATIONS_A + STATIONS_B
