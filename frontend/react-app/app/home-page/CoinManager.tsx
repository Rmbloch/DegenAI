// there is no UX representation of the coin manager; it is just responsible for managing the state of "Coin" components
import { type CoinData } from "../types/coinData";
import Coin from "../components/Coin";
import CoinList from "../home-page/CoinList";
import { useState, useEffect } from 'react';


// test resources
import cryptoLogo from './crypto_logo.png'

interface CoinManagerProps {
    initialCoins?: CoinData[];
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

    const updateCoins = (coinData: CoinData[]) => {
        setCoins(coinData);
    };

    // wrapping this in a useEffect to poll the API every 10 seconds
    useEffect(() => {
        // setting some debouncing vars
        let isMounted = true;
        let timeoutId: NodeJS.Timeout;

        // poll data function. sets the coins list every 10 seconds
        const pollData = () => {
            if (!isMounted) return;

            fetch('http://localhost:5000/api/coins')
            .then(response => response.json())
            .then(data => {
                if (!isMounted) return;
                
                // filter out duplicate URLs
                // urls will ALWAYS be unique.
                const seenUrls = new Set<string>();
                const newCoinData: CoinData[] = [];

                data.forEach((coin: any) => {
                    if (!seenUrls.has(coin.url)) {
                        seenUrls.add(coin.url);
                        newCoinData.push({
                            coinInformation: {
                                sentiment: coin.sentiment_score,
                                id: coin.url,
                                name: coin.name,
                                url: "https://pump.fun/coin/" + coin.url,
                                symbol: coin.symbol,
                                price: 0,
                            },
                            coinImage: coin.image_url
                        });
                    }
                });

                setCoins(newCoinData);
            })
            .catch(console.error)
            .finally(() => {
                if (isMounted) {
                    timeoutId = setTimeout(pollData, 10000);
                }
            });
        };

        pollData();

        return () => {
            isMounted = false;
            clearTimeout(timeoutId);
        };
    }, []); // no dependencies, so this runs once on mount
    return (
        <>
            <CoinList coins={coins}/>
        </>
    );
}



export default CoinManager;