<script>
  export let products
  export let name=""
</script>
<!-- <div>
  {#each products as product}
  <div class="card mb-3 ">
    <div class="row g-0">
      <!-- <div class="col-2">
        <img src="https://dummyimage.com/600/dee2e6/6c757d.png" class="img-fluid rounded-start" alt="...">
      </div> 
      <div class="col-12">
        <div class="card-body h-100">
          <div class="hstack gap-1 h-100">
            <div class="text-truncate">
              <span class="fs-5 fw-semibold ">{product.name}</span>
            </div>
            <div class="text-truncate">
              <small class="text-body-secondary ">{product.vendor.name}</small>
            </div>
          </div>
        </div>
      </div>
    </div>
    <a href="/product/{product.id}" class="stretched-link"> </a>
  </div>
  {/each}

</div> -->

<div class="list-group mb-2">
  <div class="list-group-item">
    <div class="fs-5 fw-semibold text-truncate p-1">
      {name} 생산제품
    </div>
  </div>
  {#each products as product}
  <a href="/product/{product.id}" class="list-group-item list-group-item-action">
    <div class="d-flex w-100 justify-content-between">
      <div class="fw-semibold text-truncate">{ product.name }</div>
      <small>{ product.vendor.name }</small>
    </div>
  </a>
  {/each}
</div>