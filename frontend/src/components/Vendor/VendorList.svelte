<script>
  import VendorListElement from "./VendorListElement.svelte";
  import { onMount } from "svelte";
  import vendorApi from "../../api/vendor"
  let vendors = []
  const accordionId = "vendorListAccordion"
  onMount(async () => {
    const res = await vendorApi.getAll()
    vendors = res.data
  })
</script>

<div class="my-2">
  <div class="accordion accordion-flush" id="{accordionId}">
    {#each vendors as vendor}
      <VendorListElement vendor={vendor} {accordionId}/>      
    {/each}
  </div>

</div>

