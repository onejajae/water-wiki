<script>
  import SupplierListElement from "./SupplierListElement.svelte";
  import { onMount } from "svelte";
  import supplierApi from "../../api/supplier"

  let suppliers = [];
  let formKeyword = ""
  let searchKeyword = ""

  const accordionId = "supplierListAccordion"


  onMount(async () => {
    const res = await supplierApi.getList()
    suppliers = res.data
    console.log(suppliers)
  })
  
  async function search(event) {
    event.preventDefault()
    if (searchKeyword === formKeyword) return
    searchKeyword = formKeyword

    const res = await supplierApi.getList(searchKeyword)
    suppliers = res.data
  }

</script>

<form class="input-group">
  <input type="text" class="form-control" placeholder="수원지 검색" bind:value={formKeyword}>
  <button class="btn btn-outline-secondary" type="submit" on:click={search}>검색</button>
</form>
<div class="my-2">
  <div class="accordion accordion-flush" id="{accordionId}">
    {#each suppliers as supplier}
      <SupplierListElement supplier={supplier} {accordionId} />
    {/each}
  </div>
</div>