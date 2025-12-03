import { useEffect, useState } from "react";
import API from "../services/api";

function Dashboard() {
  const [totals, setTotals] = useState({});
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    API.get("/summary/totals").then((res) => setTotals(res.data));
    API.get("/categories").then((res) => setCategories(res.data));
  }, []);

  return (
    <div>
      <h2>Dashboard</h2>

      <div style={{ display: "flex", gap: "20px", marginBottom: "30px" }}>
        <div className="card">
          <h3>Total Income</h3>
          <p>${totals.total_income}</p>
        </div>

        <div className="card">
          <h3>Total Expense</h3>
          <p>${totals.total_expense}</p>
        </div>

        <div className="card">
          <h3>Balance</h3>
          <p>${totals.balance}</p>
        </div>
      </div>

      <h3>Your Categories</h3>
      <ul>
        {categories.map((c) => (
          <li key={c.id}>{c.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default Dashboard;
