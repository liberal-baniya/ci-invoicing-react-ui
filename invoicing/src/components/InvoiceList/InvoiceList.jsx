import { useEffect, useState } from 'react'
import { NavLink } from 'react-router-dom'
import Navbar from '../NavBar/Navbar'

export default function InvoiceList() {
  const [invoices, setInvoices] = useState([])
  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/invoices/')
      .then((res) => res.json())
      .then((items) => {
        setInvoices(items)
        console.log(invoices)
      })
  }, [])

  return (
    <div className="container">
      <Navbar />
      <table class="table">
        <thead>
          <tr>
            <th scope="col">Invoice No</th>
            <th scope="col">Client</th>
            <th scope="col">Date</th>
          </tr>
        </thead>
        <tbody>
          {invoices.map((i) => (
            <tr>
              <th>{i.invoice_id}</th>
              <td>{i.client_name}</td>
              <td>{new Date(i.date).toDateString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
