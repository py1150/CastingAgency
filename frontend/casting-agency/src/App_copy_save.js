//import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        {/* <img src={logo} className="App-logo" alt="logo" />*/ }
        <span>Photo by <a href="https://unsplash.com/@felixmooneeram?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Felix Mooneeram</a> on <a href="https://unsplash.com/s/photos/movie?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span>
        <p>
          Agency App <code>src/App.js</code> and save to reload.
        </p>
        {/*<a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Login
        </a>*/}
        {/*<a href="{{AUTH0_AUTHORIZE_URL}}">Login</a>*/}
        <a href="https://py1150.eu.auth0.com/authorize?audience=agency&response_type=token&client_id=EeYJIGaf3frKfj1nRwclF8nA9N88wYpz&redirect_uri=http://localhost:3000">Login</a>
      </header>
    </div>
  );
}

export default App;
