import "@mantine/core/styles.css";
import '@mantine/carousel/styles.css';

import { MantineProvider } from "@mantine/core";
import { createBrowserRouter, Navigate } from "react-router";
import { RouterProvider } from "react-router";
import { ApolloProvider } from "@apollo/client/react";
import { client } from "./components/apollo";
import HomePage from "./views/Home";
import LoginPage from "./views/Login";
import { AuthProvider } from "./context/AuthProvider/AuthProvider";
import Layout from "./components/Layout";
import BookPage from "./views/Book";
import PageNotFound from "./views/404NotFound";
import UserLayout from "./components/UserLayout";
import ProfilePage from "./views/User/Profile";
import SettingsPage from "./views/User/Settings";

const router = createBrowserRouter([
  {
    Component: Layout,
    children: [
      {
        path: "/",
        Component: HomePage,
      },
      {
        path: "/books",
        element: <Navigate to="/" replace />,
      },
      {
        path: "/books/:bookId",
        Component: BookPage,
      },
    ],
  },
  {
    Component: UserLayout,
    children: [
      {
        path: "/profile",
        Component: ProfilePage
      },
      {
        path: "/settings",
        Component: SettingsPage
      }
    ]
  },
  {
    path: "/login",
    Component: LoginPage,
  },
  {
    path: "*",
    Component: PageNotFound
  }
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
