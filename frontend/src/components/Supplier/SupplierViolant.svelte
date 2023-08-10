<script>
    import dayjs from 'dayjs'
    export let violaion;

    
</script>

<div class="row">
    <div class="col-auto text-center flex-column d-none d-sm-flex">
        <div class="row h-50">
            {#if violaion.isStart}
            <div class="col">&nbsp;</div>
            <div class="col">&nbsp;</div>
            {:else}
            <div class="col border-end">&nbsp;</div>    
            <div class="col">&nbsp;</div> 
            {/if}
        </div>
        <h5 class="m-1">
            <span class="badge bg-{violaion.level} rounded-circle p-2 ">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-exclamation-triangle-fill" viewBox="0 0 16 16">
                    <path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/>
                  </svg>
            </span>
        </h5>
        <div class="row h-50">
            {#if violaion.isEnd}
            <div class="col">&nbsp;</div>
            <div class="col">&nbsp;</div>
            {:else}
            <div class="col border-end">&nbsp;</div>
            <div class="col">&nbsp;</div>
            {/if}
        </div>
    </div>
    <div class="col py-2">   
        <div class="card border-{violaion.level} shadow mt-2">
            <div class="card-body pb-2">
                <div class="float-end text-muted">{dayjs(violaion.issued_datetime).format("YYYY년 MM월 DD일")}</div>
                <h4 class="card-title text-{violaion.level}">{violaion.title}</h4>
                <p class="card-text">
                    {#each violaion.detail.split("\\n") as sentence}
                    <div class="">{sentence}</div>
                    {/each}
                </p>
                {#if violaion.start_datetime && violaion.end_datetime}
                <dl class="row mb-0">
                    <dt class="col-sm-3">
                        처분기간
                    </dt>
                    <dd class="col-sm-9">
                        {dayjs(violaion.start_datetime).format("YYYY년 MM월 DD일")} ~ {dayjs(violaion.end_datetime).format("YYYY년 MM월 DD일")}
                    </dd>
                </dl>
                {/if}
            </div>
        </div>
    </div>
</div>
