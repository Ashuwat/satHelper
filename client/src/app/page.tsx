"use client";

import React from "react";
import Image from "next/image";
import { useRouter } from "next/navigation";

const statements = [
  "progressive learning on another level",
  "fast and free way to learn the SAT",
  "instead of paying $1600, get a 1600",
  "only 10 minutes a day is all you need",
];

const TypeAnimation = () => {
  const [text, setText] = React.useState("");
  const [index, setIndex] = React.useState(0);
  const [charIndex, setCharIndex] = React.useState(0);
  const [isDeleting, setIsDeleting] = React.useState(false);

  React.useEffect(() => {
    const currentStatement = statements[index];
    if (!isDeleting && charIndex < currentStatement.length) {
      const timeout = setTimeout(() => {
        setText((prev) => prev + currentStatement[charIndex]);
        setCharIndex((prev) => prev + 1);
      }, 100);
      return () => clearTimeout(timeout);
    } else if (isDeleting && charIndex > 0) {
      const timeout = setTimeout(() => {
        setText((prev) => prev.slice(0, -1));
        setCharIndex((prev) => prev - 1);
      }, 50);
      return () => clearTimeout(timeout);
    } else if (!isDeleting && charIndex === currentStatement.length) {
      const timeout = setTimeout(() => setIsDeleting(true), 2000);
      return () => clearTimeout(timeout);
    } else if (isDeleting && charIndex === 0) {
      setIndex((prev) => (prev + 1) % statements.length);
      setIsDeleting(false);
    }
  }, [charIndex, isDeleting, index]);

  return (
    <div className="relative inline-block">
      <span className="text-white text-2xl font-serif">{text}</span>
      <span className="inline-block w-2 h-[1em] bg-white animate-blink ml-1">
        |
      </span>
    </div>
  );
};

const SearchBar = () => {
  const [query, setQuery] = React.useState("");
  const router = useRouter();

  const handleKeyDown = (event: KeyboardEvent) => {
    if (event.key === "Enter" && query.trim()) {
      sessionStorage.setItem("searchQuery", query.trim());
      router.push("/prepquestion"); // Change this to the actual route
    }
  };

  return (
    <div className="relative w-full max-w-2xl mx-auto group">
      <div className="bg-white rounded-full border-4 border-[#4b9fe1] shadow-md px-6 py-3">
        <input
          type="text"
          className="w-full text-gray-600 outline-none text-lg text-center"
          placeholder="type your homework question and we'll find the rest:"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyDown={handleKeyDown}
        />
      </div>
    </div>
  );
};

export default function HomePage() {
  return (
    // The outer container has a plain white background.
    <div className="min-h-screen relative bg-white">
      {/* Navigation Bar */}
      <nav className="fixed top-0 left-0 w-full bg-[#1e1e1e] flex items-center px-6 py-4 z-30">
        {/* Replace '/logo.png' with your actual logo image path */}
        <Image src="/logo.png" alt="Logo" width={50} height={50} />
      </nav>

      {/* Tile Background (separate from the white background)
          This layer is over the white background (from the container)
          but behind the blue hero section (z-index lower than the blue section) */}
      <div className="absolute inset-0 z-0">
        <div
          className="h-full w-full bg-[url('/icon-tiles.png')] bg-[length:200px_200px] bg-center opacity-40"
          style={{ clipPath: "polygon(0 30%, 100% 20%, 100% 100%, 0 100%)" }}
        />
      </div>

      {/* Main Content – Blue Section with Slanted Background and Search Bar */}
      {/* Add top padding so the content is not hidden under the fixed nav */}
      <div className="relative z-10 pt-20">
        <div
          className="relative h-[70vh] bg-[#324DC7]"
          style={{ clipPath: "polygon(0 0, 100% 0, 100% 85%, 0 100%)" }}
        >
          <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full px-4">
            <div className="text-center mb-8">
              <TypeAnimation />
            </div>
            <SearchBar />
          </div>
        </div>

        {/* Fetch.ai Badge */}
        <div className="absolute bottom-8 left-1/2 -translate-x-1/2 z-20">
          <div className="bg-white rounded-lg border-2 border-[#4b9fe1] px-8 py-4 text-center shadow">
            <div className="text-gray-600 mb-2">supercharged by</div>
            <div className="flex items-center justify-center space-x-2">
              <Image
                src="/fetch-ai-logo.png"
                alt="Fetch.ai"
                width={80}
                height={30}
              />
              <p className="text-black">Fetch.ai</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
