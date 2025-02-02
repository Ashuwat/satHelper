'use client';

import React from 'react';
import Image from 'next/image';
import Link from 'next/link';

export default function PrepQuestion() {
  // When clicking the left bottom card, show a mock answer (A-D)
  const handleAnswerClick = () => {
    const answers = ['A', 'B', 'C', 'D'];
    const randomAnswer = answers[Math.floor(Math.random() * answers.length)];
    alert(`Answer: ${randomAnswer}`);
  };

  return (
    <>
      {/* Navigation Bar */}
      <nav className="fixed top-0 left-0 w-full bg-[#1e1e1e] flex items-center px-6 py-4 z-30">
        {/* Replace '/logo.png' with your actual logo image path */}
        <Image src="/logo.png" alt="Logo" width={50} height={50} />
      </nav>

      {/* Main container – using IBM Plex Serif font */}
      <div
        className="flex h-screen pt-20"
        style={{ fontFamily: '"IBM Plex Serif", serif' }}
      >
        {/* Left half with blue background and icons layer */}
        <div className="relative flex w-1/2 h-screen">
          {/* Blue background layer */}
          <div className="absolute inset-0 bg-[#324DC7]"></div>
          {/* Icons background layer in front of blue background, behind cards */}
          <div
            className="absolute inset-0 bg-[url('/icon-tiles.png')] bg-[length:200px_200px] bg-center opacity-40"
            style={{ clipPath: 'polygon(0 30%, 100% 20%, 100% 100%, 0 100%)' }}
          ></div>
          {/* Card content container */}
          <div className="relative flex flex-col p-4 space-y-4 w-full">
            {/* Top half: SAT question card with a blue header */}
            <div className="flex-1 flex justify-center items-center">
              <div className="flex flex-col h-[417px] w-[750px] bg-white shadow-lg rounded-lg overflow-hidden">
                {/* (Optional: Add a header area here if needed) */}
                <div className="flex-1 flex justify-center items-center">
                  <p>Insert SAT question</p>
                </div>
              </div>
            </div>

            {/* Bottom half of the left section */}
            <div className="flex-1 flex space-x-4">
              {/* Left side: Card with answer action */}
              <div className="flex-1 flex justify-center items-center">
                <div
                  onClick={handleAnswerClick}
                  className="flex h-[400px] w-[300px] bg-white justify-center items-center shadow-lg rounded-lg cursor-pointer"
                >
                  <p>Click for Answer!</p>
                </div>
              </div>
              {/* Right side: Two small cards */}
              <div className="flex-1 flex flex-col space-y-4 justify-center items-center p-1">
                {/* Top small card: repeat.png with hover overlay */}
                <div className="relative group flex h-[150px] w-[300px] bg-white justify-center items-center shadow-lg rounded-lg cursor-pointer">
                  <Image src="/repeat.png" alt="Repeat" width={100} height={100} />
                  {/* Hover overlay */}
                  <div className="absolute inset-0 flex justify-center items-center bg-black bg-opacity-50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-lg">
                    <span className="text-white text-center px-2">
                      Generate another similar question?
                    </span>
                  </div>
                </div>
                {/* Bottom small card: Left arrow with hover overlay and routing */}
                <Link href="/">
                  <div className="relative group flex h-[150px] w-[300px] bg-white justify-center items-center shadow-lg rounded-lg cursor-pointer">
                    {/* Inline SVG arrow pointing left */}
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      width="100"
                      height="100"
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="#324DC7"
                      strokeWidth="2"
                      strokeLinecap="round"
                      strokeLinejoin="round"
                    >
                      <line x1="19" y1="12" x2="5" y2="12" />
                      <polyline points="12 19 5 12 12 5" />
                    </svg>
                    {/* Hover overlay */}
                    <div className="absolute inset-0 flex justify-center items-center bg-black bg-opacity-50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-lg">
                      <span className="text-white text-center px-2">
                        Go back and insert a new question?
                      </span>
                    </div>
                  </div>
                </Link>
              </div>
            </div>
          </div>
        </div>

        {/* Right half: Card with a large paragraph */}
        <div className="w-1/2 p-10 bg-[#E6EDF8] rounded-lg">
          <div className="bg-[#324DC7] w-full py-2 px-4 p-10 rounded-lg">
            <h2 className="text-white font-bold text-xl items-center justify-center">
              The ___ Method Example
            </h2>
          </div>
          <div className="h-full bg-white shadow-lg rounded-lg p-4 overflow-y-auto">
            <p>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed
              varius, magna in convallis interdum, odio ex condimentum augue, at
              pretium mauris nisi ac risus. Nulla facilisi. Phasellus tempus
              dolor non mauris ultricies, a feugiat libero condimentum. Vivamus
              vel ex non libero hendrerit ullamcorper. Donec maximus lacus ut
              tortor condimentum, ac vulputate urna fermentum. Donec pharetra
              commodo purus, et sagittis urna ultrices sed. Pellentesque
              habitant morbi tristique senectus et netus et malesuada fames ac
              turpis egestas. [Add as much text as you need...]
            </p>
          </div>
        </div>
      </div>
    </>
  );
}
