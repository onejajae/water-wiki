<script>
  import { onMount } from 'svelte';
  import { Datepicker } from 'vanillajs-datepicker'
  import ko from 'vanillajs-datepicker/locales/ko'
  import 'vanillajs-datepicker/css/datepicker-bs5.css'

  export let date;

  let input;
  Object.assign(Datepicker.locales, ko)

  onMount(() => {
    const datepicker = new Datepicker(input, {
			buttonClass: 'btn',
      language: 'ko'
    })
  })

  function onChangeDate() {
    date = input.value
  }
</script>


<div class="input-group">
  <input type="text" class="form-control" bind:this={input} bind:value={date} on:changeDate={onChangeDate} readonly>
</div>