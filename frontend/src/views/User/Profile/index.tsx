import { useQuery } from "@apollo/client/react";
import "./styles.scss";
import { USER_BY_ID } from "../../../graphql/user/queries";
import CustomLoadinOverlay from "../../../components/CustomLoadingOverlay";
import useAuth from "../../../hooks/useAuth";
import { type UserByIdData } from "../../../types/userTypes";

const ProfilePage = () => {
  const { userId } = useAuth();
  const { loading, data, error } = useQuery<UserByIdData>(USER_BY_ID, {
    variables: {
      id: userId,
    },
  });

  if (loading) {
    return <CustomLoadinOverlay />;
  }

  if (error) {
    console.log(error);
  }

  return (
    <div className="user-profile-content">
      {data && data.userById && (
        <div className="user-profile-main">
          <div className="basic-info">
            <h2> Basic Info </h2>
            <div className="info-item">
              <span className="bi-key">Full Name: </span>
              <span className="bi-value">
                {data.userById.firstName} {data.userById.middleName}{" "}
                {data.userById.lastName}
              </span>
            </div>
            <div className="info-item">
              <span className="bi-key">Email: </span>
              <span className="bi-value">
                {data.userById.email}
              </span>
            </div>
            <div className="info-item">
              <span className="bi-key">Role: </span>
              <span className="bi-value capitalize">
                {data.userById.role}
              </span>
            </div>
            <div className="info-item">
              <span className="bi-key">Gender: </span>
              <span className="bi-value capitalize">
                {data.userById.gender}
              </span>
            </div>
          </div>
          {
            data.userById.userOrders && 
            <div className="orders-container">
              <h2> My Orders </h2>
              <div className="order-item">
                
              </div>
            </div>
          }
        </div>
      )}
    </div>
  );
};

export default ProfilePage;
