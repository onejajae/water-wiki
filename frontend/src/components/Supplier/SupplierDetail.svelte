<script>
  import SupplierDetailProductList from "./SupplierDetailProductList.svelte";
  import SupplierDetailTable from "./SupplierDetailTable.svelte";
  import SupplierViolantList from "./SupplierViolantList.svelte";
  import { supplierApi } from "../../api"; 

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
<div class="my-5 text-center">
  <div class="spinner-border text-dark" role="status">
    <span class="visually-hidden">Loading...</span>
  </div>
  <div class="mt-3">
    <h5>불러오는 중...</h5>
  </div>
</div>
{:else}
<div class="container">
  <div class="row">
    <div class="col-lg-7 px-1 mt-1">
      <SupplierDetailTable {supplier} />
      <SupplierViolantList {supplier} />
    </div>
    <div class="col-lg-5 px-1 mt-1">
      <SupplierDetailProductList products={supplier.products} name={supplier.name}/>
    </div>
  </div>
</div>
{/if}
