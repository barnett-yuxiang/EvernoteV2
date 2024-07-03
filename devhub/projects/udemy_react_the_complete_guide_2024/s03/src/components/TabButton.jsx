export default function TabButton({ label }) {
  function handeClick() {
    console.log(`You clicked on ${label}`);
  }

  return (
    <li>
      <button onClick={handeClick}>{label}</button>
    </li>
  );
}
