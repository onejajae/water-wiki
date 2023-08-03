<script>
  import VendorListElement from "./VendorListElement.svelte";
  import { onMount } from "svelte";
  import vendorApi from "../../api/vendor"

  let vendors = []
  let formKeyword = ""
  let searchKeyword = ""

  const accordionId = "vendorListAccordion"

  onMount(async () => {
    const res = await vendorApi.getList()
    vendors = res.data
  })

  async function search(event) {
    event.preventDefault()
    if (searchKeyword === formKeyword) return
    searchKeyword = formKeyword

    const res = await vendorApi.getList(searchKeyword)
    vendors = res.data
  }

</script>

<form class="input-group">
  <input type="text" class="form-control" placeholder="수원지 검색" bind:value={formKeyword}>
  <button class="btn btn-outline-secondary" type="submit" on:click={search}>검색</button>
</form>
<div class="my-2">
  <div class="accordion accordion-flush" id="{accordionId}">
    {#each vendors as vendor}
      <VendorListElement vendor={vendor} {accordionId}/>      
    {/each}
  </div>

</div>

