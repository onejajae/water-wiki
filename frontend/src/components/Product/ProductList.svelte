<script>
  import ProductListElement from "./ProductListElement.svelte";
  import productApi from "../../api/product"
	import InfiniteLoading from 'svelte-infinite-loading';


  let page = 0;
  let size = 30;
  let products = [];
  let formKeyword = ""
  let searchKeyword = ""

  async function infiniteHandler({ detail: { loaded, complete } }) {
    const res = await productApi.getList(page, size, searchKeyword)
    if (res.data.length) {
      page++;
      products = [...products, ...res.data];
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
    products = []
    page = 0
  }

</script>

<form class="input-group">
  <input type="text" class="form-control" placeholder="생수 검색" bind:value={formKeyword}>
  <button class="btn btn-outline-secondary" type="submit" on:click={search}>검색</button>
</form>
<div class="my-3">
  <div class="row row-cols-md-2 row-cols-lg-2 row-cols-xl-3">
    {#each products as product}
      <ProductListElement {product} />
    {/each}
  </div>
  {#key searchKeyword}
    <InfiniteLoading on:infinite={infiniteHandler}>
      <div class="mt-3" slot="noMore">
        총 {products.length}개의 생수를 찾았습니다.
      </div>
      <div class="mt-3" slot="noResults">
        결과가 없습니다.
      </div>
    </InfiniteLoading>
  {/key}
</div>