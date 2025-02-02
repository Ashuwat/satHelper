"use client";

import React, { useState, useEffect } from "react";

const statements = [
  "progressive learning on another level",
  "fast and free way to learn the SAT",
  "instead of paying $1600, get a 1600",
  "only 10 minutes a day is all you need",
];

export default function TypeAnimation() {
  const [text, setText] = useState("");
  const [index, setIndex] = useState(0);
  const [charIndex, setCharIndex] = useState(0);
  const [isDeleting, setIsDeleting] = useState(false);

  useEffect(() => {
    const current = statements[index];
    let timer: ReturnType<typeof setTimeout>;

    if (!isDeleting && charIndex < current.length) {
      timer = setTimeout(() => {
        setText((prev) => prev + current[charIndex]);
        setCharIndex((prev) => prev + 1);
      }, 100);
    } else if (isDeleting && charIndex > 0) {
      timer = setTimeout(() => {
        setText((prev) => prev.slice(0, -1));
        setCharIndex((prev) => prev - 1);
      }, 50);
    } else if (!isDeleting && charIndex === current.length) {
      timer = setTimeout(() => setIsDeleting(true), 2000);
    } else if (isDeleting && charIndex === 0) {
      setIsDeleting(false);
      setIndex((prev) => (prev + 1) % statements.length);
    }

    return () => clearTimeout(timer);
  }, [charIndex, index, isDeleting]);

  return (
    <h1 className="text-3xl md:text-4xl font-bold">
      {text}
      <span className="border-r-2 border-white ml-1 animate-pulse" />
    </h1>
  );
}
