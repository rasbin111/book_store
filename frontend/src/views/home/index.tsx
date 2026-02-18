import {useAuth} from "../../hooks/useAuth"

const HomePage = () => {
    const {isEditor, isAdmin} = useAuth();
  return (
    <div>
        <h1> Home Page </h1>
        <div> User Posts</div>
        {(isEditor || isAdmin) && <div> Edit options </div>}

    </div>
  )
}

export default HomePage