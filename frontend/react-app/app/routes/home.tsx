import type { Route } from "./+types/home";
import HomePage from "../home-page/HomePage";

export function meta({}: Route.MetaArgs) {
  return [
    { title: "DegenAI Home Page" },
    { name: "description", content: "Welcome to React Router!" },
  ];
}

export default function Home() {
  return <HomePage/>;
}
