import { getProduct } from "../api/products";
import { useQuery } from "@tanstack/react-query";
import { useParams } from "react-router-dom";
import Loader from "../components/Loader";
import { toast } from "react-hot-toast";
import Reviews from "../components/Reviews";
import { Product } from "../Interfaces";
import { useCartStore } from "../store/cart";

interface Props {
    product: Product
}

const SoloProduct = ({ product }: Props) => {

    const addToCart = useCartStore(state => state.addToCart)

    const { nombre } = useParams();
    

    const { data,  isLoading, error } = useQuery
    (['product', nombre], () => getProduct(nombre));

    if (isLoading) return <Loader/>
    if(error instanceof Error) return <>{toast.error(error.message)}</>

    return (
    <>
        <div className="bg-white dark:bg-gray-900">
        <div className="gap-16 items-center py-8 px-4 mx-auto max-w-screen-xl lg:grid lg:grid-cols-2 lg:py-16 lg:px-6">
        <div className="font-light text-gray-500 sm:text-lg dark:text-gray-400">
            <h2 className="mb-4 text-4xl tracking-tight font-extrabold text-gray-900 dark:text-white">
                {data.nombre}
                <span className="text-green-300 ml-4">
                ${data.precio}
                </span>
                
            </h2>
            <p className="mb-4 font-bold">
                {data.descripcion}
            </p>
            
            <button 
        onClick={() => addToCart(product)}
        className="inline-flex items-center mx-3 px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
        Añadir al carro
        
    <svg aria-hidden="true" className="w-4 h-4 ml-2 -mr-1" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
        <path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd">
        </path>
        </svg>
        </button>
            </div>

            <img 
            src={`http://127.0.0.1:8000${data.imagen}`} alt="office content 1" />

            </div>
            </div>

<Reviews/>

</>


           )

};
export default SoloProduct;