<script>
  import VendorDetailProductList from "./VendorDetailProductList.svelte";
  import VendorDetailTable from "./VendorDetailTable.svelte";

  import { vendorApi } from "../../api";

  export let meta;

  let vendor = null;
  let isLoading = false;

  $: update()

  async function update() {
    isLoading = true
    const res = await vendorApi.get(meta.params.vendor_id)
    vendor = res.data
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
      <VendorDetailTable {vendor} />
    </div>
    <div class="col-lg-5 px-1 mt-1">
      <VendorDetailProductList products={vendor.products} name={vendor.name}/>
    </div>
  </div>
</div>
{/if}
