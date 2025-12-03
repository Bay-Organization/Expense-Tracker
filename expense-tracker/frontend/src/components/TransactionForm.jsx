import { useState, useEffect } from "react";
import API from "../services/api";

function TransactionForm({ onAdd }) {
  const [amount, setAmount] = useState("");
  const [type, setType] = useState("expense");
  const [description, setDescription] = useState("");
  const [date, setDate] = useState("");
  const [categoryId, setCategoryId] = useState("");
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    API.get("/categories").then((res) => setCategories(res.data));
  }, []);

  const submit = async (e) => {
    e.preventDefault();
    await API.post("/transactions/", {
      amount,
      type,
      description,
      date,
      category_id: Number(categoryId),
    });
    onAdd();
  };

  return (
    <div className="card" style={{ marginBottom: "20px" }}>
      <h3>Add Transaction</h3>

      <form onSubmit={submit}>
        <input placeholder="Amount" onChange={(e) => setAmount(e.target.value)} required /><br/>
        <select onChange={(e) => setType(e.target.value)}>
          <option value="expense">Expense</option>
          <option value="income">Income</option>
        </select><br/>
        <input placeholder="Description" onChange={(e) => setDescription(e.target.value)} /><br/>
        <input type="date" onChange={(e) => setDate(e.target.value)} required /><br/>

        <select onChange={(e) => setCategoryId(e.target.value)} required>
          <option>Select category</option>
          {categories.map((c) => (
            <option key={c.id} value={c.id}>{c.name}</option>
          ))}
        </select><br/>

        <button>Add Transaction</button>
      </form>
    </div>
  );
}

export default TransactionForm;
