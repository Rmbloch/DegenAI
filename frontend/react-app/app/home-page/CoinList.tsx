import { type CoinData } from "../types/coinData";
import CoinManager  from "./CoinManager";
import { formatNumber } from "../utils/formatNumbers";

// this displays the coins within the coinData -- DOES NOT HANDLE ANY LOGIC
interface CoinListProps {
    coins: CoinData[];
}

const CoinList = ({ coins }: CoinListProps)  => {
    return(
        <div className="coins-list flex flex-col gap-4 items-center bg-white p-4 w-full max-w-[calc(100%-300px)] mx-auto">
            <div className="coins-list__title font-['Molle'] text-4xl pb-0 max-w-xl text-black bg-none w-full text-center">
                <label className="inline-block align-bottom leading-none">Degen Ai</label>
            </div>
            { coins.map((coin, index) => (
                <div 
                    key={coin.coinInformation.id}
                    className="coin pl-0 h-[100px] w-full max-w-4x flex items-center divide-black rounded-sm shadow-lg px-6 coin-entering"
                >
                    <div className="coin__rank flex flex-col justify-center items-center h-full p-5 w-1 bg-black">
                        <label className="items-center text-2xl text-white italic">
                            {index+1}
                        </label>
                    </div>
                    <img className="ml-3 mr-0 size-20 rounded-full drop-shadow-lg" src={coin.coinImage}/>
                    
                    {/* name */}
                    <div className="h-full flex-1 flex flex-col items-center justify-center px-4">
                        {/*
                        <div className="text-slate-300 italic">
                            <h4>
                                name
                            </h4>
                        </div>
                        */}
                        <label className="text-2xl text-black line-clamp-2 text-center">
                            {coin.coinInformation.name}
                        </label>
                        <div className="text-gray-500 italic">
                            <h4>
                                {coin.coinInformation.symbol}
                            </h4>
                        </div>
                    </div>

                    <div className="h-full w-32 flex flex-col items-center justify-center">
                        <div className="text-gray-500 italic">
                            <h4>
                                sentiment
                            </h4>
                        </div>
                        <label className="text-center font-bold text-black">
                             {coin.coinInformation.sentiment}
                        </label>
                    </div>

                    {/* price 
                    <div className="h-full w-32 flex flex-col items-center justify-center">
                        <div className="text-slate-300 italic">
                            <h4>
                                price
                            </h4>
                        </div>
                        <label className="text-center font-bold">
                            ${formatNumber(coin.coinInformation.price)}
                        </label>
                    </div>
                    */}
                    

                    {/* market cap 
                    <div className="h-full w-32 flex flex-col items-center justify-center">
                        <div className="text-slate-300 italic">
                            <h4>
                                market cap
                            </h4>
                        </div>
                        <label className="text-center font-bold">
                            ${formatNumber(coin.coinInformation.marketCap)}
                        </label>
                    </div>
                    */}

                    {/* circulating 
                    <div className="h-full w-32 flex flex-col items-center justify-center">
                        <div className="text-slate-300 italic">
                            <h4>
                                circulating
                            </h4>
                        </div>
                        <label className="text-center font-bold">
                            ${formatNumber(coin.coinInformation.circulating)}
                        </label>
                    </div>
                    */}

                    {/* max supply 
                    <div className="h-full w-32 flex flex-col items-center justify-center">
                        <div className="text-slate-300 italic">
                            <h4>
                                max supply
                            </h4>
                        </div>
                        <label className="text-center font-bold">
                            ${formatNumber(coin.coinInformation.maxSupply)}
                        </label>
                    </div>
                    */}

                     {/* socials */}
                     <div className="h-full w-32 flex flex-col items-center justify-center">
                        <div className="text-gray-500 italic">
                            <h4>
                                link
                            </h4>
                        </div>
                        <div className="flex flex-row gap-2 text-center text-black underline font-light text-sm">
                            <a href={coin.coinInformation.url}>pump.fun link</a>
                        </div>
                    </div>
                </div>
            ))}
        </div>
    )
}

export default CoinList;