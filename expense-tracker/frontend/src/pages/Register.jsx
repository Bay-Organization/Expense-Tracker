import { useState } from "react";
import API from "../services/api";

function Register() {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleRegister = async (e) => {
    e.preventDefault();

    try {
      await API.post("/auth/register", {
        username: username,
        email: email,
        password: password
      });

      alert("Registered successfully!");
      window.location.href = "/login";

    } catch (err) {
      console.log(err);
      alert("Registration failed. Check your inputs.");
    }
  };

  return (
    <div style={{ padding: "100px", textAlign: "center" }}>
      <div className="card" style={{ width: "400px", margin: "auto" }}>
        <h2>Register</h2>

        <form onSubmit={handleRegister}>
          <input
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
          <br />

          <input
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
          <br />

          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          <br />

          <button type="submit">Register</button>
        </form>

        <p>Already have an account? <a href="/login">Login</a></p>
      </div>
    </div>
  );
}

export default Register;
