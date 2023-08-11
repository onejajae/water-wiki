<script>
  import Router from "./router.svelte";
  import Header from "./components/Header.svelte";
  import Footer from "./components/Footer.svelte";
</script>

<header class="container">
  <Header />
</header>
<section>
  <Router />
</section>
<footer>
  <Footer />
</footer>