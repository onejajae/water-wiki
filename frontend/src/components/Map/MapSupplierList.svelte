<script>
    export let suppliers;
    export let selected;

    const select = (item) => () => (selected = item)

</script>

<div class="list-group list-group-flush">
    {#each suppliers as supplier}
    <button class="list-group-item list-group-item-action" on:click={select(supplier)} class:hover={selected === supplier}>
        <div class="fw-semibold text-truncate">
            {supplier.name}
        </div>
        <div class="text-truncate">
          <small class="text-body-secondary">
            {supplier.address}
          </small>
        </div>
    </button>
    {/each}
</div>