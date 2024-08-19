// import { useEffect, useState } from 'react'
// import { useNavigate, useParams } from 'react-router-dom'
// import Navbar from '../NavBar/Navbar'
// import './InvoiceItems.css'
// import ItemList from '../ItemList/ItemList'

// export default function InvoiceForm() {
//   const [invoice, setInvoice] = useState({})
//   const [totalAmount, setTotalAmount] = useState(0)
//   const params = useParams()

//   useEffect(() => {
//     fetch('http://127.0.0.1:8000/api/invoices/' + params.id)
//       .then((res) => res.json())
//       .then((parsedRes) => {
//         setInvoice(parsedRes)
//         if (parsedRes && parsedRes.items) {
//           const totalPrice = parsedRes.items.reduce(
//             (accumulator, currentItem) => {
//               return (
//                 accumulator +
//                 currentItem.quantity * parseFloat(currentItem.rate)
//               )
//             },
//             0,
//           )
//           console.log(totalPrice)
//           setTotalAmount(totalPrice)
//         }
//       })
//   }, [])

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
//           value={invoice.client_name}
//           disabled
//         ></input>
//       </div>
//       <div className="mb-3">
//         <label hmlFor="date" className="form-label">
//           Date
//         </label>
//         <input
//           type="text"
//           className="form-control"
//           id="date"
//           value={new Date(invoice.date).toDateString()}
//           disabled
//         ></input>
//       </div>
//       <br />
//       <label className="float-start">Total Amount: {totalAmount}</label>
//       <br />
//       <br />
//       <a
//         href={invoice.invoice_id + '/newItem'}
//         className="float-start btn btn-warning"
//       >
//         New Item
//       </a>
//       <ItemList invoice={invoice} items={invoice.items} />
//     </div>
//   )
// }
import { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import Navbar from '../NavBar/Navbar';
import './InvoiceItems.css';
import ItemList from '../ItemList/ItemList';

export default function InvoiceForm() {
  const [invoice, setInvoice] = useState({});
  const [totalAmount, setTotalAmount] = useState(0);
  const params = useParams();

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/v1/invoices/' + params.id + '/')
      .then((res) => res.json())
      .then((parsedRes) => {
        setInvoice(parsedRes);
        if (parsedRes && parsedRes.items) {
          const totalPrice = parsedRes.items.reduce(
            (accumulator, currentItem) => {
              return (
                accumulator +
                currentItem.quantity * parseFloat(currentItem.rate)
              );
            },
            0
          );
          console.log(totalPrice);
          setTotalAmount(totalPrice);
        }
      });
  }, [params.id]);

  return (
    <div className="container">
      <Navbar />
      <div className="mb-3">
        <label htmlFor="name" className="form-label">
          Client Name
        </label>
        <input
          type="text"
          className="form-control"
          id="name"
          value={invoice.clientName || ''}
          disabled
        />
      </div>
      <div className="mb-3">
        <label htmlFor="date" className="form-label">
          Date
        </label>
        <input
          type="text"
          className="form-control"
          id="date"
          value={invoice.createdAt ? new Date(invoice.createdAt).toDateString() : ''}
          disabled
        />
      </div>
      <br />
      <label className="float-start">Total Amount: {totalAmount}</label>
      <br />
      <br />
      <Link
        to={'/invoices/' + params.id + '/newItem'}
        className="float-start btn btn-warning"
      >
        New Item
      </Link>
      <ItemList invoice={invoice} items={invoice.items || []} />
    </div>
  );
}
