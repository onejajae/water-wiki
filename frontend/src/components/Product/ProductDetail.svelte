<script>
  import productApi from "../../api/product"
  
  export let meta;

  let product_id;
  let product = null;
  let isLoading = false;
  
  $: {
    update()
    product_id = $meta.params.product_id
  }


  async function update() {
    isLoading = true
    const res = await productApi.get(meta.params.product_id)
    product = res.data
    console.log(product)
    isLoading = false
  }
</script>



{#if isLoading}
Loading....
{:else}
<div class="row m-2">
  <div class="col-md-12">
    <dl class="row">
      <dt class="col-sm-3">제품명</dt>
      <dd class="col-sm-9">{product.name}</dd>
      <hr>
      <dt class="col-sm-3">유통사</dt>
      <dd class="col-sm-9">
        <a href="/vendor/{product.vendor.id}" class="link-offset-2-hover link-underline link-underline-opacity-0 link-dark link-underline-opacity-75-hover">
          {product.vendor.name} 
        </a>
      </dd>
      <hr>
      <dt class="col-sm-3">제조사</dt>
      <dd class="col-sm-9">
        <dl class="col">
          {#each product.suppliers as supplier}
            <dl class="col">
              <a href="/supplier/{supplier.id}" class="link-offset-2-hover link-underline link-underline-opacity-0 link-dark link-underline-opacity-75-hover">
                <div>
                  <p class="m-0">{supplier.name}</p>
                </div>
                <div>
                  <small>{supplier.address}</small>
                </div>
              </a>
              <div>
                {#each supplier.products as product}
                  <a class="btn btn-light rounded-pill btn-sm"  href="/product/{product.id}">{product.name}</a>
                {/each}
              </div>
            </dl>
          {/each}
          </dl>
      </dd>
    </dl>
  </div>
  <!-- <div class="col-md-5">  
    <img src="https://dummyimage.com/600/dee2e6/6c757d.png" class="img-fluid" alt="...">
  </div> -->
</div>
{/if}