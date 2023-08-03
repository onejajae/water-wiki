<script>
  export let supplier
</script>

<dl class="row">
  <!-- <dd>
    <img src="">
  </dd>
  <dd>
    <div id="kakaomap" class="col" style="height: 400px;">
      <script>
        var mapContainer = document.getElementById('kakaomap')
        var mapOptions = {
          center: new kakao.maps.LatLng(33.450701, 126.570667),
          level: 4
        }
        var map = new kakao.maps.Map(mapContainer, mapOptions)

      </script>
    </div>
  </dd>
  <hr> -->
  <dt class="col-sm-4">업체명</dt>
  <dd class="col-sm-8">{supplier.name}</dd>
  <hr>
  <dt class="col-sm-4">주소</dt>
  <dd class="col-sm-8">{supplier.address}</dd>
  <hr>
  <dt class="col-sm-4">운영 현황</dt>
  <dd class="col-sm-8">
    {#if supplier.is_running}
    <span class="badge rounded-pill text-bg-success">영업 중</span>
  {:else}
    <span class="badge rounded-pill text-bg-secondary">휴업 중</span>
  {/if}
  </dd>
  <hr>
  <dt class="col-sm-4">대표자명</dt>
  <dd class="col-sm-8">{supplier.ceo_name}</dd>
  <!-- <hr>
  <dt class="col-sm-4">전화번호</dt>
  <dd class="col-sm-8">{supplier.phone_number}</dd> -->
  <hr>
  <dt class="col-sm-4">허가일자</dt>
  <dd class="col-sm-8">{supplier.first_permit_datetime}</dd>
  <hr>
  <dt class="col-sm-4">일일 취수 허용량</dt>
  <dd class="col-sm-8">{supplier.intakes}톤</dd>
  <hr>
  <dt class="col-sm-4">취수공수</dt>
  <dd class="col-sm-8">{supplier.pipes}</dd>
  <!-- <hr>
  <dt class="col-sm-4">웹 사이트 </dt>
  <dd class="col-sm-8">바로가기</dd> -->
</dl>