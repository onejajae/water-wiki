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
  <div class="text-center">
    <div class="spinner-border text-dark" role="status">
      <span class="visually-hidden">Loading...</span>
    </div>
  </div>
{:else}
<div class="container">
  <div class="row">
    <div class="col-lg-7">
      <SupplierDetailTable {supplier} />
      <SupplierViolantList {supplier} />
    </div>
    <div class="col-lg-5">
      <SupplierDetailProductList products={supplier.products} name={supplier.name}/>
    </div>
  </div>
</div>
{/if}
