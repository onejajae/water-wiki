<script>
  export let products
</script>

{#each products as product}
<div class="card mb-2 ">
  <div class="row g-0">
    <!-- <div class="col-2">
      <img src="https://dummyimage.com/600/dee2e6/6c757d.png" class="img-fluid rounded-start" alt="...">
    </div> -->
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

