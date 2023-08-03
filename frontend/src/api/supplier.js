import instance from "../api";

export default {
  getList(page=0, size=30, keyword="") {
    const res = instance.get(`/supplier/`, {
      params: {
        page: page,
        size: size,
        keyword: keyword
      }
    })
    return res
  },

  get(supplierId) {
    const res = instance.get(`/supplier/${supplierId}`)
    return res
  },

}