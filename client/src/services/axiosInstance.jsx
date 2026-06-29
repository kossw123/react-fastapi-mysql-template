import axios from "axios";
import useAuthStore from "../zustand_store/AuthStore";

// 1. Create to Axios instance for common config, 공통 설정을 위한 Axios 인스턴스 생성
const axiosinstance = axios.create({
  baseURL: "http://localhost:8000",
  timeout: 5000,
  withCredentials: true,
});

let isRefreshing = false;
let failedQueue = [];

const processQueue = (error, token = null) => {
  failedQueue.forEach((prom) => {
    if (error) {
      prom.reject(error);
    } else {
      prom.resolve(token);
    }
  });

  failedQueue = [];
};

// 2. Configuration Request interceptor: intercept to axios instance before start to server request
// Request(요청) 인터셉터 설정: 서버로 요청이 출발하기 직전에 가로챈다.
axiosinstance.interceptors.request.use(
  (config) => {
    console.log("[클라이언트] axiosInstance.jsx, axiosInstance config 확인");
    console.log("[클라이언트] axiosInstance.jsx, baseURL", config.baseURL);
    console.log("[클라이언트] axiosInstance.jsx, timeout", config.timeout);
    console.log(
      "[클라이언트] axiosInstance.jsx, withCredentials",
      config.withCredentials,
    );

    console.log(
      "[클라이언트] axiosInstance.jsx, interceptors.request.use(stmt, ), body 요청 오류 없음 확인",
    );

    // get to zustand AuthStore state
    // AuthStore에 저장되어 있는 토큰을 즉시 가져온다.
    const { token } = useAuthStore.getState();

    const skipAuth = ["/auth/login", "/auth/logout", "/auth/refresh"];

    const shouldSkip = skipAuth.some((url) => config.url?.includes(url));

    // 토큰이 존재한다면 HTTP 헤더에 ‘Authorization'을 삽입하는데, JWT 표준 규격인 Bearer를 추가한다.
    if (!shouldSkip && token) {
      // add Bearer to JWT standard spectification
      config.headers["Authorization"] = `Bearer ${token}`;
    }

    console.log(
      "[클라이언트] axiosInstance.jsx, interceptors.request.use(stmt, ), body의 요청 서버로 전송",
    );

    return config;
  },
  (error) => {
    console.log(
      "[클라이언트] axiosInstance.jsx, interceptors.request.use( , error), body 요청 오류 확인",
    );

    return Promise.reject(error);
  },
);

// Response(응답) 인터셉터 설정: 서버에서 응답이 도착했을 때 가로챈다.
axiosinstance.interceptors.response.use(
  (res) => {
    console.log(
      "[클라이언트] axiosInstance.jsx, interceptors.response.use(response, ), 400번대 응답 확인",
    );

    // 200번대 응답 정상 통과
    return res;
  },
  async (error) => {
    console.log(
      "[클라이언트] axiosInstance.jsx, interceptors.response.use( ,error), 400번대 응답 확인 후 에러 함수 진입",
    );
    const originalRequest = error.config;

    if (
      error.response &&
      error.response.status === 401 &&
      !originalRequest._retry
    ) {
      console.log(
        "[클라이언트] axiosInstance.jsx, interceptors.request.use(, error), error 상태 확인",
      );
      if (originalRequest.url === "/auth/refresh") {
        console.log(
          "[클라이언트] axiosInstance.jsx, interceptors.request.use(, error), originalRequest의 경로가 refresh인지 확인",
        );
        useAuthStore.getState().logout();
        window.location.href = "/";

        return Promise.reject(error);
      }

      if (isRefreshing) {
        console.log(
          "[클라이언트] axiosInstance.jsx, interceptors.request.use(, error), refresh 이벤트 조건문 진입",
        );

        return new Promise((resolve, reject) => {
          failedQueue.push({ resolve, reject });
        })
          .then((token) => {
            originalRequest.headers["Authorization"] = `Bearer ${token}`;
            return axiosinstance(originalRequest);
          })
          .catch((err) => Promise.reject(err));
      }

      originalRequest._retry = true;
      isRefreshing = true;

      try {
        console.log(
          "[클라이언트] axiosInstance.jsx, interceptors.request.use(, error), refresh를 위한 /auth/refresh 주소 요청",
        );
        const response = await axios.post(
          "/auth/refresh",
          {},
          {
            withCredentials: true,
          },
        );

        const newAccessToken = response.data.token;

        useAuthStore
          .getState()
          .login(useAuthStore.getState().username, newAccessToken);

        processQueue(null, newAccessToken);

        originalRequest.headers["Authorization"] = `Bearer ${newAccessToken}`;

        console.log(
          "[클라이언트] axiosInstance.jsx, interceptors.request.use(, error), refresh의 최종 결과 반환",
        );
        return axiosinstance(originalRequest);
      } catch (refreshError) {
        console.log(
          "[클라이언트] axiosInstance.jsx, interceptors.request.use(, error), refresh 도중 error 감지",
        );
        processQueue(refreshError, null);
        alert("인증 세션이 완전히 만료되었습니다. 다시 로그인해 주세요.");
        useAuthStore.getState().logout();
        window.location.href = "/";
        return new Promise(() => {});
      } finally {
        isRefreshing = false;
      }
    }
    console.log(
      "[클라이언트] axiosInstance.jsx, interceptors.request.use(, error), 인증 기간이 만료되어 reject",
    );

    return Promise.reject(error);
  },
);

export default axiosinstance;





