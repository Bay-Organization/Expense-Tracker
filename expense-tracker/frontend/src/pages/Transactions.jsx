import { useState, useEffect } from "react";
import API from "../services/api";
import TransactionForm from "../components/TransactionForm";

function Transactions() {
  const [transactions, setTransactions] = useState([]);

  const load = () => {
    API.get("/transactions").then((res) => setTransactions(res.data));
  };

  useEffect(() => {
    load();
  }, []);

  const remove = async (id) => {
    await API.delete(`/transactions/${id}`);
    load();
  };

  return (
    <div>
      <h2>Transactions</h2>

      <TransactionForm onAdd={load} />

      <div className="card">
        <ul>
          {transactions.map((tx) => (
            <li key={tx.id} style={{ marginBottom: "10px" }}>
              {tx.date} — {tx.type} — ${tx.amount} — {tx.description}
              <button onClick={() => remove(tx.id)} style={{ marginLeft: "10px" }}>Delete</button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default Transactions;
