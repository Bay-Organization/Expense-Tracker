import { useState } from "react";
import API from "../services/api";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const login = async (e) => {
    e.preventDefault();
    try {
      const res = await API.post("/auth/login", { email, password });
      localStorage.setItem("token", res.data.access_token);
      window.location.href = "/dashboard";
    } catch {
      alert("Invalid login");
    }
  };

  return (
    <div style={{ padding: "100px", textAlign: "center" }}>
      <div className="card" style={{ width: "400px", margin: "auto" }}>
        <h2>Login</h2>

        <form onSubmit={login}>
          <input placeholder="Email" onChange={(e) => setEmail(e.target.value)} required />
          <br />
          <input type="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)} required />
          <br />
          <button>Login</button>
        </form>

        <p>Don't have an account? <a href="/register">Register</a></p>
      </div>
    </div>
  );
}

export default Login;
