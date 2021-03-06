import React from 'react'
import { Field, reduxForm } from 'redux-form'

let LoginForm = props => {
    const { handleSubmit } = props
    return (
        <form onSubmit={handleSubmit} className="form">
            <div className="form-group">
                <label htmlFor="username" className="form-label">Username</label>
                <Field name="username" component="input" type="text" className="form-control" required/>
            </div>
            <div className="form-group">
                <label htmlFor="Password" className="form-label">Password</label>
                <Field name="pwd" component="input" type="password" className="form-control" required/>
            </div>
            <button type="submit">Submit</button>
        </form>
    )
}

LoginForm = reduxForm({
    form: 'login'
})(LoginForm)


export default LoginForm; 