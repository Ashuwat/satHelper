import React from "react";

export default function SearchBar() {
  return (
    <div className="flex items-center justify-center bg-white border-4 border-[#4b9fe1] rounded-full shadow-md w-[500px] max-w-[90%] px-4 py-2">
      <input
        type="text"
        className="flex-1 outline-none border-none text-gray-700 placeholder-gray-500"
        placeholder="type your homework question and we'll find the rest:"
      />
    </div>
  );
}
