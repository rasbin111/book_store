import "@mantine/core/styles.css";
import { MantineProvider } from "@mantine/core";
import { createBrowserRouter } from "react-router";
import { RouterProvider } from "react-router";
import { ApolloProvider } from "@apollo/client/react";
import { client } from "./components/apollo";
import HomePage from "./views/home";
import LoginPage from "./views/login";
import { AuthProvider } from "./context/AuthProvider/AuthProvider";
import Layout from "./components/Layout";

const router = createBrowserRouter([
  {
    Component: Layout,
    children: [
      {
        path: "/",
        Component: HomePage,
      },
    ],
  },
  {
    path: "/login",
    Component: LoginPage,
  },
]);

function App() {
  return (
    <MantineProvider>
      <ApolloProvider client={client}>
          <AuthProvider>
            <RouterProvider router={router} />
          </AuthProvider>
      </ApolloProvider>
    </MantineProvider>
  );
}

export default App;
