<script>
  import List from "./List.svelte";
  import productApi from "../../api/product"
  import ProductForm from "./ProductForm.svelte";

  let products = []
  let selectedProduct;
  let selectedProductDetail;
  let isLoad = false;
  let isNew = true;
 
  async function getProductList() {
    const res = await productApi.getList(0, 1000)
    products = res.data
    isLoad = true
    console.log(products)
  }

  async function fillForm() {
    const res = await productApi.get(selectedProduct.id)
    selectedProductDetail = res.data
  }

  function addProduct() {
    console.log("추가", selectedProductDetail)
  }

  function editProduct() {
    console.log(selectedProductDetail)

  }

  async function deleteProduct() {
    const isDelete = confirm(`${selectedProductDetail.name} 정말 삭제하시겠습니까?`)
    if (isDelete) {
      console.log("삭제")
      return
    }
  }

  $: {
    if (selectedProduct) {
      fillForm();
      isNew = false
      window.scrollTo({
        top:0,
      })
    }
  }


</script>

<div class="row my-2">
  <div class="col-sm-4">
    <div class="input-group mb-1">
      <input type="text" class="form-control" placeholder="검색">
      <button class="btn btn-outline-secondary" type="submit">검색</button>
    </div>
    <button type="button" class="btn btn-secondary w-100 my-1" on:click={getProductList}>목록 불러오기</button>
    <button type="button" class="btn btn-secondary w-100 my-1" on:click={() => isNew=true}>새 상품 추가</button>
    <List contents={products} isLoad={isLoad} bind:selectedItem={selectedProduct}></List>
  </div>
  <div class="col-sm-8">
    <ProductForm bind:product={selectedProductDetail} /> 
    <div class="d-flex">
      {#if isNew}
        <button type="button" class="btn btn-secondary w-100 me-1" on:click={addProduct}>완료</button>
      {:else}
        <button type="button" class="btn btn-danger w-100 me-1" on:click={deleteProduct}>삭제</button>
        <button type="button" class="btn btn-secondary w-100 me-1" on:click={editProduct}>완료</button>
      {/if}
    </div>
  </div>
</div>