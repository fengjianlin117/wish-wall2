
<template>
  <div class="wall">
    <h1>心愿墙</h1>
    <div class="form">
      <input v-model="nickname" placeholder="昵称（可匿名）" />
      <textarea v-model="content" placeholder="写下你的心愿"></textarea>
      <button @click="submit">贴上心愿</button>
    </div>
    <div class="cards">
      <div class="card" v-for="w in wishes" :key="w.id">
        <p>{{ w.content }}</p>
        <span>{{ w.nickname }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { getWishes, createWish } from "./api";

const wishes = ref([]);
const nickname = ref("");
const content = ref("");

const load = async () => wishes.value = (await getWishes()).data;
const submit = async () => {
  if (!content.value) return;
  await createWish(nickname.value || "匿名", content.value);
  content.value = "";
  load();
};

onMounted(load);
</script>

<style>
body { background:#f5f2ec; font-family: "KaiTi","STKaiti"; }
.wall { width:900px; margin:auto; }
.form { margin-bottom:20px; }
textarea { width:100%; height:80px; }
.cards { display:flex; flex-wrap:wrap; gap:16px; }
.card {
  width:260px;
  background:#fff8dc;
  padding:12px;
  box-shadow:2px 2px 6px rgba(0,0,0,.2);
  transform: rotate(-1deg);
}
</style>
