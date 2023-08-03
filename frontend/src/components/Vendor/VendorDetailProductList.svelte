<script>
  export let products;
</script>

{#each products as product}
<div class="mb-2">
  <div class="card">
    <div class="row g-0">
      <!-- <div class="col-2 h-auto">
        <div class="h-100 d-flex align-items-center">
          <img src="https://dummyimage.com/600/dee2e6/6c757d.png" class="img-fluid" alt="...">
        </div>
      </div> -->
      <div class="col-12">
        <div class="card-body h-100">
          <div class="h-100 ">
            <div class="text-truncate">
              <span class="fs-5 fw-semibold">{product.name}</span>
            </div>
            <div class="text-truncate">
              <small class="text-body-secondary">
                {#each product.suppliers as supplier}
                  {supplier.name}, 
                {/each}
              </small>
            </div>
          </div>
        </div>
      </div>
    </div>
    <a  href="/product/{product.id}" class="stretched-link"> </a>
  </div>
</div>
  
{/each}

