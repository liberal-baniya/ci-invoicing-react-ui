// import { useEffect, useState } from 'react'
// import { NavLink } from 'react-router-dom'
// import Navbar from '../NavBar/Navbar'

// export default function InvoiceList() {
//   const [invoices, setInvoices] = useState([])
//   useEffect(() => {
//     fetch('http://127.0.0.1:8000/api/v1/invoices/')
//       .then((res) => res.json())
//       .then((results) => {
//         setInvoices(results)
//         results.forEach((element) => {
//           element.totalAmount = element.items.reduce(
//             (total, item) =>
//               Number(total) + Number(item.rate) * Number(item.quantity),
//             0,
//           )
//         })
//         console.log(invoices)
//       })
//   }, [])

//   return (
//     <div className="container">
//       <Navbar />
//       <table className="table">
//         <thead>
//           <tr>
//             <th scope="col">Invoice No</th>
//             <th scope="col">Client</th>
//             <th scope="col">Date</th>
//             <th scope="col">Total Amount</th>
//             <th scope="col"></th>
//           </tr>
//         </thead>
//         <tbody>
//           {invoices.map((i) => (
//             <tr>
//               <th>{i.invoice_id}</th>
//               <td>{i.client_name}</td>
//               <td>{new Date(i.date).toDateString()}</td>
//               <td>{i.totalAmount}</td>
//               <td>
//                 <a href={i.invoice_id} className="btn btn-warning">
//                   Items
//                 </a>
//               </td>
//             </tr>
//           ))}
//         </tbody>
//       </table>
//     </div>
//   )
// }
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import Navbar from "../NavBar/Navbar";

export default function InvoiceList() {
  const [invoices, setInvoices] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/v1/invoices/")
      .then((res) => res.json())
      .then((results) => {
        const updatedInvoices = results.map((invoice) => {
          const totalAmount = invoice.items.reduce(
            (total, item) =>
              Number(total) + Number(item.rate) * Number(item.quantity),
            0
          );
          return {
            ...invoice,
            totalAmount: totalAmount.toFixed(2), // Ensures two decimal places
          };
        });
        setInvoices(updatedInvoices);
      });
  }, []);

  return (
    <div className="container">
      <Navbar />
      <table className="table">
        <thead>
          <tr>
            <th scope="col">Invoice No</th>
            <th scope="col">Client</th>
            <th scope="col">Date</th>
            <th scope="col">Total Amount</th>
            <th scope="col"></th>
          </tr>
        </thead>
        <tbody>
          {invoices.map((i) => (
            <tr key={i.id}>
              <th>{i.id}</th>
              <td>{i.clientName}</td>
              <td>{new Date(i.createdAt).toDateString()}</td>
              <td>{i.totalAmount}</td>
              <td>
                <Link to={`/invoice/${i.id}`} className="btn btn-warning">
                  Items
                </Link>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
