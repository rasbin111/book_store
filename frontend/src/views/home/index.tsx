import {useAuth} from "../../hooks/useAuth"

const HomePage = () => {
    const {isHost} = useAuth();
  return (
    <div>
        <h1> Home Page </h1>
        <div> User Posts</div>
        {isHost && <div> Edit options </div>}

    </div>
  )
}

export default HomePage