<script>
  export let vendor;
  export let accordionId;

  const element_id = `supplier-item-${vendor.id}`

  // let data = false;

  // function test() {
  //   if (data) return

  //   console.log(vendor)
  //   data = true
  // }
</script>


<div class="accordion-item" >
  <h2 class="accordion-header">
    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#{element_id}">
      <div class="ms-1">
        <p class="fs-5 fw-semibold m-0">{vendor.name}</p>
        <small>{vendor.address}</small>
    </button>
  </h2>
  <div id={element_id} class="accordion-collapse collapse" data-bs-parent="#{accordionId}">
    <div class="accordion-body">
      <dl class="row">
        <!-- <dt class="col-sm-3">대표자명</dt>
        <dd class="col-sm-9">{vendor.ceo_name}</dd> -->
      
        <!-- <dt class="col-sm-3">전화번호</dt>
        <dd class="col-sm-9">{vendor.phone_number}</dd> -->


        <!-- <hr class="border bordor-color-primary"> -->
      
      
        <dt class="col-sm-3">판매제품</dt>
        <dd class="col-sm-9">
          <div>
            {#each vendor.products as product}
              <a href="/product/{product.id}" class="btn btn-light rounded-pill btn-sm" type="submit">{product.name}</a>
            {/each}
          </div>
        </dd>
        
        <dt class="col-sm-3"></dt>
        <dd class="col-sm-9">
          <a class="link-primary link-offset-2 link-offset-3-hover link-underline link-underline-opacity-0 link-underline-opacity-75-hover" href="/vendor/{vendor.id}">
          <span  class="">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-info-circle" viewBox="0 0 16 16">
              <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
              <path d="m8.93 6.588-2.29.287-.082.38.45.083c.294.07.352.176.288.469l-.738 3.468c-.194.897.105 1.319.808 1.319.545 0 1.178-.252 1.465-.598l.088-.416c-.2.176-.492.246-.686.246-.275 0-.375-.193-.304-.533L8.93 6.588zM9 4.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0z"/>
            </svg>
          </span>
          자세히 보기
          </a>
        </dd>
        
      </dl>
    </div>
    
  </div>
</div>