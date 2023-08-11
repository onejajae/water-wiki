import instance from "./axiosInstance";

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
  
  me(token) {
    const headers = {
      'Authorization': `Bearer ${token}`
    }
    const res = instance.get(`/user/me`, { headers })
    return res
  }

}