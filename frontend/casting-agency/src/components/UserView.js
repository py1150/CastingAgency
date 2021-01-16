import React, { Component } from 'react';
import '../App.css';



class UserView extends Component {
    render() {
     return (
       <div>
           <p>User logged in</p>
           <p>
            <a href="https://py1150.eu.auth0.com/v2/logout?client_id=EeYJIGaf3frKfj1nRwclF8nA9N88wYpz&returnTo=http://localhost:3000">Logout</a>
           </p>
      </div>
     );
   }
  }




export default UserView;