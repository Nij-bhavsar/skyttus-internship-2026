import Card from "../../components/Card";
import { useDashboard } from "../../context/DashboardContext";

const Overview = () => {
  const { data, loading, error } = useDashboard();

  if (loading) return <p className="status">Loading...</p>;
  if (error) return <p className="status error">{error}</p>;

  return (
    <div className="card-grid">
      <Card title="Total Users" value={data.length} />
      <Card title="Products" value="120" />
      <Card title="Revenue" value="₹45,000" />
    </div>
  );
};

export default Overview;