<script>
  import Router from "./router.svelte";
  import Header from "./components/Header.svelte";
  import Footer from "./components/Footer.svelte";
</script>

<header>
  <Header />
</header>
<section>
  <Router />
</section>
<footer class="mt-auto">
  <Footer />
</footer>