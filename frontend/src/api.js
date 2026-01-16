
import axios from "axios";
export const api = axios.create({
  baseURL: "http://127.0.0.1:8000"
});
export const getWishes = () => api.get("/wishes");
export const createWish = (nickname, content) =>
  api.post("/wishes", null, { params: { nickname, content } });
