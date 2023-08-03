<script>
    import List from "./List.svelte";
    import SupplierForm from "./SupplierForm.svelte";
    import supplierApi from "../../api/supplier"

    let suppliers;
    let selectedSupplier;
    let selectedSupplierDetail;
    let isLoad = false;
 
    async function getSupplierList() {
      const res = await supplierApi.getAll()
      suppliers = res.data
      isLoad = true
      console.log(suppliers)
    }

    async function fillForm() {
      const res = await supplierApi.get(selectedSupplier.id)
      selectedSupplierDetail = res.data
    }

    function confirm() {
      console.log(selectedSupplierDetail)
    }


    $: {
      if (selectedSupplier) {
        fillForm()
      }
    }

</script>

<div class="row my-2">
  <div class="col-sm-4">
    <div class="input-group mb-1">
      <input type="text" class="form-control" placeholder="검색">
      <button class="btn btn-outline-secondary" type="submit">검색</button>
    </div>
    <button type="button" class="btn btn-secondary w-100 my-1" on:click={getSupplierList}>목록 불러오기</button>
    <button type="button" class="btn btn-secondary w-100 my-1">새 수원지 추가</button>
    <List contents={suppliers} isLoad={isLoad} bind:selectedItem={selectedSupplier}></List>
  </div>
  <div class="col-sm-8">
    <SupplierForm bind:supplier={selectedSupplierDetail} />
    <button type="button" class="btn btn-secondary w-100 my-1" on:click={confirm}>완료</button>
  </div>
</div>