# 강남구 지역 허브 — 대표 행정동 12개로 들어가는 입구.
# areas.py(동 상세)와 분리해 두어 동 본문이 갱신돼도 허브는 독립적으로 유지된다.
from .pricing import PRICING
from .site import PHONE, PHONE_DISPLAY

_CTA = f"""
<section class="cta">
<h2>예약문의</h2>
<p>방문 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

_HUB_BODY = """
<p class="lead">강남구 방문 관리는 열두 개 대표 행정동을 기준으로 안내합니다. 거주하시는 행정동이 숫자로 나뉘어 있어도 아래 대표 동 페이지에서 모든 정보를 확인하실 수 있습니다.</p>

<section>
<h2>강남구 지역 안내 구성</h2>
<p>강남구는 법정동 기준으로 신사동, 논현동, 압구정동, 청담동, 삼성동, 대치동, 역삼동, 도곡동, 개포동, 일원동, 수서동, 세곡동으로 이루어져 있고, 행정동은 그보다 잘게 나뉘어 있습니다. 예를 들어 개포동은 개포1동부터 개포4동까지, 역삼동은 역삼1·2동, 삼성동은 삼성1·2동, 논현동은 논현1·2동, 대치동은 대치1·2·4동, 도곡동은 도곡1·2동, 일원동은 일원본동과 일원1동으로 나뉩니다. 이 사이트에서는 번호가 붙은 행정동을 각각 만들지 않고 위 열두 개 대표 행정동 페이지로 통합해 안내합니다. 행정동 단위로 페이지를 쪼개면 같은 생활권을 두고 비슷한 설명이 반복될 수밖에 없고, 이용자 입장에서도 어느 페이지를 봐야 할지 혼란스럽기 때문입니다. 방문 가능 여부는 행정동 경계가 아니라 실제 위치와 예약 시간으로 판단하므로, 대표 동 기준 안내가 실제 이용 흐름과도 일치합니다. 행정동 이름으로 검색해 들어오셨더라도 필요한 내용은 모두 대표 동 페이지 안에 있습니다.</p>
</section>

<section>
<h2>한강변·상권 생활권</h2>
<ul class="card-grid">
<li><a href="/gangnam/sinsa-dong-chuljangmassage/">신사동</a></li>
<li><a href="/gangnam/apgujeong-dong-chuljangmassage/">압구정동</a></li>
<li><a href="/gangnam/cheongdam-dong-chuljangmassage/">청담동</a></li>
<li><a href="/gangnam/nonhyeon-dong-chuljangmassage/">논현동</a></li>
</ul>
<p>신사동은 가로수길과 신사역 패션 상권, 압구정동은 갤러리아와 로데오거리, 청담동은 명품거리와 고급 빌라촌, 논현동은 가구거리와 영동시장·먹자골목이 중심입니다. 한강과 가까운 강남 북부 생활권으로 고급 주거와 상권이 함께 있어, 자택과 주상복합 방문은 물론 상권 인근 숙소 방문 문의도 많은 지역입니다.</p>
</section>

<section>
<h2>업무·전시 생활권</h2>
<ul class="card-grid">
<li><a href="/gangnam/samseong-dong-chuljangmassage/">삼성동</a></li>
<li><a href="/gangnam/yeoksam-dong-chuljangmassage/">역삼동</a></li>
</ul>
<p>삼성동은 코엑스·무역센터·현대백화점을 낀 전시·업무권이고, 역삼동은 강남역과 테헤란로를 따라 오피스와 오피스텔이 밀집한 업무권입니다. 직장인과 출장 방문 수요가 많아 평일 저녁과 심야, 숙소 방문 비중이 높은 것이 특징입니다.</p>
</section>

<section>
<h2>학원가·고급 주거 생활권</h2>
<ul class="card-grid">
<li><a href="/gangnam/daechi-dong-chuljangmassage/">대치동</a></li>
<li><a href="/gangnam/dogok-dong-chuljangmassage/">도곡동</a></li>
</ul>
<p>대치동은 은마아파트와 대치동 학원가를 중심으로 한 교육·주거 중심지이고, 도곡동은 타워팰리스와 도곡렉슬 등 고급 주상복합과 매봉산 자락 주거지가 어우러진 지역입니다. 학사 일정에 맞춘 예약과 가족 단위 자택 방문이 많습니다.</p>
</section>

