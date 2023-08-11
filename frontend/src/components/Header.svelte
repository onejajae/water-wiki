<script>
  import { active } from "tinro";
  import { token } from "../stores";

  let isAdmin = false
  token.is_admin.subscribe(value => isAdmin = value)

  const nav = [
    {title: "생수", path: "/product"},
    {title: "수원지", path: "/supplier"},
    {title: "유통사", path: "/vendor"},
    // {title: "지도", path: "/map"},
  ]

</script>

<div class="container">
  <div class="text-center my-2">
    <a href="/" class="link-underline link-underline-opacity-0 fs-1 fw-bold text-primary">생수위키</a>
  </div>
  <nav class="nav nav-fill nav-justified nav-underline mb-2">
    {#each nav as item}
      <a href={item.path} class="nav-link" use:active>{item.title}</a> 
    {/each}
    {#if isAdmin}
      <a href="/admin" class="nav-link" use:active>관리자</a> 
    {/if}
  </nav>
</div>
