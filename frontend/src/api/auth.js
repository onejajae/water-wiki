import instance from "../api";

export default {
  login(username, password) {
    const headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
    const params = {
      username: username,
      password: password,
    }
    const res = instance.post(`/user/login`, params, { headers })
    return res
  },

}