<section>
<h2>재건축·병원·환승 생활권</h2>
<ul class="card-grid">
<li><a href="/gangnam/gaepo-dong-chuljangmassage/">개포동</a></li>
<li><a href="/gangnam/irwon-dong-chuljangmassage/">일원동</a></li>
<li><a href="/gangnam/suseo-dong-chuljangmassage/">수서동</a></li>
<li><a href="/gangnam/segok-dong-chuljangmassage/">세곡동</a></li>
</ul>
<p>개포동은 양재천과 대모산을 낀 재건축 대단지, 일원동은 삼성서울병원과 대모산 생활권, 수서동은 SRT 수서역 복합환승권, 세곡동은 세곡지구·자곡동 보금자리 주거지입니다. 강남 남부의 주거 중심 생활권으로 가족 단위 방문과 병원 인근 회복 관리, 환승객 숙소 방문이 고루 섞입니다.</p>
</section>

<section>
<h2>지역과 역세권을 함께 확인하세요</h2>
<p>강남구는 2·3·7·9호선과 수인분당선, 신분당선이 격자처럼 지나는 지역이라 동 기준보다 역 기준이 익숙한 분들도 많습니다. 강남역, 선릉역, 삼성역, 압구정역처럼 역 인근 위치에서 예약하실 때는 <a href="/gangnam/stations/">지하철역별 안내</a>를 함께 확인해 보세요. 역 페이지에서는 해당 역세권의 생활권과 인접 동을 연결해 설명합니다. 다만 역과 동, 테마를 조합한 별도 페이지는 운영하지 않으므로, 원하시는 관리 유형은 <a href="/themes/">테마별 안내</a>에서 따로 확인하시면 됩니다. 동 페이지와 역 페이지 중 어느 쪽을 보셔도 예약 기준은 같으니, 본인에게 익숙한 기준으로 보시면 됩니다.</p>
</section>

<section>
<h2>예약 전 참고사항</h2>
<p>어느 동이든 예약 절차는 동일합니다. 위치 확인, 시간 확인, 코스·인원 확인, 방문 가능 여부 안내, 예약 확정 순서로 진행되며, 저녁 시간대와 주말은 문의가 몰릴 수 있어 미리 연락 주시는 편이 좋습니다. 아파트와 주상복합은 동·호수와 공동현관 출입 방법을, 오피스텔과 숙소는 건물 출입 안내를 함께 알려주시면 방문이 한층 매끄럽습니다. 강남구 경계와 맞닿은 서초구, 송파구 방면 주소도 위치에 따라 방문이 가능할 수 있으니 전화로 확인해 주세요. 자세한 준비사항은 <a href="/guide/">이용가이드</a>에서 확인하실 수 있습니다.</p>
</section>

<section>
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>우리 동네 행정동 이름이 안 보여요.</h3>
<p>숫자가 붙은 행정동은 모두 대표 동 페이지에 통합되어 있습니다. 예를 들어 개포2동은 개포동 페이지, 역삼1동은 역삼동 페이지를 보시면 됩니다.</p>
</div>
<div class="faq-item">
<h3>동 경계가 애매한 위치는 어떻게 하나요?</h3>
<p>경계 지역은 어느 동 페이지를 보셔도 무방합니다. 실제 방문은 주소 기준으로 진행되므로 예약 전화에서 정확한 주소만 알려주시면 됩니다.</p>
</div>
</section>
""" + PRICING + _CTA

HUB = {
    "path": "gangnam/",
    "title": "강남구 출장마사지·홈타이 | 지역별 방문 관리 안내",
    "desc": "강남구 12개 대표 행정동 출장마사지·홈타이 안내입니다. 동별 생활권과 방문 기준을 확인하세요.",
    "h1": "강남구 지역별 안내",
    "body": _HUB_BODY,
    "breadcrumb": [("지역별 안내", None)],
}
