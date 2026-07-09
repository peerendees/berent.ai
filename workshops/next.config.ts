import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  async rewrites() {
    return [
      {
        source: "/hedy-2604",
        destination: "/hedy-2604/index.html",
      },
      {
        source: "/hedy-2604/danke",
        destination: "/hedy-2604/danke/index.html",
      },
    ];
  },
};

export default nextConfig;
