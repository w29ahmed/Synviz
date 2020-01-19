import React, { Component } from 'react';
import { Route, Switch, BrowserRouter } from 'react-router-dom';
/*the main page*/
import App from '../App'
import './style.css';
import LoginBox from '../login/LoginBox';

/* main app component*/

class Landing extends Component {

	render() {
		console.log("landing page")
		const loggedIn = localStorage.getItem('loggedIn') === "true";
		console.log("log in? " + loggedIn)
		return(
			<div>
				<BrowserRouter>
				    <Switch> { /* Similar to a switch statement - shows the component depending on the URL path */ }
		            { /* Each Route below shows a different component depending on the exact path in the URL  */ }
						<Route exact path='/' component={loggedIn ? App : LoginBox}/>
						<Route exact path='/App' component={App}/>
					</Switch>
	        	</BrowserRouter>
			</div>
		)
	}
}

export default Landing;  /* export the App component from this module.*/
