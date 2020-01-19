import React from 'react';
import { Menu, Icon, Typography} from 'antd';
import { Link } from 'react-router-dom';
import 'antd/dist/antd.css';
import { withRouter } from 'react-router-dom';

const { Title } = Typography;
class Navigation extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            current: 'mail',
            loggedIn: true
        }
    }

    logout = () => {
        localStorage.setItem('loggedIn', "false");
        this.setState({ loggedIn: false})
    }

  render() {
      const { loggedIn } = this.state;
    console.log("rendering navigation")
    return (
      <Menu selectedKeys={[this.state.current]} mode="horizontal"  style={{'marginTop': 8, 'marginBottom': 8 }}>
        <Menu.Item key="logo" style={{'width': '20%', 'marginLeft': 10}}>
          <Link to={'/'}>
            <Icon type="home" style={{'font-size': 25}}/>
          </Link>
        </Menu.Item>
        <Menu.Item key="name" style={{'width': '60%', 'text-align': 'center'}}>
          <Link to={'/'}>
            <Title level={3} style={{"color": "#4682B6"}}>Synviz</Title>      
          </Link>
        </Menu.Item>
        <Menu.Item key="LOGOUT" style={{'paddingLeft': 20, 'paddingRight': 20}} id="floatRight" onClick={this.logout}>
         <Link to={ loggedIn ? '/App' : '/'}>
            <Title level={3} style={{"color": "#4682B6"}}>Log out</Title>
          </Link>   
        </Menu.Item>
      </Menu>
    );
  }
}
export default withRouter(Navigation);
