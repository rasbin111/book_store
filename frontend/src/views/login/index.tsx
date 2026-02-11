import { useMutation } from "@apollo/client/react"
import { LOGIN } from "../../graphql/auth/userAuth"
import { useForm } from '@mantine/form';
import { TextInput, PasswordInput, Button } from '@mantine/core';
import { useNavigate } from "react-router";
import { useContext } from "react";
import { AuthContext } from "../../context/AuthProvider/AuthContext";
const LoginPage = () => {
  const navigate = useNavigate();
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

      
    }
  })

  const handleLogin = (values: {email: string, password: string}) =>{
    login({
      variables: {
        email: values.email,
        password: values.password
      }
    })
  }
  if (loading) return <p> Loading... </p>

  if (error) return <p> Error: {error.message} </p>

  return (
    <div>
      <h1> Login </h1>
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
        <Button type="submit"> Login </Button>
      </form>
    </div>
  )
}

export default LoginPage