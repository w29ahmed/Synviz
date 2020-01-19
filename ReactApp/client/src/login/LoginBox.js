import React, { Component } from 'react';
import { Redirect } from 'react-router-dom';

// Importing actions/required methods
import ErrorMessage from "../error"
import './Login.css';

class LoginBox extends Component{
    constructor(props) {
        super(props);
        this.state = {
            redirect: false,
            failed: false,
            username: "",
            password: ""}
    }
    
    updateUsernameForm = value => {
        this.setState({username: value})
        console.log("Username: " + this.state.username)
    }

    updatePasswordForm = value => {
        this.setState({password: value})
        console.log("Password: " + this.state.password)
    }

    setRedirect = () => {
        this.setState({
          redirect: true
        })
        console.log("Redirect: " + this.state.redirect)
    }

    renderRedirect = () => {
        if (this.state.redirect) {
            return <Redirect to='/App' />
        }
        console.log("Redirect to App")
    }

    login = () => {
        if (this.state.username === localStorage.getItem('username') && 
        this.state.password === localStorage.getItem('pw')) {
            localStorage.setItem('loggedIn', "true");
            this.setRedirect()
        }
        console.log("Login Status: " + localStorage.getItem('loggedIn'))
    }

    render(){
        return(
            <div className="box-container">
            {this.renderRedirect()}
                <div className= "inner-container">
                    <div className="header">
                        Login
                    </div>

                    <div classNme="box">
                        <div className="input-group">
                            <label htmlFor="username" className="login-label">Username</label>
                            <input
                                type="text"
                                name="username"
                                className="login-input"
                                placeholder="Username"
                                onChange={e => this.updateUsernameForm(e.target.value)}
                            />                       
                        </div>

                        <div className="input-group">
                            <label htmlFor="password" className="login-label">Password</label>
                            <input
                                type="password"
                                name="password"
                                className="login-input"
                                placeholder="Password"
                                onChange={e => this.updatePasswordForm(e.target.value)}
                            />                      
                        </div>
                        
                        <button
                            type="button"
                            className="login-btn"
                            onClick={this.login}                     
                        >
                            Login
                        </button>        
                    </div>            
                </div>
                <small className = "login-err">
                        {
                            this.state.failed ?  <ErrorMessage/> : ""
                        }
                </small>
            </div>
        )
    }
}
export default LoginBox;