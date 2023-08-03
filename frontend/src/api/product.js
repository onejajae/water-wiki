import instance from "../api";

export default {
  getList(page=0, size=30, keyword="") {
    const res = instance.get(`/product/`, {
      params: {
        page: page,
        size: size,
        keyword: keyword
      }
    })
    return res
  },

  get(productId) {
    const res = instance.get(`/product/${productId}`)
    return res
  },

}