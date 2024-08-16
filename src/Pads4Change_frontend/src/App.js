import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [inventory, setInventory] = useState(null);
  const [schoolId, setSchoolId] = useState('');
  const [quantity, setQuantity] = useState(0);

  const checkInventory = async () => {
    try {
      const response = await axios.get('/api/inventory');
      setInventory(response.data);
    } catch (error) {
      console.error('Error checking inventory:', error);
    }
  };

  const allocatePads = async () => {
    try {
      const response = await axios.post('/api/allocate', {
        school_id: schoolId,
        quantity: parseInt(quantity, 10),
      });
      alert(`Allocation Success: ${response.data.success}`);
    } catch (error) {
      console.error('Error allocating pads:', error);
    }
  };

  return (
    <div className="App">
      <h1>Pads4Change Distribution System</h1>
      <button onClick={checkInventory}>Check Inventory</button>
      {inventory && (
        <div>
          <h2>Inventory:</h2>
          <pre>{JSON.stringify(inventory, null, 2)}</pre>
        </div>
      )}

      <div>
        <h2>Allocate Pads to School</h2>
        <input
          type="text"
          placeholder="Enter School ID"
          value={schoolId}
          onChange={(e) => setSchoolId(e.target.value)}
        />
        <input
          type="number"
          placeholder="Enter Quantity"
          value={quantity}
          onChange={(e) => setQuantity(e.target.value)}
        />
        <button onClick={allocatePads}>Allocate</button>
      </div>
    </div>
  );
}

export default App;

