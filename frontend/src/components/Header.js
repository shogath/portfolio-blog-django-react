import React, { useContext } from 'react'
import { Link } from 'react-router-dom';
import AuthContext from '../context/AuthContext';
import '../w3.css'

const Header = () => {

    let { user, logoutUser } = useContext(AuthContext)

    return (
        <div>
            <div className="w3-container w3-left w3-padding">
                <a href="/portfolio/">
                    <button className="w3-button w3-black w3-margin-bottom">
                        <i className="fa fa-paper-plane"></i>My Portfolio
                    </button>
                </a>
            </div>
            <div className="w3-container w3-right w3-padding">
                <Link to="/blog/">
                    <button className="w3-button w3-black w3-margin-bottom">
                        <i className="fa fa-paper-plane"></i>Home
                    </button>
                </Link>
                &nbsp;&nbsp;
                {user ? (
                    <button onClick={logoutUser} className="w3-button w3-black w3-margin-bottom">
                        <i className="fa fa-paper-plane"></i>Logout
                    </button>
                ) : (
                    <Link to="/blog/login">
                        <button className="w3-button w3-black w3-margin-bottom">
                            <i className="fa fa-paper-plane"></i>Login
                        </button>
                    </Link>
                )}
            </div>
            <div className="w3-container w3-center w3-padding-32">
                <h1><b>MY BLOG</b></h1>
                <p>Welcome to the blog of <span className="w3-tag">unknown</span></p>
            </div>
        </div>
    );
}

export default Header;
