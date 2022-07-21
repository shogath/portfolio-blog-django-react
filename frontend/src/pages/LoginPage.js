import React, { useContext, useEffect } from 'react'
import AuthContext from '../context/AuthContext';
import { Link } from 'react-router-dom';

const LoginPage = () => {

    let { loginUser, errors, setErrors } = useContext(AuthContext)

    useEffect(() => {
        document.title = 'Login'
        setErrors(null)
    }, [setErrors])


    return (
        <div className="w3-col l8 s12">
            <div className="w3-card-4 w3-margin w3-white">
                <div className="w3-container w3-padding w3-white">
                    <form onSubmit={loginUser}>
                        <div className="w3-section">
                            <label>Email</label>
                            <input className="w3-input w3-border" type="text" name="email" placeholder="Enter Email" required />
                        </div>
                        <div className="w3-section">
                            <label>Password</label>
                            <input className="w3-input w3-border" type="password" name="password" placeholder="Enter Password" required />
                        </div>
                        {errors &&
                            <div className="w3-section">
                                <ul>
                                    {Object.values(errors)?.map((error, index) => (
                                        <li key={index} className="w3-padding-16">
                                            <span className="w3-large"><b>{error}</b></span>
                                        </li>
                                    ))}
                                </ul>
                            </div>
                        }
                        <button type="submit" className="w3-button w3-black w3-margin-bottom">
                            <i className="fa fa-paper-plane"></i>Login
                        </button>
                        &nbsp;&nbsp; or &nbsp;&nbsp;
                        <Link to={'/blog/register'}>
                            <button className="w3-button w3-black w3-margin-bottom">
                                <i className="fa fa-paper-plane"></i>Sign Up
                            </button>
                        </Link>
                    </form>
                </div>
            </div >
        </div >
    );
}

export default LoginPage;
