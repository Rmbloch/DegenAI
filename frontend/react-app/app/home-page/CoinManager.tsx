// there is no UX representation of the coin manager; it is just responsible for managing the state of "Coin" components
import { type CoinData } from "../types/coinData";
import Coin from "../components/Coin";
import CoinList from "../home-page/CoinList";
import { useState } from 'react';


// test resources
import cryptoLogo from './crypto_logo.png'

interface CoinManagerProps {
    initialCoins?: CoinData[];
}

// test coins
const testCoin: CoinData = {
    coinInformation: {
        sentiment: 0.5,
        id: 0,
        price: 89601.75,
        marketCap: 1774115397519,
        circulating: 19833190,
        maxSupply: 21000000,
        priceChange: new Map<string, number>,
        twitter: "https://x.com/?lang=en",
        coinBaseLink: "https://www.coinbase.com/",
        name: "Bitcoin"
    },
  
    coinImage: cryptoLogo
  }

const CoinManager = ({ initialCoins = [] }: CoinManagerProps) => {

    // define a reactive state for the coins...
    const [coins, setCoins] = useState<CoinData[]>(initialCoins);

    // adding a coin to the coins list.
    const addCoin = (coinData: CoinData) => {
        console.log("{+} Attempting to add a coin...")
        // have to do this bearing in mind immutability
        setCoins(prev => [...prev, coinData])
    };
    
    // removing a coin from the coins list
    const deleteCoin = (coinData: CoinData) => {
        console.log("{+} Attempting to delete a coin...")
        // again, remember immutability...
        setCoins(prev => prev.filter(coin => coin.coinInformation.id !== coinData.coinInformation.id))
    };

    return (
        <>
            <CoinList coins={coins}/>
            <button onClick={() => addCoin(testCoin)}>Add Test Coin</button>
        </>
    );
}

export default CoinManager;