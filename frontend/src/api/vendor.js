import instance from "../api";

export default {
  getList(keyword="") {
    let res = instance.get(`/vendor/`, {
      params: {
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