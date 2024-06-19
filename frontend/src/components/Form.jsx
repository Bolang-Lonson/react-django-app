/* eslint-disable no-unused-vars */
/* eslint-disable react/prop-types */
import { useState } from "react";
import api from "../api";
import { useNavigate } from "react-router-dom";
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants";
import '../styles/Form.css';
import LoadingIndicator from "./LoadingIndicator";

const Form = ({ route, method }) => {
	const [username, setUsername] = useState("");
	const [password, setPassword] = useState("");
	const [loading, setLoading] = useState(false);
	const navigate = useNavigate();

	const handleSubmit = async (e) => {
        setLoading(true);
		e.preventDefault();

        try {
            const res = await api.post(route, { username, password });
            if (method === 'login') {
                localStorage.setItem(ACCESS_TOKEN, res.data.access);
                localStorage.setItem(REFRESH_TOKEN, res.data.refresh);
                navigate('/');  //  If everything is good, we navigate to login page
            } else {
                navigate('/login')  //  if method was register
            }
        } catch (error) {
            alert(error)
        } finally {
            setLoading(false)
        }
	};

	const activity = (method === "login") ? "Login" : "Register";

	return (
		<form onSubmit={handleSubmit} className="form-container">
			<h1>{activity}</h1>
			<input
				type="text"
				className="form-input"
				placeholder="Username"
				value={username}
				onChange={(e) => setUsername(e.target.value)}
			/>
			<input
				type="password"
				className="form-input"
				placeholder="Password"
				value={password}
				onChange={(e) => setPassword(e.target.value)}
			/>
			{loading && <LoadingIndicator/>}
			<button type="submit" className="form-button">
				{activity}
			</button>
		</form>
	);
};

export default Form;