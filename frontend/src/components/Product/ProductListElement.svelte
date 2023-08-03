<script>
  export let product;
</script>

<div class="mb-3">
  <div class="card">
    <div class="row">
      <!-- <div class="col-4">
        <img src="https://dummyimage.com/600/dee2e6/6c757d.png" class="img-fluid rounded-start " alt="...">
      </div> -->
      <div class="col-12">
        <div class="card-body ">
          <div class="hstack gap-1">
            <div class="text-truncate">
              <span class="fs-5 fw-semibold">{product.name}</span>
            </div>
            <div class="">
              <small class="text-body-secondary text-truncate ">{product.vendor.name}</small>
            </div>
          </div>
          <p class="card-text text-truncate">
            {#each product.suppliers as supplier}
              {supplier.name}, 
            {/each}
          </p>
        </div>
      </div>
    </div>
    <a  href="/product/{product.id}" class="stretched-link"> </a>
  </div>
</div>