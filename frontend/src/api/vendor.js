import instance from "../api";

export default {
  getList(page=0, size=30, keyword="") {
    let res = instance.get(`/vendor/`, {
      params: {
        page: page,
        size: size,
        keyword: keyword
      }
    })
    return res
    return res
  },

  get(vendorId) {
    const res = instance.get(`/vendor/${vendorId}`)
    return res
  },

}