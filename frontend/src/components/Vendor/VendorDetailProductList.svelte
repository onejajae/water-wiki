<script>
  export let products;
  export let name = ""
</script>

<!-- {#each products as product}
<div class="mb-2">
  <div class="card">
    <div class="row g-0">
      <div class="col-2 h-auto">
        <div class="h-100 d-flex align-items-center">
          <img src="https://dummyimage.com/600/dee2e6/6c757d.png" class="img-fluid" alt="...">
        </div>
      </div> 
      <div class="col-12">
        <div class="card-body h-100">
          <div class="h-100 ">
            <div class="text-truncate">
              <span class="fs-5 fw-semibold">{product.name}</span>
            </div>
            <div class="text-truncate">
              <small class="text-body-secondary">
                {product.suppliers.map(supplier => supplier.name).join(", ")}
              </small>
            </div>
          </div>
        </div>
      </div>
    </div>
    <a  href="/product/{product.id}" class="stretched-link"> </a>
  </div>
</div>
  
{/each} -->

<div class="list-group mb-2">
  <div class="list-group-item">
    <div class="fs-4 fw-bold text-truncate p-2">
      { name } 판매 제품
    </div>
  </div>
  {#each products as product}
  <a href="/product/{product.id}" class="list-group-item list-group-item-action">
    <div class="d-flex w-100 justify-content-between p-1">
      <div class="fw-semibold text-truncate">{ product.name }</div>
    </div>
    
    <div class="text-truncate mx-1">
      <small class="text-body-secondary">
        {product.suppliers.map(supplier => supplier.name).join(", ")}
      </small>
    </div>
  </a>
  {/each}
</div>
