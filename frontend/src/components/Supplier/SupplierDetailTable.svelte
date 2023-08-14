<script>
  import { onMount } from "svelte";
  import dayjs from "dayjs";
  export let supplier

  const supplierPosition = new naver.maps.LatLng(supplier.loc_y, supplier.loc_x)
  const supplierPositionEPSG3857 = naver.maps.TransCoord.fromLatLngToEPSG3857(supplierPosition)

  const infoWindowContent = [
    `<div class="m-3">`,
    `<a href="http://map.naver.com/v5/search?c=${supplierPositionEPSG3857.x},${supplierPositionEPSG3857.y},18,0,0,2,dh" class="link-offset-2 link-underline link-underline-opacity-0" target="_blank" rel="noopener noreferrer">`,
    `<h5 class="mb-0">${supplier.name}</h5>`,
    `<p class="link-dark">${supplier.address}</p>`,
    `</a></div>`,
  ].join('')

  const mapOptions = {
    center: supplierPosition,
    mapTypeId: "hybrid",
    zoom: 14,
    draggable: false,
    pinchZoom: false,
    scrollWheel: false,
    disableDoubleClickZoom: true,
    disableDoubleTapZoom: true,
    logoControl: false,
    mapDataControl: false,
    scaleControl: false
  }
  const infoWindow = new naver.maps.InfoWindow({
    content: infoWindowContent,
    anchorSize: new naver.maps.Size(20, 20),
  })
  const marker = new naver.maps.Marker({
    position: supplierPosition,
  })

  onMount(() => {
    const map = new naver.maps.Map('navermap', mapOptions)
    marker.setMap(map)
    infoWindow.open(map, marker)
  })
</script>

<div class="card px-4 pt-2 mb-4">
  <dl class="row">
    <!-- map start -->
    <dd class="p-0">
      <div id="navermap" class="rounded ratio ratio-16x9">
      </div>
    </dd>
    <hr class="mt-1">
    <!-- map end -->
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
    <dd class="col-sm-8">{dayjs(supplier.first_permit_datetime).format("YYYY년 MM월 DD일")}</dd>
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
</div>





