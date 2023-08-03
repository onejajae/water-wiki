<script>
  import VendorDetailProductList from "./VendorDetailProductList.svelte";
  import VendorDetailTable from "./VendorDetailTable.svelte";

  import vendorApi from "../../api/vendor";

  export let meta;

  let vendor = null;
  let isLoading = false;

  $: update()

  async function update() {
    isLoading = true
    const res = await vendorApi.get(meta.params.vendor_id)
    vendor = res.data
    console.log(vendor)
    isLoading = false
  }

</script>

{#if isLoading}
Loading....
{:else}
<div class="row m-2">
  <div class="col-lg-5">
    <div>
      <p class="text-center my-1 fs-4 fw-medium">판매 중인 제품</p>
    </div>
    <VendorDetailProductList products={vendor.products}/>
  </div>
  <div class="col-lg-7">
    <VendorDetailTable vendor={vendor}/>
  </div>
</div>
{/if}