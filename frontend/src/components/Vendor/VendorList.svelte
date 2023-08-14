<script>
  import VendorListElement from "./VendorListElement.svelte";
  import { vendorApi } from "../../api";
	import InfiniteLoading from 'svelte-infinite-loading';

  let page = 0;
  let size = 30;
  let vendors = []
  let formKeyword = ""
  let searchKeyword = ""

  const accordionId = "vendorListAccordion"

  async function infiniteHandler({ detail: { loaded, complete } }) {
    const res = await vendorApi.getList(page, size, searchKeyword)
    if (res.data.length) {
      page++;
      vendors = [...vendors, ...res.data];
      loaded();
    }
    else {
      complete()
    }
	}

  async function search(event) {
    event.preventDefault()
    if (searchKeyword === formKeyword) return
    searchKeyword = formKeyword
    vendors = []
    page = 0
  }

</script>


<div class="container">
  <form class="input-group">
    <input type="text" class="form-control" placeholder="유통사 검색" bind:value={formKeyword}>
    <button class="btn btn-outline-secondary" type="submit" on:click={search}>검색</button>
  </form>
  <div class="my-2">
    <div class="accordion accordion-flush" id="{accordionId}">
      {#each vendors as vendor}
        <VendorListElement vendor={vendor} {accordionId}/>      
      {/each}
      {#key searchKeyword}
        <InfiniteLoading on:infinite={infiniteHandler}>
          <div class="my-5" slot="spinner">
            <div class="text-center">
              <div class="spinner-border text-dark" role="status">
                <span class="visually-hidden">Loading...</span>
              </div>
              <div class="mt-3">
                <h5>불러오는 중...</h5>
              </div>
            </div>
          </div>
          <div class="mt-3" slot="noMore">
            총 {vendors.length}개의 유통사를 찾았습니다.
          </div>
          <div class="mt-3" slot="noResults">
            결과가 없습니다.
          </div>
        </InfiniteLoading>
      {/key}
    </div>
  </div>

</div>

