export type UserRole = "ADMIN" | "EDITOR" | "VIEWER";

export interface AuthUser {
  id: number;
  username: string;
  email: string;
  role: UserRole;
  isActive: boolean;
  isVerfied: boolean;
}

export interface AuthContextType {
  user: AuthUser | null;
  setUser: (user: AuthUser | null) => void;
}

export interface UserOrder {
  orderId: string;
  orderAmount: number;
  expectedDeliveryDate: string; // Typically ISO string from GraphQL
}

export interface Address {
  id: string;
  addressType: string;
  city: string;
  country: string;
  street: string;
  postalCode: string;
  phoneNumber: string;
  altPhoneNumber?: string | null;
}

export interface User {
  id: string;
  username: string;
  firstName: string;
  middleName: string;
  lastName: string;
  gender: string;
  email: string;
  avatar: string;
  createdAt: string;
  role: string;
  address?: Address | null;
  userOrders?: UserOrder[] | null;
}

export interface UserByIdData {
  userById: User;
}
