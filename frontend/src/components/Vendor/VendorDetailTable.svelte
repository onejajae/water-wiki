<script>
  import { onMount } from "svelte";
  import dayjs from "dayjs";
  export let vendor;
  
  onMount(() => {
    const center = new naver.maps.LatLng(vendor.loc_y, vendor.loc_x)
    const mapOptions = {
      center: center,
      zoom: 14,
      draggable: false,
      pinchZoom: false,
      scrollWheel: false,
    }
    const map = new naver.maps.Map('navermap', mapOptions)
    const marker = new naver.maps.Marker({
      position: center,
      map: map,
    })
  })
</script>

<div class="card px-4 py-2 mb-4">
  <dl class="row">
    <!-- map start -->
    <dd class="px-0">
      <div id="navermap" class="rounded" style="height: 250px;">

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