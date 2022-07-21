import axios from "axios";

const axiosInstance = axios.create({
  headers: {
    "Content-Type": "application/json",
  },
});
axiosInstance.interceptors.request.use(
  (config) => {
    const token = JSON.parse(localStorage.getItem('authTokens'))?.access
    if (token) {
      config.headers["Authorization"] = 'Bearer ' + token;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

axiosInstance.interceptors.response.use(
  (response) => {
    return response;
  },
  async (error) => {
    const originalConfig = error.config;
    if (originalConfig && (originalConfig.url !== "/blog/api/login/" && error.response)) {
      // Access Token was expired
      if (error.response.status === 401 && !originalConfig._retry) {
        originalConfig._retry = true;
        try {
          const rs = await axiosInstance.post("/blog/api/login/refresh/", {
            refresh: JSON.parse(localStorage.getItem('authTokens'))?.refresh,
          });

          localStorage.setItem('authTokens', JSON.stringify(rs.data));
          return axiosInstance(originalConfig);
        } catch (_error) {
          return Promise.reject(_error);
        }
      }
    }
    return Promise.reject(error);
  }
);
export default axiosInstance;