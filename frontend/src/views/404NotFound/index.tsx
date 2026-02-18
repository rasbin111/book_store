import { Link } from "react-router"

import "./styles.scss"

const PageNotFound = () => {
  return (
    <div className='main'>
      <h1>404 | Not Found </h1>
      <p> You seem lost. Please visit <Link to="/"> Dashboard </Link> </p>
    </div>
  )
}

export default PageNotFound