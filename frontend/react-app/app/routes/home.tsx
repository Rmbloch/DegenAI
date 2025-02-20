import type { Route } from "./+types/home";
import { DisplayPage } from "../display-page/displayPage";

export function meta({}: Route.MetaArgs) {
  return [
    { title: "New React Router App" },
    { name: "description", content: "Welcome to React Router!" },
  ];
}

export default function Home() {
  return <DisplayPage/>;
}
