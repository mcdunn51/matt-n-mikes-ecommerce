import React from 'react'
import { Field, reduxForm } from 'redux-form'

let LoginForm = props => {
    const { handleSubmit } = props
    return (
        <form onSubmit={handleSubmit} className="form">
            <div className="form-group">
                <label htmlFor="firstName" className="form-label">First Name</label>
                <Field name="firstName" component="input" type="text" className="form-control" required/>
            </div>
            <div className="form-group">
                <label htmlFor="lastName" className="form-label">Last Name</label>
                <Field name="lastName" component="input" type="text" className="form-control" required/>
            </div>
            <div className="form-group">
                <label htmlFor="email" className="form-label">Email</label>
                <Field name="email" component="input" type="email" className="form-control" required/>
            </div>
            <button type="submit">Submit</button>
        </form>
    )
}

LoginForm = reduxForm({
    form: 'login'
})(LoginForm)


export default LoginForm; 