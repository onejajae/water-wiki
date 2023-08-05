<script>
// @ts-nocheck

  import { Route } from 'tinro'

  import Main from './pages/Main.svelte'
  import Product from './pages/Product.svelte'
  import Supplier from './pages/Supplier.svelte'
  import Vendor from './pages/Vendor.svelte'
  import Map from './pages/Map.svelte'

  import ProductDetail from './components/Product/ProductDetail.svelte';
  import SupplierDetail from './components/Supplier/SupplierDetail.svelte';
  import VendorDetail from './components/Vendor/VendorDetail.svelte';

  
  import NotFound from './pages/NotFound.svelte'
  import Admin from './pages/Admin.svelte';
  import ManageProduct from './components/Admin/ManageProduct.svelte';
  import ManageSupplier from './components/Admin/ManageSupplier.svelte';
  import ManageVendor from './components/Admin/ManageVendor.svelte';
</script>

<Route>
  <Route path="/" redirect="/product"><Main/></Route>
  <Route path="/product/*">
    <Route path="/"><Product/></Route>
    <Route path="/:product_id" let:meta><ProductDetail meta={meta} /></Route>
  </Route>
  <Route path="/supplier/*">
    <Route path="/"><Supplier/></Route>
    <Route path="/:supplier_id" let:meta><SupplierDetail meta={meta} /></Route>
  </Route>
  <Route path="/vendor/*">
    <Route path="/"><Vendor/></Route>
    <Route path="/:vendor_id" let:meta><VendorDetail meta={meta} /></Route>
  </Route>
  <Route path="/map"><Map/></Route>
  <Route path="/admin/*">
    <Route path="/*">
      <Admin/>
    </Route>
    <Route path="/product"><ManageProduct /></Route>
    <Route path="/supplier"><ManageSupplier /></Route>
    <Route path="/vendor"><ManageVendor /></Route>

  </Route>

  <Route fallback><NotFound/></Route>
</Route>
