<template>
  <div>
    <nav>
      <div class="nav-content">
        <h1>Cookio</h1>
      </div>
    </nav>
    <div class="content-container">
      <router-view/>
    </div>
  </div>
</template>

<style>
body {
  background-color: var(--bg-color);
}

.content-container{
  max-width: var(--size-md);
  margin: 20px auto;
  background-color: white;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  padding: 20px;
  border-radius: 15px;
  height: 100vh;
}

nav {
  max-width: var(--size-xl);
  margin: auto;
  background-color: white;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  padding: 3px;
  height: 50px;
  border-bottom: 1px solid var(--primary-color);
}

.nav-content{
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 20px;
}

</style>
