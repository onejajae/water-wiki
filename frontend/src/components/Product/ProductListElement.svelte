<script>
  export let product;

</script>

<!-- <div class="mb-3">
  <div class="card">
    <div class="row">
      <div class="col-4">
        <img src="https://dummyimage.com/600/dee2e6/6c757d.png" class="img-fluid rounded-start " alt="...">
      </div>
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
            {product.suppliers.map(supplier => supplier.name).join(", ")}
          </p>
        </div>
      </div>
    </div>
    <a  href="/product/{product.id}" class="stretched-link"> </a>
  </div>
</div> -->

<div class="my-1 px-1">
  <div class="card px-1">
    <div class="card-body">
      <div class="float-end text-muted"> {product.vendor.name} </div>
      <h5 class="card-title text-truncate"> {product.name} </h5>
      <p class="card-text text-truncate">
        {product.suppliers.map(supplier => supplier.name).join(", ")}
      </p>
    </div>
    <a href="/product/{product.id}" class="stretched-link"> </a>
  </div>
</div>

<style>
  .card:hover {
    transform: scale(1.01);
    border-color: rgba(var(--bs-dark-rgb));
  }
</style>