import { useMutation } from "@apollo/client/react"
import { LOGIN } from "../../graphql/auth/userAuth"
import { useForm } from '@mantine/form';
import { TextInput, PasswordInput, Button } from '@mantine/core';
import { useNavigate, Navigate} from "react-router";
import { useContext } from "react";
import { AuthContext } from "../../context/AuthProvider/AuthContext";
import useAuth from "../../hooks/useAuth";

const LoginPage = () => {
  const navigate = useNavigate();
  const {isLoggedIn} = useAuth();
  const form = useForm({
    "mode": "uncontrolled",
    initialValues: {
      email: "",
      password: "",
    }
  })

  const context = useContext(AuthContext)

  if (context == undefined){
    throw Error("Auth context error")
  }

  const {setUser} = context;

  const [login, {loading, error}] = useMutation(LOGIN, {
    onCompleted: (data: any) => {
      const token = data.tokenAuth.token;
      const user = data.tokenAuth.user;
      if (token){
        localStorage.setItem("token", token);
        localStorage.setItem("user", JSON.stringify(user));
        setUser(user);
        navigate("/", {replace: true})
      }

      
    },
    onError: () => {}
  })

    const handleLogin = (values: {email: string, password: string}) =>{
    login({
      variables: {
        email: values.email,
        password: values.password
      }
    })
  }

    if (isLoggedIn){
      return <Navigate to="/" replace />
  }


  // if (loading) return <p> Loading... </p>


  return (
    <div>
      <h1> Login </h1>
      {error && (
        <div style={{ color: 'red', marginBottom: '10px', fontWeight: 'bold' }}>
          {error.message}
        </div>
      )}
      <form onSubmit={form.onSubmit(handleLogin)}>
        <TextInput 
        label="Email"
        placeholder="Email"
        key={form.key("email")}
        {...form.getInputProps("email")}
        />
        <PasswordInput
        label="Password"
        placeholder="Password"
        key={form.key("password")}
        {...form.getInputProps("password")}
        />
        <Button type="submit" color="#7c2d38" loading={loading}> Login </Button>
      </form>
    </div>
  )
}

export default LoginPage