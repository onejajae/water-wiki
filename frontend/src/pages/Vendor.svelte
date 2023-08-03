<script>
  import VendorList from "../components/Vendor/VendorList.svelte";
</script>

<div class="input-group">
  <input type="text" class="form-control" placeholder="유통사 검색">
  <button class="btn btn-outline-secondary" type="submit">검색</button>
</div>

<!-- <div class="d-flex flex-row-reverse">
  <div>
    <select class="form-select" aria-label="Default select example">
      <option selected>이름</option>
      <option value="1">주소</option>
      <option value="2">개업일</option>
    </select>
  </div>
  <div>
    <div class="form-check form-check-inline">
      <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio1" value="option1" checked>
      <label class="form-check-label" for="inlineRadio1">오름차순</label>
    </div>
  </div>
  <div>
    <div class="form-check form-check-inline">
      <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio2" value="option2">
      <label class="form-check-label" for="inlineRadio2">내림차순</label>
    </div>
  </div>
</div> -->

<VendorList />