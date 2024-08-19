// import { useState } from 'react'
// import { useNavigate } from 'react-router-dom'
// import Navbar from '../NavBar/Navbar'
// import './InvoiceForm.css'

// export default function InvoiceForm() {
//   const [newInvoice, setNewInvoice] = useState({})
//   const navigate = useNavigate()

//   function handleSubmit() {
//     newInvoice.items = []
//     fetch('http://127.0.0.1:8000/api/invoices/new', {
//       method: 'POST',
//       body: JSON.stringify(newInvoice),
//       headers: {
//         'Content-Type': 'application/json',
//       },
//     }).then((res) => navigate('/'))
//   }

//   return (
//     <div className="container">
//       <Navbar />
//       <div className="mb-3">
//         <label hmlFor="name" className="form-label">
//           Client Name
//         </label>
//         <input
//           type="text"
//           className="form-control"
//           id="name"
//           value={newInvoice.client_name}
//           onInput={(e) => {
//             setNewInvoice({ ...newInvoice, client_name: e.target.value })
//           }}
//         ></input>
//       </div>
//       <div className="mb-3">
//         <label hmlFor="date" className="form-label">
//           Date
//         </label>
//         <input
//           type="date"
//           className="form-control"
//           id="date"
//           value={newInvoice.date}
//           onInput={(e) => {
//             setNewInvoice({
//               ...newInvoice,
//               date: e.target.value,
//             })
//           }}
//         ></input>
//       </div>

//       <button className="btn btn-primary" type="button" onClick={handleSubmit}>
//         Create Invoice
//       </button>
//     </div>
//   )
// }
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Navbar from '../NavBar/Navbar';
import './InvoiceForm.css';

export default function InvoiceForm() {
  const [newInvoice, setNewInvoice] = useState({
    title: '',
    status: false,
    totalAmount: 0,
    clientName: '',
  });
  const navigate = useNavigate();

  function handleSubmit() {
    fetch('http://127.0.0.1:8000/api/v1/invoices/new/', {
      method: 'POST',
      body: JSON.stringify(newInvoice),
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then((res) => res.json())
      .then((data) => {
        navigate('/invoice/' + data.id);
      });
  }

  return (
    <div className="container">
      <Navbar />
      <div className="mb-3">
        <label htmlFor="title" className="form-label">
          Invoice Title
        </label>
        <input
          type="text"
          className="form-control"
          id="title"
          value={newInvoice.title}
          onChange={(e) => setNewInvoice({ ...newInvoice, title: e.target.value })}
        />
      </div>
      <div className="mb-3">
        <label htmlFor="clientName" className="form-label">
          Client Name
        </label>
        <input
          type="text"
          className="form-control"
          id="clientName"
          value={newInvoice.clientName}
          onChange={(e) => setNewInvoice({ ...newInvoice, clientName: e.target.value })}
        />
      </div>
      <div className="mb-3">
        <label htmlFor="totalAmount" className="form-label">
          Total Amount
        </label>
        <input
          type="number"
          className="form-control"
          id="totalAmount"
          value={newInvoice.totalAmount}
          onChange={(e) => setNewInvoice({ ...newInvoice, totalAmount: parseFloat(e.target.value) })}
        />
      </div>

      <div className="mb-3">
        <label htmlFor="status" className="form-label">
          Status
        </label>
        <select
          id="status"
          className="form-control"
          value={newInvoice.status}
          onChange={(e) => setNewInvoice({ ...newInvoice, status: e.target.value === 'true' })}
        >
          <option value="false">Unpaid</option>
          <option value="true">Paid</option>
        </select>
      </div>

      <button className="btn btn-primary" type="button" onClick={handleSubmit}>
        Create Invoice
      </button>
    </div>
  );
}
