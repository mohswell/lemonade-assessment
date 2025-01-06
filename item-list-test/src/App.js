import logo from './logo.svg';
import './App.css';
import React from 'react';

// Define the ItemList component
export const ItemList = ({ items }) => (
  <ul>
    {items.map((item, index) => (
      <li key={index} data-testid="list-item">
        {item}
      </li>
    ))}
  </ul>
);

function App() {
  const sampleItems = ['Item 1', 'Item 2', 'Item 3'];

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
      </header>
      {/* Use the ItemList component */}
      <ItemList items={sampleItems} />
    </div>
  );
}

export default App;