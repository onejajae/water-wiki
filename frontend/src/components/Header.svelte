<script>
  import { active } from "tinro";
  import { get } from "svelte/store"
  import { token } from "../stores";
  import LoginModal from "./LoginModal.svelte";
  import authApi from "../api/auth"

  let isLogin = false
  let isAdmin = false

  token.is_login.subscribe(value => isLogin = value)
  token.is_admin.subscribe(value => isAdmin = value)

  const loginModalId = "login-modal"

  const nav = [
    {title: "생수", path: "/product"},
    {title: "수원지", path: "/supplier"},
    {title: "유통사", path: "/vendor"},
    // {title: "지도", path: "/map"},
  ]

  function logout() {
    token.access_token.set("")
    token.username.set("")
    token.is_login.set(false)
    token.is_admin.set(false)
    location.reload()
  }

  async function aboutMe() {
    const a = await authApi.me(get(token.access_token))
    console.log(await a.data)
  }
</script>

<div>
  <div class="text-end mt-1">
    {#if !(isLogin)}
      <a href={"#"} class="link-offset-2 link-offset-3-hover link-underline link-underline-opacity-0 link-underline-opacity-75-hover link-dark" data-bs-toggle="modal" data-bs-target="#{loginModalId}">
        <span class="ms-3">
          로그인
        </span>
      </a>
    {:else}
    <a href={"#"} class="link-offset-2 link-offset-3-hover link-underline link-underline-opacity-0 link-underline-opacity-75-hover link-dark" on:click={aboutMe}>
      <span class="ms-3">
        내 정보 보기
      </span>
    </a>
      <a href={"#"} class="link-offset-2 link-offset-3-hover link-underline link-underline-opacity-0 link-underline-opacity-75-hover link-dark" on:click={logout}>
        <span class="ms-3">
          로그아웃
        </span>
      </a>
    {/if}
  </div>
  
  <div class="text-center">
    <a href="/" class="link-underline link-underline-opacity-0 fs-1 fw-bold text-primary">생수위키</a>
  </div>
  <nav class="nav nav-fill nav-justified nav-underline my-2">
    {#each nav as item}
      <a href={item.path} class="nav-link" use:active>{item.title}</a> 
    {/each}
    {#if isAdmin}
      <a href="/admin" class="nav-link" use:active>관리자</a> 
    {/if}
  </nav>
</div>

<LoginModal modalId={loginModalId} />