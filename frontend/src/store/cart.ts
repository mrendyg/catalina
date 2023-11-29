import { create } from "zustand"
import { persist } from "zustand/middleware";
import { Product } from "../Interfaces";

interface State {
 cart: Product[]
 totalPrice: number
}

interface Actions {
 addToCart: (Item: Product) => void
 removeFromCart: (Item: Product) => void
}

const State = {
 cart: [],
 totalPrice: 0,
}

export const useCartStore = create(persist<State & Actions>((set, get) => ({
 cart: State.cart,
 totalPrice: State.totalPrice,

 addToCart: (product: Product) => {
  const cart = get().cart
  const cartItem = cart.find(item => item.id === product.id)

  if (cartItem) {
   const updatedCart = cart.map(item =>
    item.id === product.id ? { ...item, cantidad: (item.cantidad as number) + 1 } : item
   )
   set(state => ({
    cart: updatedCart,
    totalPrice: state.totalPrice + Number(product.precio),
   }))
  } else {
   const updatedCart = [...cart, { ...product, cantidad: 1 }]

   set(state => ({
    cart: updatedCart,
    totalPrice: state.totalPrice + Number(product.precio),
   }))
  }
 },

 removeFromCart: (product: Product) => {
  const cart = get().cart
  const cartItem = cart.find(item => item.id === product.id)

  if (cartItem && cartItem.cantidad && cartItem.cantidad > 1) {
   const updatedCart = cart.map(item =>
    item.id === product.id ? { ...item, quantity: (item.cantidad as number) - 1 } : item
   )
   set(state => ({
    cart: updatedCart,
    totalPrice: state.totalPrice - Number(product.precio),
   }))
  } else {
    set(state => ({
        cart: state.cart.filter(item => item.id !== product.id),
        totalPrice: state.totalPrice - Number(product.precio),
    }))
  }
 },
}),

{
      name: "cart-storage",
}

))