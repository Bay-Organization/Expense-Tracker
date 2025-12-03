import Navbar from "../components/Navbar";

function AppLayout({ children }) {
  return (
    <div style={{ display: "flex", height: "100vh" }}>
      <Navbar />

      <div style={{ flex: 1, padding: "40px", overflowY: "auto" }}>
        {children}
      </div>
    </div>
  );
}

export default AppLayout;
