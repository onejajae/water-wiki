<script>
  import SupplierDetailProductList from "./SupplierDetailProductList.svelte";
  import SupplierDetailTable from "./SupplierDetailTable.svelte";
  import supplierApi from "../../api/supplier"

  export let meta;

  let supplier = null;
  let isLoading = false;

  $: update()

  async function update() {
    isLoading = true
    const res = await supplierApi.get(meta.params.supplier_id)
    supplier = res.data
    isLoading = false
  }

</script>

{#if isLoading}
  <div class="text-center">
    <div class="spinner-border text-dark" role="status">
      <span class="visually-hidden">Loading...</span>
    </div>
  </div>
{:else}
  <div class="row m-2">
    <div class="col-lg-5">
      <div>
        <p class="text-center my-1 fs-4 fw-medium">{supplier.name} 생산제품</p>
      </div>
      <SupplierDetailProductList products={supplier.products}/>
    </div>
    <div class="col-lg-7">
      <SupplierDetailTable supplier={supplier}/>
    </div>
  </div>
{/if}
