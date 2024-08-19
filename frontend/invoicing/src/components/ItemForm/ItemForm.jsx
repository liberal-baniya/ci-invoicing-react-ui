// import { useState } from 'react'
// import { useNavigate, useParams } from 'react-router-dom'
// import Navbar from '../NavBar/Navbar'
// import './ItemForm.css'

// export default function ItemForm() {
//   const [newItem, setNewItem] = useState({})
//   const navigate = useNavigate()
//   const { id } = useParams()
  
//   function handleSubmit() {
//     fetch('http://127.0.0.1:8000/api/invoices/' + id.toString() + '/items', {
//       method: 'POST',
//       body: JSON.stringify(newItem),
//       headers: {
//         'Content-Type': 'application/json',
//       },
//     }).then((res) => navigate('/' + id))
//   }

//   return (
//     <div className="container">
//       <Navbar />
//       <div className="mb-3">
//         <label hmlFor="desc" className="form-label">
//           Description
//         </label>
//         <input
//           type="text"
//           className="form-control"
//           id="desc"
//           onInput={(e) => {
//             setNewItem({ ...newItem, desc: e.target.value })
//           }}
//         ></input>
//       </div>
//       <div className="mb-3">
//         <label hmlFor="rate" className="form-label">
//           Rate
//         </label>
//         <input
//           type="number"
//           className="form-control"
//           id="rate"
//           onInput={(e) => {
//             setNewItem({ ...newItem, rate: e.target.value })
//           }}
//         ></input>
//       </div>

//       <div className="mb-3">
//         <label hmlFor="quantity" className="form-label">
//           Quantity
//         </label>
//         <input
//           type="number"
//           className="form-control"
//           id="quantity"
//           onInput={(e) => {
//             setNewItem({ ...newItem, quantity: e.target.value })
//           }}
//         ></input>
//       </div>

//       <button className="btn btn-primary" type="button" onClick={handleSubmit}>
//         Add Item
//       </button>
//     </div>
//   )
// }
import { useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import Navbar from '../NavBar/Navbar';
import './ItemForm.css';

export default function ItemForm() {
  const [newItem, setNewItem] = useState({
    description: '',
    rate: 0,
    quantity: 0,
  });
  const navigate = useNavigate();
  const { id } = useParams();

  function handleSubmit() {
    fetch('http://127.0.0.1:8000/api/v1/invoices/' + id + '/items/', {
      method: 'POST',
      body: JSON.stringify(newItem),
      headers: {
        'Content-Type': 'application/json',
      },
    }).then((res) => navigate('/invoice/' + id));
  }

  return (
    <div className="container">
      <Navbar />
      <div className="mb-3">
        <label htmlFor="desc" className="form-label">
          Description
        </label>
        <input
          type="text"
          className="form-control"
          id="desc"
          value={newItem.description}
          onChange={(e) => {
            setNewItem({ ...newItem, description: e.target.value });
          }}
        />
      </div>
      <div className="mb-3">
        <label htmlFor="rate" className="form-label">
          Rate
        </label>
        <input
          type="number"
          className="form-control"
          id="rate"
          value={newItem.rate}
          onChange={(e) => {
            setNewItem({ ...newItem, rate: parseFloat(e.target.value) });
          }}
        />
      </div>

      <div className="mb-3">
        <label htmlFor="quantity" className="form-label">
          Quantity
        </label>
        <input
          type="number"
          className="form-control"
          id="quantity"
          value={newItem.quantity}
          onChange={(e) => {
            setNewItem({ ...newItem, quantity: parseInt(e.target.value, 10) });
          }}
        />
      </div>

      <button className="btn btn-primary" type="button" onClick={handleSubmit}>
        Add Item
      </button>
    </div>
  );
}
