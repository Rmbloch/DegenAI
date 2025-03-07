import { type CoinData } from "../types/coinData";
import CoinManager  from "./CoinManager";
import { formatNumber } from "../utils/formatNumbers";

// this displays the coins within the coinData -- DOES NOT HANDLE ANY LOGIC
interface CoinListProps {
    coins: CoinData[];
}

const CoinList = ({ coins }: CoinListProps)  => {
    return(
        <div className="coins-list flex flex-col gap-4 items-center bg-slate-800 p-4 w-full">
            <div className="coins-list__title text-4xl pb-0 font-light max-w-4xl text-white border-slate-700 w-full text-center">
                <label>"Best" Coins</label>
            </div>
            { coins.map((coin, index) => (
                <div 
                    key={coin.coinInformation.id}
                    className="coin pl-0 h-[100px] w-full border-1 border-slate-500 max-w-4xl flex items-center divide-x-2 outline-sky-500 divide-slate-500 rounded-sm shadow-xl px-6 dark:bg-slate-600"
                >
                    <div className="coin__rank flex flex-col justify-center items-center h-full px-5 bg-slate-500">
                        <label className="items-center text-2xl italic">
                            {index+1}
                        </label>
                    </div>
                    <img className="ml-3 size-12 rounded-lg" src={coin.coinImage}/>
                    
                    {/* name */}
                    <div className="h-full flex-1 flex flex-col items-center justify-center px-4">
                        <div className="text-slate-300 italic">
                            <h4>
                                name
                            </h4>
                        </div>
                        <label className="text-2xl line-clamp-2 text-center">
                            {coin.coinInformation.name}
                        </label>
                    </div>

                    {/* price */}
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

                    {/* market cap */}
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

                    {/* circulating */}
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

                    {/* max supply */}
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

                     {/* socials */}
                     <div className="h-full w-32 flex flex-col items-center justify-center">
                        <div className="text-slate-300 italic">
                            <h4>
                                socials
                            </h4>
                        </div>
                        <div className="flex flex-row gap-2 text-center text-white underline font-light text-sm">
                            <a href={coin.coinInformation.twitter}>twitter</a>
                            <a href={coin.coinInformation.coinBaseLink}>coinbase</a>
                        </div>
                    </div>
                </div>
            ))}
        </div>
    )
}

export default CoinList;