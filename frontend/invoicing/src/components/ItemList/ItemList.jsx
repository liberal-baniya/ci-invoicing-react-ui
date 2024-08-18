// export default function ItemList({ invoice, items }) {
//   return (
//     <div className="container">
//       <table className="table">
//         <thead>
//           <tr>
//             <th scope="col">Invoice No</th>
//             <th scope="col">Description</th>
//             <th scope="col">Rate</th>
//             <th scope="col">Quantity</th>
//             <th scope="col">Total</th>
//           </tr>
//         </thead>
//         <tbody>
//           {items &&
//             items.map((i) => (
//               <tr>
//                 <th>{invoice.invoice_id}</th>
//                 <td>{i.desc}</td>
//                 <th>{i.rate}</th>
//                 <td>{i.quantity}</td>
//                 <td>{i.rate * i.quantity}</td>
//               </tr>
//             ))}
//         </tbody>
//       </table>
//     </div>
//   )
// }
import React from 'react';
import { useLocation } from 'react-router-dom';

export default function ItemList() {
  const location = useLocation();
  const { i: invoice, items } = location.state || {}; // Accessing the state passed from NavLink

  if (!invoice || !items) {
    return <div>No data available</div>; // Handle cases where state is missing
  }

  return (
    <div className="container">
      <h2>Items for Invoice {invoice.id}</h2>
      <table className="table">
        <thead>
          <tr>
            <th scope="col">Invoice No</th>
            <th scope="col">Description</th>
            <th scope="col">Rate</th>
            <th scope="col">Quantity</th>
            <th scope="col">Total</th>
          </tr>
        </thead>
        <tbody>
          {items.map((item) => (
            <tr key={item.id}>
              <th>{invoice.id}</th>
              <td>{item.description}</td>
              <td>{item.rate}</td>
              <td>{item.quantity}</td>
              <td>{(item.rate * item.quantity).toFixed(2)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
