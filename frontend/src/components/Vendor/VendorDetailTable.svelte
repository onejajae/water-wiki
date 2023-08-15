<script>
  import { onMount } from "svelte";
  import dayjs from "dayjs";
  export let vendor;

  const vendorPosition = new naver.maps.LatLng(vendor.loc_y, vendor.loc_x)
  const vendorPositionEPSG3857 = naver.maps.TransCoord.fromLatLngToEPSG3857(vendorPosition)

  const infoWindowContent = [
    `<div class="m-3">`,
    `<a href="https://map.naver.com/v5/search?c=${vendorPositionEPSG3857.x},${vendorPositionEPSG3857.y},18,0,0,2,dh" class="link-offset-2 link-underline link-underline-opacity-0" target="_blank" rel="noopener noreferrer">`,
    `<h5 class="mb-0">${vendor.name}</h5>`,
    `<p class="link-dark">${vendor.address}</p>`,
    `</a></div>`,
  ].join('')

  const mapOptions = {
    center: vendorPosition,
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
    position: vendorPosition,
  })
  
  onMount(() => {
    const map = new naver.maps.Map('navermap', mapOptions)
    marker.setMap(map)
    infoWindow.open(map, marker)
  })
</script>

<div class="card px-4 py-2 mb-2">
  <dl class="row">
    <!-- map start -->
    <dd class="px-0">
      <div id="navermap" class="rounded ratio ratio-16x9">
      </div>
    </dd>
    <hr class="mt-1">
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