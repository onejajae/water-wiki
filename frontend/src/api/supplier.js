import instance from "../api";

export default {
  getAll(page="") {
    let res = instance.get(`/supplier/`)
    // res.then(data => {
    //   data.data.map(e => {
    //     if (e.vendor === null) {
    //       e.vendor = {id: -1, name:"test"};
    //       return e
    //     }
    //     else return e;
    //   })
    // })
    return res
  },

  get(productId) {
    const res = instance.get(`/supplier/${productId}`)
    res.then(data => {
      data.data.products.map(e => {
        if (e.vendor === null) {
          e.vendor = {id: -1, name:"test"};
          return e
        }
        else return e;
      })
    })
    return res
  },

}