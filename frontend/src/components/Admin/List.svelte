<script>

  export let contents = [];
  export let isLoad = false;
  export let selectedItem;

  const select = (item) => () => (selectedItem = item);

</script>

{#if isLoad}
  <div>
    <div class="my-3 text-end">
      총 항목 갯수 <span class="badge bg-dark rounded-pill">{contents.length}</span>
    </div>
    <ul class="list-group">
      {#each contents as content}
        <button type="button" class="list-group-item list-group-item-action" on:click={select(content)}>{content.name}</button>
      {/each}
    </ul>
  </div>
{/if}