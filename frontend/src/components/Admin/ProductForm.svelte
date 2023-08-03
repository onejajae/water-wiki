<script>

  
  import vendorApi from "../../api/vendor"
  import supplierApi from "../../api/supplier"

  export let product = {
    name: "",
    suppliers: [],
    vendor: {
      id: -1,
      name: "test"
    },
  }

  let vendorList = null
  let supplierList = null

  async function getVendorList() {
    if (vendorList) return
    const res = await vendorApi.getAll()
    vendorList = res.data
  }

  async function getSupplierList() {
    if (supplierList) return
    const res = await supplierApi.getAll()
    supplierList = res.data
  }

  async function setVendor(vendor) {
    product.vendor = {
      id: vendor.id,
      name: vendor.name
    }
  }

  async function deleteVendor() {
    product.vendor = {
      id: -1,
      name: "test"
    }
  }

  async function addSupplier(supplier) {
    product.suppliers = [...product.suppliers, {
      id: supplier.id,
      name: supplier.name
    }]
  }

  async function deleteSupplier(supplier) {
    const result = product.suppliers.filter(e => e.id !== supplier.id)
    product.suppliers = result
  }



</script>
  <div class="mb-3">
    <label for="product-name" class="form-label">상품명</label>
    <div class="input-group">
      <input type="text" class="form-control" id="product-name" bind:value={product.name}>
    </div>
  </div>

  <div class="mb-3">
    <label for="vendor-name" class="form-label">유통사</label>
    <div class="">
      {#if product.vendor.id === -1}
        <div></div>
      {:else}
        <button class="btn btn-secondary rounded-pill m-1" on:click={deleteVendor}>{product.vendor.name}</button>
      {/if}
    </div>
    <div class="dropdown">
      <button type="button" class="btn btn-primary dropdown-toggle" data-bs-toggle="dropdown" on:click={getVendorList}>
        유통사 선택
      </button>
      <div class="dropdown-menu">
        <form class="px-2">
          <div class="input-group">
            <input type="text" class="form-control" placeholder="검색" >
            <button type="button" class="btn btn-outline-secondary" >검색</button>
          </div>
        </form>
        <div class="dropdown-divider"></div>
        {#if vendorList}
          {#each vendorList as vendor}
            <li><button class="dropdown-item" type="button" on:click={() => setVendor(vendor)}>{vendor.name}</button></li>
          {/each}
        {/if}
      </div>
    </div>
  </div>

  <div class="mb-3">
    <label for="supplier-name" class="form-label">수원지</label>
    <div>
      {#each product.suppliers as supplier}
        <button class="btn btn-secondary rounded-pill m-1" on:click={() => deleteSupplier(supplier)}>{supplier.name}</button>
        
      {/each}
    </div>
    <div class="dropdown">
      <button type="button" class="btn btn-primary dropdown-toggle" data-bs-toggle="dropdown" on:click={getSupplierList}>수원지 선택</button>
      <div class="dropdown-menu">
        <form class="px-2">
          <div class="input-group">
            <input type="text" class="form-control" placeholder="검색">
            <button class="btn btn-outline-secondary">검색</button>
          </div>
        </form>
        <div class="dropdown-divider"></div>
        {#if supplierList}
          {#each supplierList as supplier}
            <li><button class="dropdown-item" type="button" on:click={() => addSupplier(supplier)}>{supplier.name}</button></li>
          {/each}
        {/if}
      </div>
    </div>
  </div>

