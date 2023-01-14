<template>
  <div class="d-flex flex-column flex-shrink p-3 bg-dark" style=" width: 230px; min-height:230px ;">
    <ul class="nav nav-pills flex-column mb-auto bg-dark" style = "position: fixed;">
      <li class="nav-item">
        <nuxt-link  exact active-class = 'active' to ="/" class="nav-link text-white" aria-current="page">
          Главная
        </nuxt-link>
      </li>
      <li class="nav-item">
        <nuxt-link active-class = 'active' to="/demand" class="nav-link text-white">
          Востребованность
        </nuxt-link>
      </li>
      <li class="nav-item">
        <nuxt-link active-class = 'active' to="/geography" class="nav-link text-white">
          География
        </nuxt-link>
      </li>
      <li class="nav-item">
        <nuxt-link active-class = 'active' to="/skills" class="nav-link text-white">
          Навыки
        </nuxt-link>
      </li>
      <li class="nav-item">
        <nuxt-link active-class = 'active' to="/vacancies" class="nav-link text-white">
          Последине вакансии
        </nuxt-link>
      </li>
    </ul>
  </div>
</template>
