import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        bg: "#090806",
        card: "#110E0A",
        border: "#2A2118",
        copper: "#B5742A",
        gold: "#E8C98A",
        text: "#C4BCB1",
        muted: "#7A6A58",
        muted2: "#9A8870",
      },
      fontFamily: {
        headline: ["Bebas Neue", "sans-serif"],
        body: ["Lora", "serif"],
        label: ["JetBrains Mono", "monospace"],
      },
      letterSpacing: {
        headline: "0.04em",
      },
    },
  },
};

export default config;
