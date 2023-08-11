<script>
  import dayjs from "dayjs";
  export let vendor;
</script>

<div class="card p-4 pb-2 mb-4">
  <dl class="row">
    <!-- map start -->
    <dd>
      <div id="kakaomap" class="col" style="height: 300px;">
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
    <hr class="mt-3">
    <!-- map end -->
    <dt class="col-sm-4">업체명</dt>
    <dd class="col-sm-8">{vendor.name}</dd>
    <hr>
    <dt class="col-sm-4">주소</dt>
    <dd class="col-sm-8">{vendor.address}</dd>
    <hr>
    <dt class="col-sm-4">대표자명</dt>
    <dd class="col-sm-8">{vendor.ceo_name}</dd>
    <!-- <hr>
    <dt class="col-sm-4">전화번호</dt>
    <dd class="col-sm-8">{vendor.phone_number}</dd> -->
    <hr>
    <dt class="col-sm-4">신고일자</dt>
    <dd class="col-sm-8">{dayjs(vendor.declare_datetime).format("YYYY년 MM월 DD일")}</dd>
    <!-- <hr>
    <dt class="col-sm-4">웹 사이트 </dt>
    <dd class="col-sm-8">바로가기</dd> -->
  </dl>
</div>