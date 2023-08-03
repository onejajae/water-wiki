<script>
    import DatePicker from "../common/DatePicker.svelte";

  export let supplier = {
    name: "",
    address: "",
    is_running: true,
    ceo_name: "",
    phone_number: "",
    first_permit_datetime: "",
    intakes: "",
    pipes: ""
  };


</script>

<div>
  <div class="mb-3">
    <label for="product-name" class="form-label">수원지 업체명</label>
    <div class="input-group">
      <input type="text" class="form-control" id="product-name" bind:value="{supplier.name}">
    </div>
  </div>
  
  <div class="mb-3">
    <label for="product-name" class="form-label">주소</label>
    <div class="input-group">
      <input type="text" class="form-control" id="product-name" bind:value="{supplier.address}">
    </div>
  </div>
  
  <div class="mb-3">
    <label for="product-name" class="form-label">운영 현황</label>
    <div class="form-check form-switch">
      <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckChecked" bind:checked={supplier.is_running}>
      <label class="form-check-label" for="flexSwitchCheckChecked">
        {#if supplier.is_running}
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
      <input type="text" class="form-control" id="product-name" bind:value="{supplier.ceo_name}">
    </div>
  </div>
  
  <div class="mb-3">
    <label for="product-name" class="form-label">전화번호</label>
    <div class="input-group">
      <input type="text" class="form-control" id="product-name" bind:value="{supplier.phone_number}">
    </div>
  </div>
  
  <div class="mb-3">
    <label for="product-name" class="form-label">팩스번호</label>
    <div class="input-group">
      <input type="text" class="form-control" id="product-name" bind:value="{supplier.phone_number}">
    </div>
  </div>
  
  <div class="mb-3">
    <p class="form-label">허가일자</p>
    <DatePicker bind:date={supplier.first_permit_datetime} />
  </div>    
  
  <div class="mb-3">
    <label for="product-name" class="form-label">일일 취수 허용량</label>
    <div class="input-group">
      <input type="text" class="form-control" id="product-name" bind:value="{supplier.intakes}">
    </div>
  </div>   
  
  <div class="mb-3">
    <label for="product-name" class="form-label">취수공 수</label>
    <div class="input-group">
      <input type="text" class="form-control" id="product-name" bind:value="{supplier.pipes}">
    </div>
  </div>   
  
  <div class="mb-3">
    <label for="product-name" class="form-label">웹 사이트 URL</label>
    <div class="input-group">
      <input type="text" class="form-control" id="product-name" bind:value="{supplier.name}">
    </div>
  </div>  
  

</div>