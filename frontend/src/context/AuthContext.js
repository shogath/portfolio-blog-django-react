import { createContext, useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import jwt_decode from "jwt-decode";
import axiosInstance from "../utils/axiosInstanse";

const AuthContext = createContext()

export default AuthContext;


export const AuthProvider = ({ children }) => {

    let [authTokens, setAuthTokens] = useState(() => localStorage.getItem('authTokens') ? JSON.parse(localStorage.getItem('authTokens')) : null)
    let [user, setUser] = useState(() => localStorage.getItem('authTokens') ? jwt_decode(localStorage.getItem('authTokens')) : null)
    let [loading, setLoading] = useState(true)
    let [errors, setErrors] = useState(() => null)

    let navigate = useNavigate()

    let loginUser = async (e) => {
        e.preventDefault()
        try {
            let response = await axiosInstance.post('/blog/api/login/', {
                headers: {
                    'Content-Type': 'application/json'
                },
                email: e.target.email.value,
                password: e.target.password.value
            })
            setAuthTokens(response.data)
            setUser(jwt_decode(response.data.access))
            localStorage.setItem('authTokens', JSON.stringify(response.data))
            navigate('/blog')
        } catch (err) {
            e.target.password.value = ''
            setErrors(err.response.data)
        }
    }

    let logoutUser = () => {
        setAuthTokens(null)
        setUser(null)
        localStorage.removeItem('authTokens')
        navigate('/blog')
    }

    let contextData = {
        user: user,
        loginUser: loginUser,
        logoutUser: logoutUser,
        errors: errors,
        setErrors: setErrors
    }

    useEffect(() => {

        if (authTokens) {
            setUser(jwt_decode(authTokens.access))
        }
        setLoading(false)

    }, [authTokens, loading])

    return (
        <AuthContext.Provider value={contextData}>
            {children}
        </AuthContext.Provider>
    )
}
