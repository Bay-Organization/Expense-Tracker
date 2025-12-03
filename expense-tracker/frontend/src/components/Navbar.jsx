import { Link } from "react-router-dom";

function Navbar() {
  return (
    <div style={{
      width: "230px",
      background: "rgba(255,255,255,0.12)",
      backdropFilter: "blur(10px)",
      height: "100vh",
      padding: "20px",
      boxSizing: "border-box"
    }}>
      <h2 style={{ marginBottom: "40px" }}>💸 Expense</h2>

      <ul style={{ listStyle: "none", padding: 0, fontSize: "18px" }}>
        <li style={{ marginBottom: "10px" }}>
          <Link to="/dashboard" style={{ color: "white", textDecoration: "none" }}>Dashboard</Link>
        </li>
        <li style={{ marginBottom: "10px" }}>
          <Link to="/transactions" style={{ color: "white", textDecoration: "none" }}>Transactions</Link>
        </li>
        <li style={{ marginBottom: "10px" }}>
          <Link to="/categories" style={{ color: "white", textDecoration: "none" }}>Categories</Link>
        </li>
      </ul>

      <button
        onClick={() => {
          localStorage.removeItem("token");
          window.location.href = "/login";
        }}
        style={{ marginTop: "40px", width: "100%" }}
      >
        Logout
      </button>
    </div>
  );
}

export default Navbar;
