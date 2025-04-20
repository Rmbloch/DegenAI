import CoinList from "./CoinList";
import CoinManager from "./CoinManager";
import { type CoinData } from "../types/coinData";


const HomePage = () => {
  return (
    <>
      <main className="home-page">
        <div className="coin-manager">
          <CoinManager/>
        </div>
      </main>
    </>
  );
}

export default HomePage;

