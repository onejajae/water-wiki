<script>
  import Router from "./router.svelte";
  import Header from "./components/Header.svelte";
  import DarkModeToggle from "./components/DarkModeToggle.svelte";
  import Footer from "./components/Footer.svelte";
</script>

<header class="container">
  <Header />
</header>
<section class="container">
  <Router />
</section>
<footer>
  <Footer />
</footer>