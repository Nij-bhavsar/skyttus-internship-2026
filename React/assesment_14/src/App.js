import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import DashboardLayout from "./pages/dashboard/DashboardLayout";
import Overview from "./pages/dashboard/Overview";
import Products from "./pages/dashboard/Products";
import Users from "./pages/dashboard/Users";
import { DashboardProvider } from "./context/DashboardContext";

function App() {
  return (
    <DashboardProvider>
      <BrowserRouter>
        <Routes>

          {/* Redirect root to dashboard */}
          <Route path="/" element={<Navigate to="/dashboard/overview" />} />

          <Route path="/dashboard" element={<DashboardLayout />}>
            <Route index element={<Navigate to="overview" />} />
            <Route path="overview" element={<Overview />} />
            <Route path="products" element={<Products />} />
            <Route path="users" element={<Users />} />
          </Route>

        </Routes>
      </BrowserRouter>
    </DashboardProvider>
  );
}

export default App;