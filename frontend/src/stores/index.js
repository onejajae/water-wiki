import { writable } from "svelte/store";

const persist_storage = (key, initValue) => {
  const storedValueStr = localStorage.getItem(key)
  const store = writable(storedValueStr != null ? JSON.parse(storedValueStr) : initValue)
  store.subscribe((val) => {
      localStorage.setItem(key, JSON.stringify(val))
  })
  return store
}

const token = {
  access_token: persist_storage("access_token", ""),
  username: persist_storage("username", ""),
  is_admin: persist_storage("is_admin", false),
  is_login: persist_storage("is_login", false),
}


export {
  token
}