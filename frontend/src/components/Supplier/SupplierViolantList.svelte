<script>
    import SupplierViolant from "./SupplierViolant.svelte";
    export let supplier;
    $: console.log(supplier)
    let violaions = supplier.violations
    $: {
        if (violaions.length) {
            violaions[0].isStart = true;
            violaions[violaions.length-1].isEnd = true;
        }
    }
</script>

<div class="container">
    {#each violaions as violaion}
        <SupplierViolant {violaion}/>
    {/each}
</div>