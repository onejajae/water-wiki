import instance from "./axiosInstance";

export default {
  getList(page=0, size=30, keyword="") {
    const res = instance.get(`/vendor/`, {
      params: {
        page: page,
        size: size,
        keyword: keyword
      }
    })
    return res
  },

  get(vendorId) {
    const res = instance.get(`/vendor/${vendorId}`)
    return res
  },

}