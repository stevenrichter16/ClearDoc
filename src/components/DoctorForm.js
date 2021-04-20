import React, { useState, useEffect } from 'react';
import { Button, Row, Container, Col } from "reactstrap"
import SimpleOutput from './SimpleOutput'
const axios = require('axios');

function DoctorForm(props) {
    // input from the user (doctor)
    const [doctorInput, setDoctorInput] = useState("")
    // output generated by GPT3
    const [output, setOutput] = useState("...")
    // handles the POST function (sending the input to the Flask server)
    function handleSubmit(e) {
        e.preventDefault()
        console.log({ doctorInput })
        axios.post("http://localhost:5000/", { doctorInput })
            .then(response => {
                console.log(response)
                setOutput(response.data)
            })
            .catch(error => {
                console.log(error)
            })
    }

    // handles user input in the text area
    function onInputChange(e) {
        setDoctorInput(e.target.value)
        console.log({ doctorInput })
    }

    function clear() {
        document.getElementsByTagName("textarea").value=""
    }

    return (
        <div>
            <form onSubmit={handleSubmit}>

                <div className="px-2" style={{ zIndex: "4000", background: "#fff", position: "relative", width: "fit-content" }}>
                    <h4>Clinical Notes</h4>
                </div>

                <Row>
                    <Col>
                        <div style={{ marginTop: "-30px" }}>
                            <textarea
                                name="doctorText"
                                rows="10" cols="50"
                                className="py-5 px-3 mb-4"
                                onChange={e => onInputChange(e)}
                            ></textarea>
                        </div>
                    </Col>
                    <Col>
                        {
                            output ?
                                <div>
                                    <div className="mt-4 d-flex align-items-center">
                                        <div style={{ cursor: "pointer" }} className="d-flex align-items-center">
                                            <img src="/check.png" style={{ maxWidth: "20px" }}></img>
                                            <p className="font-weight-bold mb-0 ml-1">Approve</p>
                                        </div>
                                        <div style={{ cursor: "pointer" }} className="d-flex align-items-center ml-4">
                                            <img src="/edit.png" style={{ maxWidth: "20px" }}></img>
                                            <p className="font-weight-bold mb-0 ml-1">Edit</p>
                                        </div>
                                        <div style={{ cursor: "pointer" }} className="d-flex align-items-center ml-4">
                                            
                                        </div>
                                    </div>
                                    <SimpleOutput text={output} />
                                </div>
                                :
                                ""
                        }

                    </Col>
                </Row>

                <Button color="primary" type="submit">
                    Submit
                </Button>
            </form>
        </div>
    )
}

export default DoctorForm;

//<img src="/retry.png" style={{ maxWidth: "20px" }}></img>
//<p className="font-weight-bold mb-0 ml-1">Retry</p>