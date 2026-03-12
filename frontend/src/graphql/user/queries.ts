import { gql } from "@apollo/client"

export const USER_BY_ID = gql `
query userById($id:ID!){
  userById(id:$id){
    id
    username
    firstName
    middleName
    lastName
    gender
    email
    email
    createdAt
    role
    avatar
    address{
      id
      addressType
      city
      country
      street
      postalCode
      phoneNumber
      altPhoneNumber
    }
    userOrders{
      orderId
      orderAmount
      expectedDeliveryDate
    }
  }
}
`