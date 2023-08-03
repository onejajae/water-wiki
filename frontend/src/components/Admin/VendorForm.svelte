<script>
  import DatePicker from "../common/DatePicker.svelte";

  export let vendor = {
    name: "",
    address: "",
    is_running: true,
    ceo_name: "",
    phone_number: "",
    declare_datetime: "",
  };

</script>

<div class="mb-3">
  <label for="product-name" class="form-label">유통사 업체명</label>
  <div class="input-group">
    <input type="text" class="form-control" id="product-name" bind:value={vendor.name}>
  </div>
</div>

<div class="mb-3">
  <label for="product-name" class="form-label">주소</label>
  <div class="input-group">
    <input type="text" class="form-control" id="product-name" bind:value={vendor.address}>
  </div>
</div>

<div class="mb-3">
  <label for="product-name" class="form-label">운영 현황</label>
  <div class="form-check form-switch">
    <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckChecked" bind:checked={vendor.is_running}>
    <label class="form-check-label" for="flexSwitchCheckChecked">
      {#if vendor.is_running}
        <span class="badge rounded-pill text-bg-success">영업 중</span>
      {:else}
        <span class="badge rounded-pill text-bg-secondary">휴업 중</span>
      {/if}
    </label>
  </div>
</div>

<div class="mb-3">
  <label for="product-name" class="form-label">대표자명</label>
  <div class="input-group">
    <input type="text" class="form-control" id="product-name" bind:value={vendor.ceo_name}>
  </div>
</div>

<div class="mb-3">
  <label for="product-name" class="form-label">전화번호</label>
  <div class="input-group">
    <input type="text" class="form-control" id="product-name" bind:value={vendor.phone_number}>
  </div>
</div>

<div class="mb-3">
  <label for="product-name" class="form-label">팩스번호</label>
  <div class="input-group">
    <input type="text" class="form-control" id="product-name" bind:value={vendor.phone_number}>
  </div>
</div>

<div class="mb-3">
  <p class="form-label">신고일자</p>
  <DatePicker bind:date={vendor.declare_datetime} />
</div>    

<div class="mb-3">
  <label for="product-name" class="form-label">웹 사이트 URL</label>
  <div class="input-group">
    <input type="text" class="form-control" id="product-name" bind:value={vendor.name}>
  </div>
</div>  
