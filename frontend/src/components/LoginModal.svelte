<script>
  export let modalId;
  import { authApi } from "../api";
  import { token } from "../stores";

  let username
  let password
  let incorrect = false

  async function login(event) {
    event.preventDefault()
    try {
      const res = await authApi.login(username, password)
      incorrect = false

      console.log(res.data)
      token.access_token.set(res.data.access_token)
      token.username.set(res.data.username)
      token.is_login.set(true)
      if (res.data.admin) token.is_admin.set(true)
      else token.is_admin.set(false)

      location.reload()
    } catch (error) {
      incorrect = true
    }
  }
</script>

<!-- Modal -->
<div class="modal fade" id="{modalId}" tabindex="-1" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-body">
        <div class="text-end">
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="form-title text-center mb-3">
          <label for="username">
            <h4>로그인</h4>
          </label>
        </div>
          
        <div class="d-flex flex-column text-center">
          <form>
            <div class="form-group mb-3">
              <input type="text" class="form-control" id="username" placeholder="아이디" bind:value={username}>
            </div>
            <div class="form-group mb-3">
              <input type="password" class="form-control" id="password" placeholder="비밀번호" bind:value={password}>
            </div>
            {#if incorrect}
              <div class="form-text text-danger mb-3">아이디 또는 비밀번호가 올바르지 않습니다.</div>
            {/if}
            <button type="submit" class="btn btn-outline-primary rounded-pill" on:click={login}>확인</button>
          </form>
        </div>

      </div>
    </div>
  </div>
</div>