<script>
  import SupplierListElement from "./SupplierListElement.svelte";
  import { supplierApi } from "../../api"; 
	import InfiniteLoading from 'svelte-infinite-loading';

  let page = 0;
  let size = 30;
  let suppliers = [];
  let formKeyword = ""
  let searchKeyword = ""

  const accordionId = "supplierListAccordion"

  async function infiniteHandler({ detail: { loaded, complete } }) {
    const res = await supplierApi.getList(page, size, searchKeyword)
    if (res.data.length) {
      page++;
      suppliers = [...suppliers, ...res.data];
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
    suppliers = []
    page = 0
  }

</script>

<div class="container">
  <form class="input-group">
    <input type="text" class="form-control" placeholder="수원지 검색" bind:value={formKeyword}>
    <button class="btn btn-outline-secondary" type="submit" on:click={search}>검색</button>
  </form>
  <div class="my-2">
    <div class="accordion accordion-flush" id="{accordionId}">
      {#each suppliers as supplier}
        <SupplierListElement supplier={supplier} {accordionId} />
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
            총 {suppliers.length}개의 수원지를 찾았습니다.
          </div>
          <div class="mt-3" slot="noResults">
            결과가 없습니다.
          </div>
        </InfiniteLoading>
      {/key}
    </div>
  </div>

</div>