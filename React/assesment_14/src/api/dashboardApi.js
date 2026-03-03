import axios from "axios";

export const fetchDashboardData = () => {
  return axios.get("https://jsonplaceholder.typicode.com/users");
};