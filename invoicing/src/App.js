import logo from "./logo.svg";
import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import InvoiceList from "./components/InvoiceList/InvoiceList";
import InvoiceForm from "./components/InvoiceForm/InvoiceForm";
import InvoiceItems from "./components/InvoiceItems/InvoiceItems";
import ItemForm from "./components/ItemForm/ItemForm";
import Login from "./components/Login";
import PrivateRoute from "./components/PrivateRoute";
import { useState } from "react";

function App() {
  const [auth, setAuth] = useState(false);
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/login" element={<Login setAuth={setAuth} />} />
          <Route
            path=""
            element={
              <PrivateRoute auth={auth}>
                <InvoiceList />
              </PrivateRoute>
            }
          ></Route>
          <Route
            path="newInvoice"
            element={
              <PrivateRoute auth={auth}>
                <InvoiceForm />
              </PrivateRoute>
            }
          ></Route>
          <Route
            path="/:id"
            element={
              <PrivateRoute auth={auth}>
                <InvoiceItems />
              </PrivateRoute>
            }
          ></Route>
          <Route
            path="/:id/newItem"
            element={
              <PrivateRoute auth={auth}>
                <ItemForm />
              </PrivateRoute>
            }
          ></Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
