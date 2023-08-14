<script>
  import { productApi } from "../../api";
  
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
    isLoading = false
  }
</script>



{#if isLoading}
<div class="my-5 text-center">
  <div class="spinner-border text-dark" role="status">
    <span class="visually-hidden">Loading...</span>
  </div>
  <div class="mt-3">
    <h5>불러오는 중...</h5>
  </div>
</div>
{:else}
<div class="container">
  <div class="card p-2">
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
                      <p class="m-0">
                        <span class="me-1">{supplier.name}</span>
                        {#if supplier.violations.reduce((acc, cur) => { if (cur.level === "danger") { return acc + 1 } else { return acc } }, 0)}
                          <span class="badge text-bg-danger">
                            { supplier.violations.reduce((acc, cur) => { if (cur.level === "danger") { return acc + 1 } else { return acc } }, 0) }
                          </span>
                        {/if}
                        {#if supplier.violations.reduce((acc, cur) => { if (cur.level === "warning") { return acc + 1 } else { return acc } }, 0)}
                          <span class="badge text-bg-warning">
                            { supplier.violations.reduce((acc, cur) => { if (cur.level === "warning") { return acc + 1 } else { return acc } }, 0) }
                          </span>
                        {/if}
                      </p>
                    </div>
                    <div>
                      <small>{supplier.address}</small>
                    </div>
                  </a>
                  <div>
                    {#each supplier.products as product}
                      <a class="btn btn-light rounded-pill btn-sm me-1 mt-1"  href="/product/{product.id}">{product.name}</a>
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
  </div>
</div>
{/if}