

export interface CoinInformation{
    sentiment: number,
    id: number;
    price: number;
    marketCap: number;
    circulating: number;
    maxSupply: number;
    priceChange: Map<string, number>
    twitter: string;
    coinBaseLink: string;
    name: string;
}