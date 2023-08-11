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
<div class="text-center v-100">
  <div class="spinner-border text-dark" role="status">
    <span class="visually-hidden">Loading...</span>
  </div>
</div>
{:else}
<div class="container">
  <div class="row">
    <div class="col-lg-7">
      <VendorDetailTable {vendor} />
    </div>
    <div class="col-lg-5">
      <VendorDetailProductList products={vendor.products} name={vendor.name}/>
    </div>
  </div>
</div>
{/if}
