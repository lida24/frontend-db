import axios from "axios";

const state = {
  user: null,
};

const getters = {
  isAuthenticated: (state) => !!state.user,
  StateUser: (state) => state.user,
};

const actions = {
  async Register({dispatch}, form) {
    await axios.post('http://192.168.75.11:5000/register', form)
    let UserForm = new FormData()
    UserForm.append('username', form.username)
    UserForm.append('password', form.password)
    /* await dispatch('LogIn', UserForm) */
  },

  async LogIn({commit}, form) {
    await axios.post("http://192.168.75.11:5000/login",
      {
        "username": form.username,
        "password": form.password
      }
    )
    .then((res) => {
      console.log(res);
      console.log("u", form.username);
      console.log("p", form.password);
      this.msg = res.data;
      commit("setUser", form.username);
    })
    .catch((error) => {
      console.log("ERROR: ", error);
      console.error(error);
    });
  },


  async LogOut({ commit }) {
    await axios.get('http://192.168.75.11:5000/logout')
    let user = null;
    commit("logout", user);
  },
};

const mutations = {
  setUser(state, username) {
    state.user = username;
  },

  logout(state, user) {
    state.user = user;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
