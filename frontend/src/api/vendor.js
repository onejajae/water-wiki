import instance from "../api";

export default {
  getAll(page="") {
    let res = instance.get(`/vendor/`)
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

  get(vendorId) {
    const res = instance.get(`/vendor/${vendorId}`)
    return res
  },

}