<script>
  export let vendor;
</script>

<dl class="row">
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
  <dd class="col-sm-8">{vendor.declare_datetime}</dd>
  <!-- <hr>
  <dt class="col-sm-4">웹 사이트 </dt>
  <dd class="col-sm-8">바로가기</dd> -->
</dl>