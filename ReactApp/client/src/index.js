import React from 'react'
import { render } from 'react-dom'
import Landing from './landing/Landing'

const container = document.getElementById('root')

localStorage.setItem('loggedIn', "false");
localStorage.setItem('username', "user");
localStorage.setItem('pw', "user");

render(<Landing />, container)
