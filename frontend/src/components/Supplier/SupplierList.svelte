<script>
  import SupplierListElement from "./SupplierListElement.svelte";
  import { onMount } from "svelte";
  import supplierApi from "../../api/supplier"
  let suppliers = [];

  const accordionId = "supplierListAccordion"

  onMount(async () => {
    const res = await supplierApi.getAll()
    suppliers = res.data
    console.log(suppliers)
  })

</script>

<div class="my-2">
  <div class="accordion accordion-flush" id="{accordionId}">
    {#each suppliers as supplier}
      <SupplierListElement supplier={supplier} {accordionId} />
    {/each}
  </div>
</div>