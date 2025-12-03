import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";
import Transactions from "./pages/Transactions";
import Categories from "./pages/Categories";
import AppLayout from "./layout/AppLayout";

function App() {
  return (
    <BrowserRouter>
      <Routes>

        <Route path="/" element={<Login />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />

        <Route path="/dashboard" element={<AppLayout><Dashboard /></AppLayout>} />
        <Route path="/transactions" element={<AppLayout><Transactions /></AppLayout>} />
        <Route path="/categories" element={<AppLayout><Categories /></AppLayout>} />

      </Routes>
    </BrowserRouter>
  );
}

export default App;
