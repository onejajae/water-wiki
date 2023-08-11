<script>
    import Disclaimer from "./Docs/Disclaimer.svelte";
    import PrivacyPolicy from "./Docs/PrivacyPolicy.svelte";

    export let modalId;

    const accordionId = "terms-of-service-accordion"
</script>


<div class="modal fade" id="{modalId}" tabindex="-1"  aria-hidden="true">
    <div class="modal-dialog modal-dialog-scrollable">
      <div class="modal-content">
        <div class="modal-body">
            <div class="accordion" id="accordionExample">
                <div class="accordion-item">
                    <h2 class="accordion-header">
                      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-one">
                        개인정보처리방침
                      </button>
                    </h2>
                    <div id="collapse-one" class="accordion-collapse collapse" data-bs-parent="#{accordionId}">
                      <div class="accordion-body">
                        <PrivacyPolicy />
                      </div>
                    </div>
                </div>
                <div class="accordion-item">
                    <h2 class="accordion-header">
                      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-two">
                        책임의 한계와 법적고지
                      </button>
                    </h2>
                    <div id="collapse-two" class="accordion-collapse collapse" data-bs-parent="#{accordionId}">
                      <div class="accordion-body">
                        <Disclaimer />
                      </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        </div>
      </div>
    </div>
</div>