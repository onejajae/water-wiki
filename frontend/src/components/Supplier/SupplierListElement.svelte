<script>
  export let supplier;
  export let accordionId;

  const element_id = `supplier-item-${supplier.id}`
</script>

<div class="accordion-item" >
  <h2 class="accordion-header">
    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#{element_id}">
      <div class="d-flex align-items-start">
        <div class="align-self-center">
          {#if supplier.is_running}
            <span class="badge rounded-pill text-bg-success">영업 중</span>
          {:else}
            <span class="badge rounded-pill text-bg-secondary">휴업 중</span>
          {/if}
        </div>
        <div class="ms-4">
          <p class="fs-5 fw-semibold m-0">{supplier.name}</p>
          <small>{supplier.address}</small>
        </div>
      </div>
    </button>
  </h2>
  <div id={element_id} class="accordion-collapse collapse" data-bs-parent="#{accordionId}">
    <div class="accordion-body">
      <dl class="row">
        <!-- <dt class="col-sm-3">대표자명</dt>
        <dd class="col-sm-9">{supplier.ceo_name}</dd> -->
       
        <!-- <dt class="col-sm-3">전화번호</dt>
        <dd class="col-sm-9">{supplier.phone_number}</dd> -->

        <!-- <hr class="border bordor-color-primary"> -->
      
        <dt class="col-sm-3">생산제품</dt>
        <dd class="col-sm-9">
          <div>
            {#each supplier.products as product}
              <a href="/product/{product.id}" class="btn btn-light rounded-pill btn-sm me-1 mt-1">{product.name}</a> 
            {/each}
          </div>
        </dd>
        
        <dt class="col-sm-3"></dt>
        <dd class="col-sm-9">
          <a class="icon-link" href="/supplier/{supplier.id}">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-info-circle" viewBox="0 0 16 16">
              <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
              <path d="m8.93 6.588-2.29.287-.082.38.45.083c.294.07.352.176.288.469l-.738 3.468c-.194.897.105 1.319.808 1.319.545 0 1.178-.252 1.465-.598l.088-.416c-.2.176-.492.246-.686.246-.275 0-.375-.193-.304-.533L8.93 6.588zM9 4.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0z"/>
            </svg>
            자세히 보기
          </a>
        </dd>
      </dl>
    </div>
    
  </div>
</div>