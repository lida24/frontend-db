import { authService } from '@/api'

const namespaced = true;

const state = {
  user: {},
  isLoggedIn: false
};

const getters = {
  isLoggedIn: state => state.isLoggedIn,
  user: state => state.user
};

const actions = {
  async registerUser({ dispatch }, user) {
    await authService.post("http://192.168.75.11:5000//register", user)
    await dispatch('fetchUser')
  },
  async loginUser({ dispatch }, user) {
    await authService.post("http://192.168.75.11:5000/login", user)
    await dispatch('fetchUser')
  },
  async fetchUser({ commit }) {
    await authService.get("http://192.168.75.11:5000/user")
      .then(({ data }) => commit('setUser', data))
  },
  async logoutUser({ commit }) {
    await authService.post('/logout');
    commit('logoutUserState');
  }
};

const mutations = {
  setUser(state, user) {
    state.isLoggedIn = true;
    state.user = user;
  },
  logoutUserState(state) {
    state.isLoggedIn = false;
    state.user = {};
  }
};

export default {
  namespaced,
  state,
  getters,
  actions,
  mutations
};