<script>
    import SupplierViolant from "./SupplierViolant.svelte";
    export let supplier;
    let violaions = supplier.violations
    $: {
        if (violaions.length) {
            violaions[0].isStart = true;
            violaions[violaions.length-1].isEnd = true;
        }
    }
</script>

<div class="card container p-4 mb-1">
    <h4 class="card-title">위반 및 처분 결과</h4>
    {#each violaions as violaion}
        <SupplierViolant {violaion}/>
    {/each}
</div>