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
    <div class="fs-5 fw-semibold text-truncate p-1">
      { name } 판매제품
    </div>
  </div>
  {#each products as product}
  <a href="/product/{product.id}" class="list-group-item list-group-item-action">
    <div class="fw-semibold text-truncate">{ product.name }</div>
    <div class="text-truncate">
      <small class="text-body-secondary">
        {product.suppliers.map(supplier => supplier.name).join(", ")}
      </small>
    </div>
  </a>
  {/each}
</div>
