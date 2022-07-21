import React, { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom';
import axiosInstance from '../utils/axiosInstanse';

const RegisterPage = () => {

    let [errors, setErrors] = useState(() => null)

    const navigate = useNavigate()

    useEffect(() => {
        document.title = 'Sign Up'
        setErrors(null)
    }, [])

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const formData = new FormData();
            formData.append('username', e.target.username.value);
            formData.append('email', e.target.email.value);
            formData.append('password', e.target.password.value);
            formData.append('password2', e.target.password2.value);
            await axiosInstance.post('/blog/api/register/',
                formData
            )
            navigate('/blog/login')
        } catch (err) {
            e.target.password.value = ''
            e.target.password2.value = ''
            setErrors(err.response.data)
        }
    }

    return (
        <div className="w3-col l8 s12">
            <div className="w3-card-4 w3-margin w3-white">
                <div className="w3-container w3-padding w3-white">
                    <form onSubmit={handleSubmit}>
                        <div className="w3-section">
                            <label>Username</label>
                            <input className="w3-input w3-border" type="text" name="username" placeholder="Enter username" required />
                        </div>
                        <div className="w3-section">
                            <label>Email</label>
                            <input className="w3-input w3-border" type="text" name="email" placeholder="Enter Email" required />
                        </div>
                        <div className="w3-section">
                            <label>Password</label>
                            <input className="w3-input w3-border" type="password" name="password" placeholder="Enter Password" required />
                        </div>
                        <div className="w3-section">
                            <label>Repeat password</label>
                            <input className="w3-input w3-border" type="password" name="password2" placeholder="Repeat password" required />
                        </div>
                        {errors &&
                            <div className="w3-section">
                                <ul>
                                    {errors.username?.map((error, index) => (
                                        <li key={index} className="w3-padding-16">
                                            <span className="w3-large"><b>{error}</b></span>
                                        </li>
                                    ))}
                                    {errors.email?.map((error, index) => (
                                        <li key={index} className="w3-padding-16">
                                            <span className="w3-large"><b>{error}</b></span>
                                        </li>
                                    ))}
                                    {errors.password?.map((error, index) => (
                                        <li key={index} className="w3-padding-16">
                                            <span className="w3-large"><b>{error}</b></span>
                                        </li>
                                    ))}
                                </ul>
                            </div>
                        }
                        <button type="submit" className="w3-button w3-black w3-margin-bottom">
                            <i className="fa fa-paper-plane"></i>Sign Up
                        </button>
                    </form>
                </div>
            </div >
        </div >
    );
}

export default RegisterPage;
