<script>
  import { get } from "svelte/store"
  import { token } from "../stores";
  import { authApi } from "../api";
  import LoginModal from "./LoginModal.svelte";

  let isLogin = false
  let isAdmin = false

  token.is_login.subscribe(value => isLogin = value)
  token.is_admin.subscribe(value => isAdmin = value)

  const loginModalId = "login-modal"
  
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

<div class="bg-light mt-3">
  <nav class="nav justify-content-center py-3">
    <a href="/" class="nav-link mx-3 text-secondary">Home</a>
    <a href="https://github.com/" class="nav-link mx-3 text-secondary">GitHub</a>
    {#if !(isLogin)}
    <a href={"#"} class="nav-link mx-3 text-secondary" data-bs-toggle="modal" data-bs-target="#{loginModalId}">Login</a>
    {:else}
    <a href={"#"} class="nav-link mx-3 text-secondary" on:click={logout}>Logout</a>
    <a href={"#"} class="nav-link mx-3 text-secondary" on:click={aboutMe}>Account</a>
    {/if}
  </nav>
</div>

<LoginModal modalId={loginModalId} />