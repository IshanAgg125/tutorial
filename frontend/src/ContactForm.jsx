/* eslint-disable react/prop-types */
/* eslint-disable no-empty-pattern */
/* eslint-disable no-unused-vars */
import {useState} from "react"


const ContactForm = ({ exisitingContact = {}, updateCallBack}) => {
    const [firstName, setFirstName] = useState(exisitingContact.firstName || "")
    const [lastName, setLastName] = useState(exisitingContact.lastName || "")
    const [email, setEmail] = useState(exisitingContact.email || "")

    const updating = Object.entries(exisitingContact).length !== 0
    // if it is not a new object, then we update it because it has some entries.

    const onSubmit = async (e) => {
        // Once the submit button is clicked, this is where the code will come next
        e.preventDefault()
        // calling the post function 
        const data = {
            firstName,
            lastName,
            email
        }
        const url = "http://127.0.0.1:5000/" + (updating ? `update_contact/${exisitingContact.id}`: "create_contact")
        // updating or creating
        const options = {
            method: updating ? "PATCH" : "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
        const response = await fetch(url, options)
        if(response.status !== 201 && response.status !== 200) {
            const message = await response.json()
            alert(data.message)
        } else {
            updateCallBack()
        }
    }

    return <form onSubmit={onSubmit}> 
    
        <div>
            <label htmlFor="firstName">First Name:</label>
            <input type="text"
                   id ="firstName"
                   value={firstName}
                   onChange = {(e) => setFirstName(e.target.value)}
            />
            <label htmlFor="lastName">Last Name: </label>
            <input type="text"
                   id ="lastName"
                   value={lastName}
                   onChange = {(e) => setLastName(e.target.value)}
            />
            <label htmlFor="email">Email: </label>
            <input type="text"
                   id ="email"
                   value={email}
                   onChange = {(e) => setEmail(e.target.value)}
            />
        </div>
        <button type="submit">{updating ? "update" : "Create Contact"}</button>
    </form>
}

export default ContactForm
