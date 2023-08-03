<script>
  import List from "./List.svelte";
  import VendorForm from "./VendorForm.svelte";
  import vendorApi from "../../api/vendor"

  let vendors = [];
  let selectedVendor;
  let selectedVendorDetail;
  let isLoad = false;
     
  async function getVendorList() {
    const res = await vendorApi.getList(0, 1000)
    vendors = res.data
    isLoad = true
    console.log(vendors)
  }

  async function fillForm() {
    const res = await vendorApi.get(selectedVendor.id)
    selectedVendorDetail = res.data
  }

  function confirm() {
    console.log(selectedVendorDetail);
  }

  $: {
    if (selectedVendor) {
      fillForm();
    }
  }

</script>

<div class="row my-2">
  <div class="col-sm-4">
    <div class="input-group mb-1">
      <input type="text" class="form-control" placeholder="검색">
      <button class="btn btn-outline-secondary" type="submit">검색</button>
    </div>
    <button type="button" class="btn btn-secondary w-100 my-1" on:click={getVendorList}>목록 불러오기</button>
    <button type="button" class="btn btn-secondary w-100 my-1">새 상품 추가</button>
    <List contents={vendors} isLoad={isLoad} bind:selectedItem={selectedVendor} />
  </div>
  <div class="col-sm-8">
    <VendorForm bind:vendor={selectedVendorDetail} />
    <button type="button" class="btn btn-secondary w-100 my-1" on:click={confirm}>완료</button>
  </div>
</div>