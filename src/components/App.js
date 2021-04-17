import React, { useState, useEffect } from 'react';
import { Container, Row, Col } from 'reactstrap'
// import '../styles/App.css';
import '../styles/scss2/__main.scss';
import DoctorForm from './DoctorForm'

function App() {

  // output from GPT3 
  // this is currently generated in <DoctorForm />
  const [simpleOutput, setSimpleOutput] = useState("...")

  return (
    <React.Fragment>
      <div id="maincontainer" className="d-flex" style={{ minWidth: "1050px" }}>

        <div id="left_nav"
          style={{ minWidth: "200px", width: "200px", background: "", minHeight: "100vh", boxShadow: "rgb(85 85 85) -6px 0px 18px 0px" }}
          className="p-3">

          {/* Logo section */}
          <div className="d-flex align-items-center">
            <img src="/health.png" style={{ maxWidth: "25px" }} />
            <h4 id="leftTitle" className="mb-0 ml-1">
              Health<span className="font-weight-normal">care</span>
            </h4>
          </div>

          {/* Menu */}
          <hr></hr>
          <div className="mt-5">
            <div style={{ opacity: "0.4", cursor: "pointer" }} className="d-flex align-items-center">
              <img src="/dashboard.png" style={{ maxWidth: "20px" }}></img>
              <h6 className="mb-0 ml-3">Dashboard</h6>
            </div>
            <div style={{ cursor: "pointer" }} className="d-flex align-items-center mt-5 py-2">
              <img src="/patient.png" style={{ maxWidth: "20px" }}></img>
              <h6 style={{ color: "blue" }} className="mb-0 ml-3">Patient</h6>
            </div>
            <div className="d-flex align-items-center mt-5">
              <h6 className="text-muted">...</h6>
            </div>
          </div>

        </div>


        <div id="mainBlock">
          <Container className="p-5">
            <h2>John Doe</h2>
            <div className="mt-5">
              <img src="/skeleton1.png" style={{ maxWidth: "400px" }} />
              <div className="mt-5">
                <DoctorForm />
              </div>
            </div>
          </Container>
        </div>
      </div>

    </React.Fragment>
  );
}

export default App;



/*useEffect(() => {
  console.log("IN USEEFFECT")
  console.log(generate)
  fetch('http://localhost:5000/')
  .then((res) => res.json())
  .then((data) => {
    setDoctorInput(data.doctor_text)
    setSimpleOutput(data.simple_text)
  })
})*/
