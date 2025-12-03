import { useState } from "react";
import API from "../services/api";

function CategoryForm({ onAdd }) {
  const [name, setName] = useState("");

  const submit = async (e) => {
    e.preventDefault();
    await API.post("/categories/", { name });
    setName("");
    onAdd();
  };

  return (
    <div className="card" style={{ marginBottom: "20px" }}>
      <h3>Add Category</h3>

      <form onSubmit={submit}>
        <input
          placeholder="Category name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        /><br/>

        <button>Add</button>
      </form>
    </div>
  );
}

export default CategoryForm;
