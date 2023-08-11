<script>
import { active } from "tinro";


const items = [
    {title: "상품", path: "/admin/product"},
    {title: "수원지", path: "/admin/supplier"},
    {title: "유통사", path: "/admin/vendor"},
  ]
</script>

<div class="container">
  <ul class="nav nav-pills nav-justified my-2">
    {#each items as item}
      <li class="nav-item">
        <a  class="nav-link" href={item.path} use:active>{item.title}</a>
      </li> 
    {/each}
  </ul>  
</div>