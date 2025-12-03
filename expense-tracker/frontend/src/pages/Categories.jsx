import { useEffect, useState } from "react";
import API from "../services/api";
import CategoryForm from "../components/CategoryForm";

function Categories() {
  const [categories, setCategories] = useState([]);

  const load = () => {
    API.get("/categories").then((res) => setCategories(res.data));
  };

  useEffect(() => {
    load();
  }, []);

  const remove = async (id) => {
    await API.delete(`/categories/${id}`);
    load();
  };

  return (
    <div>
      <h2>Categories</h2>

      <CategoryForm onAdd={load} />

      <div className="card">
        <ul>
          {categories.map((c) => (
            <li key={c.id} style={{ marginBottom: "10px" }}>
              {c.name}
              <button onClick={() => remove(c.id)} style={{ marginLeft: "10px" }}>Delete</button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default Categories;
